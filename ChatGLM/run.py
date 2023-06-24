import os
from typing import Dict, Tuple, Union, Optional
from torch.nn import Module
from transformers import AutoTokenizer, AutoModel
import csv
import json

def auto_configure_device_map(num_gpus: int) -> Dict[str, int]:
    # transformer.word_embeddings 占用1层
    # transformer.final_layernorm 和 lm_head 占用1层
    # transformer.layers 占用 28 层
    # 总共30层分配到num_gpus张卡上
    num_trans_layers = 28
    per_gpu_layers = 30 / num_gpus

    # bugfix: 在linux中调用torch.embedding传入的weight,input不在同一device上,导致RuntimeError
    # windows下 model.device 会被设置成 transformer.word_embeddings.device
    # linux下 model.device 会被设置成 lm_head.device
    # 在调用chat或者stream_chat时,input_ids会被放到model.device上
    # 如果transformer.word_embeddings.device和model.device不同,则会导致RuntimeError
    # 因此这里将transformer.word_embeddings,transformer.final_layernorm,lm_head都放到第一张卡上
    device_map = {'transformer.word_embeddings': 0,
                  'transformer.final_layernorm': 0, 'lm_head': 0}

    used = 2
    gpu_target = 0
    for i in range(num_trans_layers):
        if used >= per_gpu_layers:
            gpu_target += 1
            used = 0
        assert gpu_target < num_gpus
        device_map[f'transformer.layers.{i}'] = gpu_target
        used += 1

    return device_map


def load_model_on_gpus(checkpoint_path: Union[str, os.PathLike], num_gpus: int = 2,
                       device_map: Optional[Dict[str, int]] = None, **kwargs) -> Module:
    if num_gpus < 2 and device_map is None:
        model = AutoModel.from_pretrained(checkpoint_path, trust_remote_code=True, **kwargs).half().cuda()
    else:
        from accelerate import dispatch_model

        model = AutoModel.from_pretrained(checkpoint_path, trust_remote_code=True, **kwargs).half()

        if device_map is None:
            device_map = auto_configure_device_map(num_gpus)

        model = dispatch_model(model, device_map=device_map)

    return model


prompt = "问题: 一箱蜜蜂一个月大约产6千克蜂蜜，蛋糕房现需要126千克蜂蜜，大约需要多少箱蜜蜂？（答案是一个数值）。 解答:让我们一步步推理，蛋糕房需要126千克蜂蜜，一箱蜜蜂可以产6千克蜂蜜，所以需要126/6=21箱。答案是: 21" \
        "问题: 一个长方形的面积是56.7平方厘米，已知长是10厘米，宽是多少厘米？（答案是一个数值）。 解答:让我们一步步推理，长方形面积是56.7平方厘米，长是10厘米。宽是56.7/10=5.67厘米。答案是: 5.67" \
        "问题: 商场里的糖果每盒14.6元，饼干每盒29.8元。李叔叔要买4盒糖果和2盒饼干。请你算一算，李叔叔需要带多少钱？（答案是一个数值）。 解答:让我们一步步推理，糖果每盒需要14.6元，买4盒糖果需要14.6*4=58.4元。饼干每盒29.8元，买2盒饼干需要29.8*2=59.6元。所以需要带58.4+59.6=118元。答案是: 118" \
        "问题: 苹果每千克5.6元，香蕉每千克3.2元，李华买了苹果和香蕉各1.5kg，一共花了多少钱？（答案是一个数值）。 解答:让我们一步步推理，苹果每千克5.6元，买1.5kg苹果需要1.5*5.6=8.4元。香蕉每千克3.2元，买1.5千克香蕉需要1.5*3.2=4.8元。所以一共花8.4+4.8=13.2元。答案是: 13.2" \
        "问题: 1.0，4.0，9.0，16.0，多少，36.0…（答案是一个数值）。 解答:让我们一步步推理，4比1大3，9比4大5，16比9大7，以此类推，接下来一个数应该比16大9，所以16+9=25，答案是: 25" \
        "问题: 0.57×6.0的积是多少位小数？（答案是一个数值）。 解答:让我们一步步推理，0.57×6.0=3.42，所以有两位小数，答案是: 2" \
        "问题: " 



if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained("../chatglm-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("../chatglm-6b", trust_remote_code=True).half().cuda()
    model = model.eval()
    # response, history = model.chat(tokenizer, "你好", history=[])
    # print(response)
    data = []
    with open('test_out.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
            
    predict = []
    
    for i,each in enumerate(data[1:]):
        each_predict = []
        each_question  = each[-1]
        print(i)
        input = prompt + each_question + '（答案是一个数值）。 解答:让我们一步步推理，'
        for j in range(30):
            response, _ = model.chat(tokenizer, input, history=[])
            each_predict.append(response)
        predict.append(each_predict)

    with open('GLMpredict_final.json','w',encoding = 'utf-8') as f:
        json.dump(predict,f,ensure_ascii=False)

            
    
    
    # model = load_model_on_gpus("THUDM/chatglm-6b",num_gpus=4)
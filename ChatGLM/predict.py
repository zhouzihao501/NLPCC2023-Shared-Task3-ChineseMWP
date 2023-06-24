
import csv
import json
import re
import math


if __name__ == "__main__":
    data = []
    label = []
    with open('test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    for i,each in enumerate(data[1:]):
        each_label  = float(each[1])
        label.append(each_label)
        
    
    with open('GLMpredict.txt','r',encoding='utf-8') as a:
        result = a.read()
    result = eval(result)
    
    final_result = []
    
    for each_p in result:
        each_result = []
        for each in each_p:
            numbers = re.findall(r"\d+\.?\d*",each)
            if len(numbers)==0:
                each_result.append(-9999)
            else:
                each_result.append(float(numbers[-1]))
        final_result.append(each_result)
        
    
    result_dict = []
    true = 0

    for each in final_result:
        each_dict = {}
        for each_num in each:
            flag = 0
            for each_key in each_dict.keys():
                if abs(each_key-each_num)<1e-4:
                    each_dict[each_key] += 1
                    flag = 1
            if flag==0:
                each_dict[each_num] = 1
        result_dict.append(each_dict)
        
    store = [{'result':[]}]
    for each,each_la in zip(result_dict,label):
        max_num = 0
        predict = 0
        for each_pre in each.keys():
            if each[each_pre]>max_num:
                max_num = each[each_pre]
                predict = each_pre
        store[0]['result'].append(predict)
        if abs(predict-each_la)<1e-4:
            true += 1
    with open('GLMresult.json','w',encoding = 'utf-8') as f:
        json.dump(store,f,ensure_ascii=False)
    print(true/1200)
            
        
            
    
    


            
    
    
    # model = load_model_on_gpus("THUDM/chatglm-6b",num_gpus=4)
# coding: utf-8
import os
import time
import csv 
import math
import json
import pprint
import argparse
import re
import torch.optim
from tqdm import tqdm
from src.models import *
from src.pre_data import *
from src.train_and_evaluate import *
from src.expressions_transfer import *



# result_file = "result_32.txt"

valid_score = [0.256667,0.277500,0.27333,0.27333,0.275833,0.280833,0.276667,0.261667,0.2700,0.2675]

#valid_score = [0.265833,0.269167,0.270833,0.278333,0.263333,0.255,0.269167,0.255,0.265833,0.264167]


def cal_mean(all_case,label):
    all_score = []
    for i in range(10):
        each_score = []
        true = 0
        num = 0
        for predict,each_label in zip(all_case[i],label):
            predict = predict[1]
            num += 1
            if predict != None:
                if abs(predict-each_label)<1e-4:
                    true += 1
            each_score = true/num
        print(each_score)
        all_score.append(each_score)
    print('mean: '+str(sum(all_score)/10))
    

def cal_vo(all_case,label,glm,vote_index,question):
    all_data = []
    
    all_score = []
    for i in range(len(label)):
        all_score.append({})

    for i in range(10):
        for predict,each_label,each_result in zip(all_case[i],label,all_score):
            # print("all",all_score)
            # print("predict",predict)
            # print("each_label",each_label)
            # print("each_result",each_result)
            predict = predict[1]

            flag = 0
            if predict!=None:
                for each in each_result.keys():
                    if abs(each-predict)<1e-4:
                        each_result[each][0] += 1
                        each_result[each][1] += valid_score[i]
                        flag = 1
                if flag == 0:
                    each_result[predict] = [1,valid_score[i]]
            # print("each_result", each_result)

    true = 0
    bert_glm_true = 0
    max_true = 0
    for each,each_label,each_glm, each_index, each_question in zip(all_score,label,glm,solve_index,question):
        if each_index['solve_index'] == '1':
            each_question['solve_index'] = 'chatGLM'
        
        max_num = 0
        result = 0
        confi = 0
        for each_key in each.keys():
            if each[each_key][0]>max_num:
                max_num = each[each_key][0]
                result = each_key
                confi = each[each_key][1]
            elif each[each_key][0] == max_num:
                if each[each_key][1]>confi:
                    max_num = each[each_key][0]
                    result = each_key
                    confi = each[each_key][1]
                else:
                    continue
                
        if each_index["solve_index"] == "0":
            all_data.append(result)
        else:
            all_data.append(each_glm)
        
        if abs(result-each_label)<1e-4:
            each_question['bert'] = 1
            true += 1
        if abs(each_glm-each_label)<1e-4:
            each_question['LLM'] = 1
            
        if abs(each_glm-each_label)<1e-4 or abs(result-each_label)<1e-4:
            max_true += 1
            
        if each_index["solve_index"] == "1" and abs(each_glm-each_label)<1e-4 or each_index["solve_index"] == "0" and abs(result-each_label)<1e-4:
            bert_glm_true += 1
        
    #         each_score = true/num
    #     print(each_score)
    #     all_score.append(each_score)

    print('vote: '+str(true/len(label)))
    print('Bert_GLM_vote:' + str(bert_glm_true/len(label)))          
    print('max_vote:' + str(max_true/len(label)))  
    
    with open('Predict_case.json', 'w', encoding='utf-8') as file_obj:
        json.dump(question, file_obj, ensure_ascii=False, indent=2)
    
    return question,all_data


def process_result(result,question):
    result = str(result)
    if "得数保留整数" in question:
        result = result.split('.')[0]
        result = str(float(result)+1)
    elif "保留π" in question:
        result = str(float(result)/3.14)+'π'
    elif "得数保留一位小数" in question:
        result = result.split('.')[0] + '.' +result.split('.')[1][0]
    elif "末尾有多少个零" in question or "末尾有多少个0" in question:
        Len = len(result)-1
        num_0 = 0
        while result[Len]==0 and Len>0:
            num_0 += 1
            Len -= 1
        result = str(num_0)
    elif "多少位数" in question:
        result = str(len(result.split('.')[0]))
    elif "省略亿" in question:
        num_list = re.findall(r'[1-9]+\.?[0-9]*',question)
        result = str(num_list[0])
    elif "取整百" in question:
        result = str(len(result.split('.')[0]))
        result = result[:-2]+'00'
    elif "%" in question or "百分之几" in question:
        result = str(float(result)*100)
    return result


if __name__ == "__main__":
    glm_path = 'GLMresult_final.json'
    glm_data = read_json(glm_path)
    glm_data = glm_data[0]['result']
    
    solve_index = read_json('test_out_index.json')
    
    
    all_case = []
    for i in range(10):
        case_file = './model/aug_MWPbase' + str(i) + '/final_case2.json'
        predict = read_json(case_file)
        all_case.append(predict)
    label_data = read_json('./data/test_out.json')
    label = []
    question = []
    for each in label_data:
        label.append(float(each['ans']))
        question.append({'q':each['original_text'],'solve_index':'bert','bert':0,'LLM':0})
        
    cal_mean(all_case,label)
    question,all_data = cal_vo(all_case,label,glm_data,solve_index,question)

    # data = []
    # for each in label:
    #     new_each = {}
    #     new_each["id"] = each["id"]
    #     new_each["original_text"] = each["original_text"]
    #     new_each["segmented_text"] = each["original_text"]
    #     new_each["equation"] = each["output_original"]
    #     new_each["ans"] = each["ans"]
    #     data.append(new_each)
        
    # with open('./data/math_test2.json', 'w', encoding='utf-8') as file_obj:
    #     json.dump(data, file_obj, ensure_ascii=False, indent=2)
    
    # true = 0
    # num = 0
    # for each_pre,each_label in zip(predict, label):
    #     if each_pre[1] != None:
    #         x = each_label["ans"]
    #         if '(' in x:
    #             print(x)
    #             x = eval(x)
    #         elif "%" in x:
    #             x = x.replace("%",'*0.01')
    #             x = eval(x)
    #         num += 1
    #         if abs(each_pre[1]-float(x))<1e-4:
    #             true += 1
    # print(num)
    # print(true/len(predict))
    
    
    #TODO
    final_result = [['id','prediction']]
    for each,each_result,each_question in zip(label_data,all_data,question):
        each_result = process_result(each_result,each_question['q'])
        final_result.append([each['id'],str(each_result)])
    with open('submission_01_final.csv','w',encoding='utf-8') as f:
        writer =csv.writer(f)#注意delimiter这里的值必须有一个空格
        writer.writerows(final_result)
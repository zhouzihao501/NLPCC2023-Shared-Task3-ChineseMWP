#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import os
from json import loads, dumps


# In[2]:


data = pd.read_csv("/Users/jaylin/PycharmProjects/CNMWP/data/test_out.csv")
data


# In[3]:


data = data.drop("id", axis=1)
data


# In[4]:


data


# In[5]:


data = data.rename(columns={'Unnamed: 0': 'id'})
data


# In[6]:


data = data.rename(columns={'ori_text': 'segmented_text'})
data


# In[7]:


data['original_text'] = data['segmented_text']
data


# In[8]:


data["original_text"]


# In[9]:


id_id = []
for i in data["id"]:
    i = str(i)
    id_id.append(i)
data["id"] = id_id

# ans = []
# for i in data["ans"]:
#     i = str(i)
#     ans.append(i)
# data["ans"] = ans

ori = []
for i in data["original_text"]:
    i = i.replace(" ", "")
    if "l" in i:
        i = i.replace("l","1")
    ori.append(i)
data["original_text"] = ori


# In[10]:


data


# In[11]:


data["equation"] = ""
data["ans"] = "0"
data


# In[12]:


data = data.loc[:, ['id', 'original_text', 'segmented_text', 'equation','ans','num_list']]
data


# In[13]:


with open('/Users/jaylin/PycharmProjects/CNMWP/data/test_out.json','w',encoding='utf-8') as f:
    result = data.to_json(orient="records",force_ascii=False)
    parsed = loads(result)
    json_data = dumps(parsed, indent=4,ensure_ascii=False)
    f.write(json_data)
# data.to_json('/Users/jaylin/PycharmProjects/CNMWP/data/val.json', orient='records',force_ascii=False)


# In[ ]:





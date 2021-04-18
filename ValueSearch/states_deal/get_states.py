import json
import requests as rq
import copy
url = 'http://poe.game.qq.com/api/trade/data/stats'
res = rq.get(url).text
unicode2str = res
unicode2str_dict = eval(unicode2str)
imp_dicts = {}
exp_dicts = {}
enc_dicts = {}
all_dict = {}
dict_list = ['','']
explit_list = unicode2str_dict['result'][1]['entries']  #外延词缀
implit_list = unicode2str_dict['result'][2]['entries']  #基底词缀
enclit_list = unicode2str_dict['result'][4]['entries']  #附魔词缀
# len = len(unicode2str_dict['result'])
for i in unicode2str_dict['result']:
    states_dict = i['entries']
    for j in states_dict:
        dict_list[0] = j['id']
        dict_list[1] = j['type']
        if j['text'] in all_dict:
            if j['type'] != all_dict[j['text']][1]:
                print(j['text'])
                print(all_dict[j['text']])
                continue
            continue
        all_dict[copy.deepcopy(j['text'])] = copy.deepcopy(dict_list)
for i in explit_list:
    dict_list[0] = i['id']
    dict_list[1] = i['type']
    exp_dicts[copy.deepcopy(i['text'])] = copy.deepcopy(dict_list)

for i in implit_list:
    dict_list[0] = i['id']
    dict_list[1] = i['type']
    imp_dicts[copy.deepcopy(i['text'])] = copy.deepcopy(dict_list)

for i in enclit_list:
    dict_list[0] = i['id']
    dict_list[1] = i['type']
    enc_dicts[copy.deepcopy(i['text'])] = copy.deepcopy(dict_list)
print(unicode2str_dict['result'][0]['entries'])
with open("states.json", 'w+', encoding='utf-8') as f:
    json.dump(exp_dicts, f, indent=4, ensure_ascii=False)
    # for key in exp_dicts:
    #     f.write(key)
# print(unicode2str)
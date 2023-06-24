import json

def read_json(filename):
    with open(filename,"r") as f:
        json_data = json.load(f)
    return json_data

def write_json(filename,data):
    with open(filename,"w") as f:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(json_data)


if __name__ == '__main__':
    data_un = list()
    json_data = read_json("./data/test_out.json")
    for i in json_data:
        i.pop("segmented_text")
        i.pop("equation")
        i.pop("ans")
        i.pop("num_list")
        if "倍数" in i["original_text"]:
            if "自然数" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "甲" in i["original_text"] and "乙" in i["original_text"] and "丙" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "甲" in i["original_text"] and "乙" in i["original_text"] and "最大公因数" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "学生" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "A" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "约数" in i["original_text"] and "多少组" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "奇数" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "质数" in i["original_text"]:
            if "长方体" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "分数" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "小数点" in i["original_text"]:
            if "移" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "102" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "规律" in i["original_text"] and "107" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "末尾" in i["original_text"] and "除法" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "倒数" in i["original_text"] and "自然数" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "余数" in i["original_text"]:
            if "整数" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "72" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "甲" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "自然数" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "乘积" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "除数" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "151" in i["original_text"]:
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "观察" in i["original_text"] and "100" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "个位" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "10.0位" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "0位数" in i["original_text"]:
            if "本位" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "最高" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "对称" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "不重复" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "不同" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "整除" in i["original_text"] and "自然数" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "排列" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "多少种" in i["original_text"]:
            if "日报" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "明明" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "乘积" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "车站" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "楼梯" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "分母" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "元" in i["original_text"] and "角" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "补角" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "多少场" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "扑克牌" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "电话号码" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "红球" in i["original_text"] and "50" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "厘米" in i["original_text"]:
            text = i["original_text"]
            text = text.replace("厘米", "")
            if "米" in text:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "分米" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "分米" in i["original_text"]:
            text = i["original_text"]
            text = text.replace("分米", "")
            if "米" in text:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "步行5.0千米" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "千米" in i["original_text"]:
            text = i["original_text"]
            text = text.replace("千米", "")
            if "米" in text:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "上午9.0时" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "cm" in i["original_text"]:
            text = i["original_text"]
            text = text.replace("cm", "")
            if "m" in text:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "米" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "dm" in i["original_text"]:
            text = i["original_text"]
            text = text.replace("dm", "")
            if "m" in text:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "小时" in i["original_text"]:
            if "分钟" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "20.0分" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "10.0分" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "上午7" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "上午9.0" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "分钟" in i["original_text"]:
            if "秒" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "小时" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "点钟" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "到校" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "大风车" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "126" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "鸡" in i["original_text"] and "兔" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "作业" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "吨" in i["original_text"]:
            if "小麦" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "玉米" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "□" in i["original_text"]:
            if "86" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "万元" in i["original_text"]:
            if "红红" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            elif "饭店" in i["original_text"]:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "公顷" in i["original_text"] and "米" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "星期4" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "2009.0年元旦" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "小华的生日" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "千克" in i["original_text"]:
            text = i["original_text"]
            text = text.replace("千克", "")
            if "克" in text:
                i["solve_index"] = "1"
                i.pop("original_text")
                data_un.append(i)
            else:
                i["solve_index"] = "0"
                i.pop("original_text")
                data_un.append(i)
        elif "C㎡" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "布娃娃" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "下午2.0时30.0分" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "1950204650" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "数位" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "8.0月25.0日" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "7.0月25.0日" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "商的最高位" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "计数单位" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "线段" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        elif "\\u" in i["original_text"]:
            i["solve_index"] = "1"
            i.pop("original_text")
            data_un.append(i)
        else:
            i["solve_index"] = "0"
            i.pop("original_text")
            data_un.append(i)

    print(len(data_un))
    write_json("./data/test_out_index.json", data_un)

    # j_data = read_json("./data/test_out_index.json")
    # a0 = 0
    # a1 = 0
    # for i in j_data:
    #     if i["solve_index"] == "0":
    #         a0 = a0 +1
    #     else:
    #         a1 = a1 +1
    # print(a0)
    # print(a1)

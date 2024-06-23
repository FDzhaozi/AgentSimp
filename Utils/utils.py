import json
import os
import re
import matplotlib.pyplot as plt
import numpy as np
import tiktoken


def extract_docs_from_list(names, contents):
    doc_name = ""
    raw_text = ""
    ver1_text = ""
    ver2_text = ""
    ver3_text = ""
    ver4_text = ""
    for name, content in zip(names, contents):
        if name.endswith("0.txt"):
            doc_name = name.split(".")[0]
            raw_text = content
        elif name.endswith("1.txt"):
            ver1_text = content
        elif name.endswith("2.txt"):
            ver2_text = content
        elif name.endswith("3.txt"):
            ver3_text = content
        elif name.endswith("4.txt"):
            ver4_text = content
        else:
            print("error")
    return doc_name, raw_text, ver1_text, ver2_text, ver3_text, ver4_text


def split_string_into_paragraphs(text):
    # 使用split函数根据'\n\n'分割字符串
    paragraphs = text.split('\n\n')
    return paragraphs


def calc_tokens(text, model="gpt-3.5-turbo"):
    """使用openai的工具，计算文本的token数量"""
    encoding = tiktoken.encoding_for_model(model)
    """Returns the number of tokens in a text string."""
    num_tokens = len(encoding.encode(text))
    return num_tokens


def new_dir(dir_path):
    """创建一个新的文件夹"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def new_json_file(file_path):
    """创建一个新的json文件"""
    with open(file_path, 'w') as f:
        pass


def append_to_json_file(file_path, data):
    with open(file_path, 'a', encoding="utf-8") as file:
        json.dump(data, file)
        file.write('\n')


def rebuild_json_file(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as input_f:
        lines = input_f.readlines()

    json_data = []
    for line in lines:
        line = line.strip()
        if line:
            json_data.append(json.loads(line))

    with open(output_file, 'w', encoding="utf-8") as output_f:
        output_f.write(json.dumps(json_data, indent=4))


def concat_paras(paras):
    """将段落拼接成一个字符串"""
    text = ""
    for para in paras:
        text += para + "\n\n"
    return text


if __name__ == '__main__':
    path = r"D:\Desktop\FILEs\code\SimpAgents\Results\pipeline\worldcup-1950\paras.json"
    # 读取JSON文件
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    # 提取每个json中的“word_para”字段
    paras = [d["word_para"] for d in data]
    # 拼接成一个字符串
    text = concat_paras(paras)
    print(text)

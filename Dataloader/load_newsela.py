import os
import re

import nltk
import numpy as np

from Utils.utils import extract_docs_from_list


def load_newsela_doc(
        path=os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\data\newsela\articles\\",
        nums=1, random_seed=10):
    # 读取path下的所有文件
    file_list = os.listdir(path)
    # 构造正则表达式，找到所有以“0.txt”结尾的文件名
    pattern = re.compile(r'.*0.txt')
    raw_file_list = list(filter(lambda x: pattern.match(x), file_list))
    # 拿到当前文件后面的4个文件（根据在file_list中的索引）
    doc_list = []
    for file in raw_file_list:
        index = file_list.index(file)
        temp_list = file_list[index:index + 5]
        # 检查temp_list中的文件名前缀是否一致
        prefix = file.split('-')[0]
        if len(temp_list) < 5:
            continue
        else:
            flag = 0
            for i in range(1, 5):
                if prefix != temp_list[i].split('-')[0]:
                    print("文件名前缀不一致！")
                    flag = 1
            if flag == 1:
                continue
        if len(temp_list) == 5:
            doc_list.append(temp_list)
    # 随机生成nums个随机数
    np.random.seed(random_seed)
    if nums > len(doc_list):
        nums = len(doc_list)
    random_index = np.random.randint(0, len(doc_list), nums)
    # 从list中取出对应的数据
    doc_list = np.array(doc_list)[random_index]
    # print(doc_list.shape)
    # print(doc_list)
    # 读取对应的文件内容
    content_list = []
    for i in range(len(doc_list)):
        temp_list = []
        for j in range(len(doc_list[i])):
            with open(path + doc_list[i][j], 'r', encoding='utf-8') as f:
                temp_list.append(f.read())
        content_list.append(temp_list)
    return doc_list, content_list


if __name__ == '__main__':
    path = r"D:\Desktop\FILEs\code\dataset\articles\\"
    nums = 1000
    doc_list, content_list = load_newsela_doc(path, nums)
    # 开始时间
    counts = 0

    chapter_nums = 0
    paragraph_nums = 0
    sentence_nums = 0
    word_nums = 0
    words_per_chatper = 0

    for names, contents in zip(doc_list[20:], content_list[20:]):
        doc_name, raw_text, ver1_text, ver2_text, ver3_text, ver4_text = extract_docs_from_list(names, contents)
        if counts == 100:
            break
        if "spanish" in doc_name:
            continue
        counts += 1

        chapter_nums += 1
        for paragraph in raw_text.split("\n\n"):
            paragraph_nums += 1
            # 导入nltk分句
            sents = nltk.sent_tokenize(paragraph)
            for sentence in sents:
                sentence_nums += 1
                word_nums += len(nltk.word_tokenize(sentence))

    words_per_chatper = word_nums / chapter_nums

    print(f"Chapter numbers: {chapter_nums}")
    print(f"Paragraph numbers: {paragraph_nums}")
    print(f"Sentence numbers: {sentence_nums}")
    print(f"Word numbers: {word_nums}")
    print(f"Words per chapter: {words_per_chatper}")

    # Chapter
    # numbers: 100
    # Paragraph
    # numbers: 2425
    # Sentence
    # numbers: 4717
    # Word
    # numbers: 110391
    # Words
    # per
    # chapter: 1103.91


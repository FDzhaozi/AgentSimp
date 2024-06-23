import re
import json

import nltk

nltk.download('punkt')
def extract_chapters(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    chapter_pattern = r'<CHAPTER id="([^"]+)">([^<]+)</CHAPTER>'
    chapters = re.findall(chapter_pattern, content)

    extracted_data = []
    for chapter_id, chapter_content in chapters:
        book_id_pattern = r'<BOOK id="([^"]+)">'
        book_id = re.search(book_id_pattern, content).group(1)
        extracted_data.append({
            "book_id": book_id,
            "chapter_id": chapter_id,
            "content": chapter_content.strip()
        })

    return extracted_data


def export_to_json(data, file_path):
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# 使用示例
file_path = r"D:\Desktop\FILEs\code\dataset\TEST_1\test.en"
output_file_path = r"D:\Desktop\FILEs\code\dataset\TEST_1\test.json"

# extracted_data = extract_chapters(file_path)
# export_to_json(extracted_data, output_file_path)


if __name__ == '__main__':
    file_path = r"D:\Desktop\FILEs\code\dataset\TEST_2\test.json"

    # 读取JSON文件
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    chapter_nums = 0
    paragraph_nums = 0
    sentence_nums = 0
    word_nums = 0
    words_per_chatper = 0

    for chapter in data:
        chapter_nums += 1
        for paragraph in chapter["content"].split("\n"):
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
    # numbers: 12
    # Paragraph
    # numbers: 869
    # Sentence
    # numbers: 1377
    # Word
    # numbers: 20386
    # Words
    # per
    # chapter: 1698.8333333333333


    # Chapter
    # numbers: 13
    # Paragraph
    # numbers: 645
    # Sentence
    # numbers: 1373
    # Word
    # numbers: 23641
    # Words
    # per
    # chapter: 1818.5384615384614



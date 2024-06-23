import time

from Dataloader.load_newsela import load_newsela_doc
from Outputparser.ff_parser import parse_ff_output
from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5
from Utils.chat_with_4o import chat_with_4o
from Utils.utils import extract_docs_from_list, new_dir, new_json_file, append_to_json_file, rebuild_json_file


def gen_single_3_5_response(passage: str) -> str:
    prompt = f"""Please act as an editor for the task of simplifying articles. Your task is to simplify a given 
    article so that it remains easily understandable while retaining the original meaning as much as possible. You 
    may delete redundant content (paragraphs or sentences), split and combine sentences, replace complex vocabulary 
    or expressions, explain metaphorical expressions and complex emotions, etc. Please ensure that your 
    simplification results can be easily comprehended by elementary school students or non-native speakers.\n
    Original Article:\n[{passage}]\n
    Your Simplified Result:\n
    """
    return chat_with_3_5(prompt)


def gen_single_4_response(passage: str) -> str:
    prompt = f"""Please act as an editor for the task of simplifying articles. Your task is to simplify a given 
    article so that it remains easily understandable while retaining the original meaning as much as possible. You 
    may delete redundant content (paragraphs or sentences), split and combine sentences, replace complex vocabulary 
    or expressions, explain metaphorical expressions and complex emotions, etc. Please ensure that your 
    simplification results can be easily comprehended by elementary school students or non-native speakers.\n
    Original Article:\n[{passage}]\n
    Your Simplified Result:\n
    """
    return chat_with_4(prompt)


def gen_single_4o_response(passage: str) -> str:
    prompt = f"""Please act as an editor for the task of simplifying articles. Your task is to simplify a given 
    article so that it remains easily understandable while retaining the original meaning as much as possible. You 
    may delete redundant content (paragraphs or sentences), split and combine sentences, replace complex vocabulary 
    or expressions, explain metaphorical expressions and complex emotions, etc. Please ensure that your 
    simplification results can be easily comprehended by elementary school students or non-native speakers.\n
    Original Article:\n[{passage}]\n
    Your Simplified Result:\n
    """
    return chat_with_4o(prompt)


if __name__ == '__main__':
    path = r"D:\Desktop\FILEs\code\dataset\articles\\"
    nums = 50
    doc_list, content_list = load_newsela_doc(path, nums)
    # 开始时间
    start = time.time()
    nums = 0
    for names, contents in zip(doc_list[20:], content_list[20:]):
        doc_name, raw_text, ver1_text, ver2_text, ver3_text, ver4_text = extract_docs_from_list(names, contents)
        print(doc_name)
        if nums == 1:
            break
        if "spanish" in doc_name:
            continue
        nums += 1
        dir_name = r"../Results/single_agent/" + doc_name + "/"
        new_dir(dir_name)
        new_json_file(dir_name + "passages.json")

        simp_3_5_passage = gen_single_3_5_response(raw_text)
        simp_3_5_passage = parse_ff_output(simp_3_5_passage)
        simp_4_passage = gen_single_4_response(raw_text)
        simp_4_passage = parse_ff_output(simp_4_passage)
        simp_4o_passage = gen_single_4o_response(raw_text)
        simp_4o_passage = parse_ff_output(simp_4o_passage)

        passages_data = {
            "doc_name": doc_name,
            "raw_passage": raw_text,
            "ver1_passage": ver1_text,
            "ver2_passage": ver2_text,
            "ver3_passage": ver3_text,
            "ver4_passage": ver4_text,
            "simp_3.5_passage": simp_3_5_passage,
            "simp_4_passage": simp_4_passage,
            "simp_4o_passage": simp_4o_passage,
            "simp_llama_passage": "",
            "simp_mistral_passage": "",
        }
        append_to_json_file(dir_name + "passages.json", passages_data)
        rebuild_json_file(dir_name + "passages.json", dir_name + "passages.json")

    # 结束时间
    end = time.time()
    print("Time:", end - start)

from Agents.Junior_editor import gen_je_response
from Agents.Project_director import gen_pd_response
from Dataloader.load_newsela import load_newsela_doc
from Outputparser.je_parser import parse_je_output
from Utils.utils import extract_docs_from_list, split_string_into_paragraphs

if __name__ == '__main__':
    path = r"D:\Desktop\FILEs\code\dataset\articles\\"
    nums = 1
    doc_list, content_list = load_newsela_doc(path, nums)
    print(doc_list)
    print(content_list)
    for names, contents in zip(doc_list, content_list):
        doc_name, raw_text, ver1_text, ver2_text, ver3_text, ver4_text = extract_docs_from_list(names, contents)
        print(doc_name)
        guidelines = gen_pd_response(raw_text)
        paras = split_string_into_paragraphs(raw_text)
        print("paras[0]:", paras[0])
        response = gen_je_response(guidelines, paras[0])
        while response == "Invalid JSON data":
            response = gen_je_response(guidelines, paras[0])
        print(response)
        print("=========")
        print(parse_je_output(response))





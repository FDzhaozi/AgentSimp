from Agents.Project_director import gen_pd_response
from Agents.Terminology_interpreter import gen_ti_response
from Dataloader.load_newsela import load_newsela_doc
from Outputparser.ti_parser import parse_ti_output
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
        print("paras[8]:", paras[8])
        response = gen_ti_response(guidelines, paras[8])
        while response == "Invalid JSON data":
            response = gen_ti_response(guidelines, paras[8])
        print(response)
        print("=========")
        print(parse_ti_output(response))





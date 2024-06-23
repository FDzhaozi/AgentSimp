import time

from Agents.Article_architect import gen_aa_response
from Agents.Feature_fusion import gen_ff_response
from Agents.Junior_editor import gen_je_response
from Agents.Metaphor_sentiment import gen_ms_response
from Agents.Project_director import gen_pd_response
from Agents.Proofreader import gen_pf_response
from Agents.Senior_editor import gen_se_response
from Agents.Terminology_interpreter import gen_ti_response
from Dataloader.load_newsela import load_newsela_doc
from Outputparser.ff_parser import parse_ff_output
from Outputparser.je_parser import parse_je_output
from Outputparser.ms_parser import parse_ms_output
from Outputparser.se_parser import parse_se_output
from Outputparser.ti_parser import parse_ti_output
from Utils.utils import extract_docs_from_list, new_dir, new_json_file, append_to_json_file, rebuild_json_file, \
    split_string_into_paragraphs

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
        dir_name = r"../Results/synchronize/" + doc_name + "/"
        new_dir(dir_name)
        new_json_file(dir_name + "guidelines.json")
        guidelines = gen_pd_response(raw_text)
        print("guidelines:", guidelines)
        guidelines_data = {
            "doc_name": doc_name,
            "guidelines": guidelines
        }
        append_to_json_file(dir_name + "guidelines.json", guidelines_data)
        rebuild_json_file(dir_name + "guidelines.json", dir_name + "guidelines.json")

        print("=========")

        new_json_file(dir_name + "structure.json")
        structure = gen_se_response(raw_text)
        structure = parse_se_output(structure)
        while structure == "Invalid JSON data":
            print("Invalid JSON data")
            print("structure:", structure)
            print("re-generating structure...")
            structure = gen_se_response(raw_text)
            structure = parse_se_output(structure)
        print("structure:", structure)
        structure_data = {
            "doc_name": doc_name,
            "structure": structure
        }
        append_to_json_file(dir_name + "structure.json", structure_data)
        rebuild_json_file(dir_name + "structure.json", dir_name + "structure.json")

        print("=========")

        paras = split_string_into_paragraphs(raw_text)
        new_json_file(dir_name + "paras.json")
        new_json_file(dir_name + "passages.json")
        simp_passage = """"""
        meta_passage = """"""
        word_passage = """"""
        fusion_passage = """"""
        meta_count = 0
        word_count = 0
        normal_guidelines = """1.Complete the requirements as carefully as possible to serve the subsequent 
        simplified tasks.\n2.The generated content should be as easy as possible for elementary school students or 
        people with low educational levels to understand."""
        for para in paras:
            print("para:", para)
            print("=========")
            simp_para = gen_je_response(normal_guidelines, para)
            simp_para = parse_je_output(simp_para)
            while simp_para == "Invalid JSON data":
                simp_para = gen_je_response(normal_guidelines, para)
                simp_para = parse_je_output(simp_para)
            print("simp_para:", simp_para)
            print("=========")

            meta_para = gen_ms_response(normal_guidelines, para)
            meta_para = parse_ms_output(meta_para)
            while meta_para == "Invalid JSON data":
                meta_para = gen_ms_response(normal_guidelines, para)
                meta_para = parse_ms_output(meta_para)
            if meta_para == "None":
                meta_para = para
            else:
                meta_count += 1
            print("meta_para:", meta_para)
            print("=========")

            word_para = gen_ti_response(normal_guidelines, para)
            count, word_para = parse_ti_output(word_para)
            while word_para == "Invalid JSON data":
                word_para = gen_ti_response(normal_guidelines, para)
                count, word_para = parse_ti_output(word_para)
            word_count += count
            print("word_para:", word_para)
            print("=========")

            fusion_para = gen_ff_response(normal_guidelines, para, simp_para, meta_para, word_para)
            fusion_para = parse_ff_output(fusion_para)
            print("fusion_para:", fusion_para)
            print("=========")

            simp_passage += simp_para + "\n\n"
            meta_passage += meta_para + "\n\n"
            word_passage += word_para + "\n\n"
            fusion_passage += fusion_para + "\n\n"
            para_data = {
                "doc_name": doc_name,
                "para": para,
                "simp_para": simp_para,
                "meta_para": meta_para,
                "word_para": word_para,
                "fusion_para": fusion_para
            }
            append_to_json_file(dir_name + "paras.json", para_data)
            time.sleep(3)
        rebuild_json_file(dir_name + "paras.json", dir_name + "paras.json")
        arch_passage = gen_aa_response(guidelines, structure, fusion_passage)
        proof_passage = gen_pf_response(arch_passage)
        passages_data = {
            "doc_name": doc_name,
            "meta_count": meta_count,
            "word_count": word_count,
            "raw_passage": raw_text,
            "ver1_passage": ver1_text,
            "ver2_passage": ver2_text,
            "ver3_passage": ver3_text,
            "ver4_passage": ver4_text,
            "simp_passage": simp_passage,
            "meta_passage": meta_passage,
            "word_passage": word_passage,
            "fusion_passage": fusion_passage,
            "arch_passage": arch_passage,
            "proof_passage": proof_passage
        }
        append_to_json_file(dir_name + "passages.json", passages_data)
        rebuild_json_file(dir_name + "passages.json", dir_name + "passages.json")

    # 结束时间
    end = time.time()
    print("Time:", end - start)


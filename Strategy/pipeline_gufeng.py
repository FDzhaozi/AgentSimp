import time

from Agents.Article_architect import gen_aa_response
from Agents.Junior_editor import gen_je_response
from Agents.Metaphor_sentiment import gen_ms_response
from Agents.Project_director import gen_pd_response
from Agents.Proofreader import gen_pf_response
from Agents.Senior_editor import gen_se_response
from Agents.Terminology_interpreter import gen_ti_response
from Dataloader.load_gufeng import extract_chapters
from Outputparser.je_parser import parse_je_output
from Outputparser.ms_parser import parse_ms_output
from Outputparser.se_parser import parse_se_output
from Outputparser.ti_parser import parse_ti_output
from Utils.utils import extract_docs_from_list, new_dir, new_json_file, append_to_json_file, rebuild_json_file, \
    split_string_into_paragraphs

if __name__ == '__main__':
    file_path = r"D:\Desktop\FILEs\code\dataset\TEST_1\test.en"
    ch_path = r"D:\Desktop\FILEs\code\dataset\TEST_1\test.zh"
    gufeng_data = extract_chapters(file_path)
    zh_data = extract_chapters(ch_path)
    num = 0
    for en, zh in zip(gufeng_data[8:10], zh_data[8:10]):
        print(en)
        print(zh)
        num+=1
        book_id = en["book_id"]
        chapter_id = en["chapter_id"]
        doc_name = f"{book_id}_{chapter_id}_{num}"
        raw_text = en["content"]
        ch_text = zh["content"]
        dir_name = r"../Results/pipeline/" + doc_name + "/"
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

        paras = raw_text.split("\n")
        new_json_file(dir_name + "paras.json")
        new_json_file(dir_name + "passages.json")
        simp_passage = """"""
        meta_passage = """"""
        word_passage = """"""
        meta_count = 0
        word_count = 0
        normal_guidelines = """1.Complete the requirements as carefully as possible to serve the subsequent
        simplified tasks.\n2.The generated content should be as easy as possible for elementary school students or
        people with low educational levels to understand."""
        for para in paras:
            if para == "":
                continue
            print("para:", para)
            print("=========")
            simp_para = gen_je_response(normal_guidelines, para)
            simp_para = parse_je_output(simp_para)
            while simp_para == "Invalid JSON data":
                simp_para = gen_je_response(normal_guidelines, para)
                simp_para = parse_je_output(simp_para)
            print("simp_para:", simp_para)
            print("=========")

            meta_para = gen_ms_response(normal_guidelines, simp_para)
            meta_para = parse_ms_output(meta_para)
            while meta_para == "Invalid JSON data":
                meta_para = gen_ms_response(normal_guidelines, simp_para)
                meta_para = parse_ms_output(meta_para)
            if meta_para == "None":
                meta_para = simp_para
            else:
                meta_count += 1
            print("meta_para:", meta_para)
            print("=========")

            word_para = gen_ti_response(normal_guidelines, meta_para)
            count, word_para = parse_ti_output(word_para)
            while word_para == "Invalid JSON data":
                word_para = gen_ti_response(normal_guidelines, meta_para)
                count, word_para = parse_ti_output(word_para)
            word_count += count
            print("word_para:", word_para)
            print("=========")

            simp_passage += simp_para + "\n\n"
            meta_passage += meta_para + "\n\n"
            word_passage += word_para + "\n\n"
            para_data = {
                "doc_name": doc_name,
                "para": para,
                "simp_para": simp_para,
                "meta_para": meta_para,
                "word_para": word_para
            }
            append_to_json_file(dir_name + "paras.json", para_data)
            time.sleep(3)
        rebuild_json_file(dir_name + "paras.json", dir_name + "paras.json")
        arch_passage = gen_aa_response(guidelines, structure, word_passage)
        proof_passage = gen_pf_response(arch_passage)
        passages_data = {
            "doc_name": doc_name,
            "meta_count": meta_count,
            "word_count": word_count,
            "raw_passage": raw_text,
            "ch_passage": ch_text,
            "simp_passage": simp_passage,
            "meta_passage": meta_passage,
            "word_passage": word_passage,
            "arch_passage": arch_passage,
            "proof_passage": proof_passage
        }
        append_to_json_file(dir_name + "passages.json", passages_data)
        rebuild_json_file(dir_name + "passages.json", dir_name + "passages.json")



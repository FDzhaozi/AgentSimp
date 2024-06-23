from Utils.utils import new_json_file, new_dir, append_to_json_file, rebuild_json_file

if __name__ == '__main__':
    doc_name = "newsela_pa"
    new_dir(r"../Results/pipeline/"+doc_name+"/")
    new_json_file(r"../Results/pipeline/"+doc_name+"/"+"data.json")
    json_data_1 = {
        "doc_name": doc_name,
        "guidelines": "guidelines",
        "paras": "paras",
        "response": "response",
        "parsed_output": "parsed_output"
    }
    json_data_2 = {
        "doc_name": "hello",
        "guidelines": "guidelines",
        "paras": "paras",
        "response": "response",
        "parsed_output": "parsed_output"
    }
    append_to_json_file(r"../Results/pipeline/"+doc_name+"/"+"data.json", json_data_1)
    append_to_json_file(r"../Results/pipeline/"+doc_name+"/"+"data.json", json_data_2)
    rebuild_json_file(r"../Results/pipeline/"+doc_name+"/"+"data.json",r"../Results/pipeline/"+doc_name+"/"+"data.json")

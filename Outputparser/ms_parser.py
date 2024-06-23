import json
import re


def parse_ms_output(json_data: str) -> str:
    # 将JSON字符串解析为Python字典
    json_data = json_data.replace("```json", "").replace("```", "")
    try:
        data = json.loads(json_data)
    except:
        pattern = r'"simplified result":\s*([^}]*)\s*}'

        # 使用正则表达式搜索匹配项
        match = re.search(pattern, json_data)

        # 如果找到匹配项，则提取文本内容
        if match:
            extracted_text = match.group(1)
            return extracted_text
        else:
            return "Invalid JSON data"
    if "analyzed result" not in data or "simplified result" not in data:
        return "Invalid JSON data"
    if data["analyzed result"] == "None":
        return "None"
    else:
        return data["simplified result"]

if __name__ == '__main__':
    # 假设json_data是你要读取的JSON字符串
    json_data = '''
    {
        "simplified result": "Navajo Nation Implements Junk Food Tax to Combat Health Issues"
    }
    '''

    # 调用函数解析JSON数据
    output = parse_ms_output(json_data)
    print(output)

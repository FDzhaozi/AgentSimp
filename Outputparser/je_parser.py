import json
import re


def parse_je_output(json_data: str) -> str:
    # 将JSON字符串解析为Python字典
    # 清除```json 和 ```标记
    json_data = json_data.replace("```json", "").replace("```", "")
    try:
        if "simplified result" not in json_data:
            return "Invalid JSON data"
        data = json.loads(json_data)
    except:
        # print("Invalid JSON data")
        # print(json_data)
        # return "Invalid JSON data"
        pattern = r'"simplified result":\s*([^}]*)\s*}'

        # 使用正则表达式搜索匹配项
        match = re.search(pattern, json_data)

        # 如果找到匹配项，则提取文本内容
        if match:
            extracted_text = match.group(1)
            return extracted_text
        else:
            return "Invalid JSON data"
    return data["simplified result"]


if __name__ == '__main__':
    # 假设json_data是你要读取的JSON字符串
    json_data = '''
    {
        "simplified result": "Navajo Nation Implements "Junk Food Tax to Combat Health Issues
    }
    '''

    # 调用函数解析JSON数据
    output = parse_je_output(json_data)
    print(output)

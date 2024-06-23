import json
import re


def parse_ti_output(json_data: str) -> tuple[int, str]:
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
            return 0, extracted_text
        else:
            return 0, "Invalid JSON data"
    if "terminology" not in data or "parsed result" not in data:
        return 0, "Invalid JSON data"
    # count of data["terminology"]
    count = len(data["terminology"])

    return count, data["parsed result"]


if __name__ == '__main__':
    pass
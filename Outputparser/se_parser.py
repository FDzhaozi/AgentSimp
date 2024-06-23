import json


def parse_se_output(json_data: str) -> str:
    # 将JSON字符串解析为Python字典
    json_data = json_data.replace("```json", "").replace("```", "")
    out_str = """"""
    try:
        data = json.loads(json_data)
    except:
        return "Invalid JSON data"
    if "title" not in data or "subheadings" not in data:
        return "Invalid JSON data"

    # 打印标题
    out_str += "Title: " + data["title"] + "\n"
    # 打印子标题
    out_str += "Subheadings:" + "\n"
    for subheading in data["subheadings"]:
        out_str += "## " + subheading + "\n"
    return out_str


if __name__ == '__main__':
    # 假设json_data是你要读取的JSON字符串
    json_data = '''
    {
        "title": "Navajo Nation Implements Junk Food Tax to Combat Health Issues",
        "subheadings": [
            "Introduction to the Junk Food Tax Initiative",
            "Challenges Faced by Navajo Nation Residents",
            "Details of the Junk Food Tax Legislation",
            "Impact on Local Grocery Stores",
            "Community Response and Advocacy Efforts",
            "Historical Context and Cultural Relationship with Food",
            "Hopes for Future Health Improvements"
        ]
    }
    '''

    # 调用函数解析JSON数据
    output = parse_se_output(json_data)
    print(output)

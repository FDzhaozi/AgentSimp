import json


def parse_ff_output(text: str) -> str:
   # 将包裹在[]中的文本提取出来
    if "[" not in text:
       return text
    text = text[text.find("[") + 1:text.find("]")]
    return text



if __name__ == '__main__':
    # 假设json_data是你要读取的JSON字符串
    text = """hello world [this is a test] hello world"""

    # 调用函数解析JSON数据
    output = parse_ff_output(text)
    print(output)

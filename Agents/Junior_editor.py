from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5


def gen_je_response(guidelines: str, paragraph: str) -> str:
    prompt = f"""Please act as a junior editor for the task of simplifying articles. You are given a paragraph from 
    the article (which may also just be a sentence). Your task is to simplify this section while trying to ensure 
    that the original meaning remains intact, making it more easily understandable. The methods you may use include 
    deleting sentences, splitting and combining sentences, reordering sentences, and replacing complex words with 
    simpler terms. Additionally, before simplifying, you need to read a set of guidelines and try to follow the 
    requirements outlined in them during the simplification process. Your output format must be in JSON format: {{
    "simplified result":"This is the simplified content"}}.

    The guidelines:\n[{guidelines}]
    The paragraph need to be simplified:\n[{paragraph}]
    Please provide the results according to my requirements and output format, without any additional explanations:   
    """
    return chat_with_4(prompt)




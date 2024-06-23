from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5


def gen_pf_response(article: str) -> str:
    prompt = f"""Please act as a proofreader for the task of simplifying articles. Your role is to check an article 
    for logical errors, content mistakes, grammatical errors, etc. Your output format must be in JSON format: {{ 
    "mistakes": "here are the mistakes found in the article, if none, fill in 'None'", "corrected article":"if 
    'mistakes' is 'None', here is 'None', Otherwise, the corrected complete article needs to be provided here"}}. 

    The simplified article:\n[{article}]\n
    Please provide the results according to my requirements and output format, without any additional explanations:   
    """
    return chat_with_4(prompt)
Please act as a proofreader for the task of simplifying articles. Your role is to check an article
    for logical errors, content mistakes, grammatical errors, etc. Your output format must be in JSON format: {{
    "mistakes": "here are the mistakes found in the article, if none, fill in 'None'", "corrected article":"if 
    'mistakes' is 'None', here is 'None', Otherwise, the corrected complete article needs to be provided here"}}.

    The simplified article:\n[{article}]\n
    Please provide the results according to my requirements and output format, without any additional explanations:  
from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5


def gen_ti_response(guidelines: str, paragraph: str) -> str:
    prompt = f"""Please act as a ‘Terminology Interpreter’ for the task of simplifying articles. You are given a 
    paragraph from the article (which may also just be a sentence) that requires terminology explanation. Here are 
    several examples for your reference: [derivatives(financial contracts that get their value from other things like 
    stocks, bonds, commodities, or currencies. It's like making a bet on the price or performance of these 
    things.);\n resilience(means being able to quickly recover when faced with tough times or challenges;\n Cognitive 
    flexibility: The capacity to adapt and switch between different thinking strategies or mental frameworks when 
    faced with changing situations or problems.]

    You need to read a set of guidelines which could be helpful for you to analyze the terminology. Your output 
    format must be in JSON format: {{ "terminology": ["terminology1","terminology2","terminology3"...], 
    "parsed result":"Here, still place the original paragraph, with the only difference being that every 
    terminologies has been replaced by an easy-to-understand explanation(Use simple words as much as possible)."}}.

    The guidelines:\n[{guidelines}]
    The paragraph need to be parsed:\n[{paragraph}]
    Please provide the results according to my requirements and output format, without any additional explanations:   
    """
    return chat_with_4(prompt)




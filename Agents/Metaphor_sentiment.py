from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5


def gen_ms_response(guidelines: str, paragraph: str) -> str:
    prompt = f"""Please act as a metaphorical sentiment analyst for the task of simplifying articles. You are given a 
    paragraph from the article (which may also just be a sentence) that requires metaphorical sentiment analysis. 
    
    You need to read a set of guidelines which could be helpful for you to analyze the 
    metaphorical sentiment. Your output format must be in JSON format: {{ "analyzed result":"Here are sentences with 
    metaphorical emotional phenomena and corresponding explanations(Fill in "None", if no metaphor and complex 
    sentiment).", "simplified result":"This is a modification to the original text based on metaphorical sentiment 
    analysis. It is best to add parentheses in the original text to explain but do not require any other changes. (If 
    the analyzed result is "None", then the simplified result is also "None")"}}.

    The guidelines:\n[{guidelines}]
    
    Here are several examples involving metaphors and complex sentiment analysis: [1. Metaphor: - "She has a heart of 
    gold." (Used to describe someone's kindness and compassion, not their literal heart) - "Time is money." (Used to 
    convey the value of time, not the literal exchange of time for currency) 2. Simile: - "He runs like a cheetah." ( 
    Comparing someone's running speed to that of a cheetah) - "She is as brave as a lion." (Comparing someone's 
    bravery to that of a lion) 3. Sarcasm: - "Well, that's just what I needed, more work piled on my desk." ( 
    Expressing sarcasm to convey frustration about an increased workload) - "Fantastic! I just missed my train." ( 
    Using irony to express disappointment or frustration) 4. Hidden logic: - Health advocates claim that fast food 
    chains exerted influence to exclude their products from the classification of unhealthy options in the proposed 
    regulations.(Fast food chains hope that their products are healthy and legal, but health advocates may hold the 
    opposite view.)] \n
    
    The paragraph need to be analyzed:\n[{paragraph}]
    Please provide the results according to my requirements and output format, without any additional explanations:   
    """
    return chat_with_4(prompt)




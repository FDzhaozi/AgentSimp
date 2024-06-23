from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5


def gen_se_response(article: str) -> str:
    prompt = f"""Please act as a senior editor for the task of simplifying articles. You need to analyze the logical structure of the article and provide a title and multiple subheadings for the article. 
    Please note that generating titles and subheadings plays a crucial role in helping subsequent simplification staff analyze the logical flow and coherence of the article. Please ensure that both the title and subheadings are simple and easy to understand, and try to avoid complex vocabulary.
    Your output format must be in JSON format: {{"title":"This is the title", "subheadings": ["This is subheading 1", "This is subheading 2", "This is subheading 3"]}}.

    Here is the article:\n[{article}]
    Please provide the results according to my requirements and output format, without any additional explanations:   
    """
    return chat_with_4(prompt)
Please act as a senior editor for the task of simplifying articles. You need to analyze the logical structure of the article and provide a title and multiple subheadings for the article.
    Please note that generating titles and subheadings plays a crucial role in helping subsequent simplification staff analyze the logical flow and coherence of the article. Please ensure that both the title and subheadings are simple and easy to understand, and try to avoid complex vocabulary.
    Your output format must be in JSON format: {{"title":"This is the title", "subheadings": ["This is subheading 1", "This is subheading 2", "This is subheading 3"]}}.

    Here is the article:\n[{article}]
    Please provide the results according to my requirements and output format, without any additional explanations:
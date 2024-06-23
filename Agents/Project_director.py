from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5

def gen_pd_response(article: str) -> str:
    prompt = f"""Please act as a project instructor for the task of simplifying articles. The guidelines for simplifying an article, which are crucial for guiding subsequent agents in the simplification process, may contain the following information:
    1. Executive Summary:
       - A brief overview of the article's main points, arguments, and conclusions.
    2. Style and Tone:
       - A description of the article's style (such as formal, informal, academic, creative writing, etc.) ,and domain(science, history, sport, etc.), and overall tone (such as objective, subjective, humorous, serious, etc.).
    3. Target Audience:
       - A clear identification of the intended readership for the simplified article, including their age, educational level, cultural background, and language proficiency(Please provide a specific hypothesis to indicate that the reader's reading ability is not strong.).
    4. Key Concepts and Terminology:
       - A list of core concepts, specialized terms, and key words used in the article, along with their definitions and contextual meanings.
    5. Main Arguments and Evidence:
       - An outline of the article's main arguments and the key evidence or examples that support these arguments.
    6. Cultural and Social Context:
       - Information about the cultural, historical, or social context mentioned in the article, to be appropriately addressed during simplification.
    7. Emotions and Attitudes:
       - Identification of the emotions and attitudes expressed in the article, ensuring that these nuances are preserved throughout the simplification process.

    Here is the article:\n[{article}]
    The content of the guidelines should be as concise and to the point as possible. Please list the guidelines I need in the format I specify (a total of seven aspects), without any additional explanations:   
    """
    return chat_with_4(prompt)
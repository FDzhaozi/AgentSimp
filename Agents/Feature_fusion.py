from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5


def gen_ff_response(guidelines: str, paragraph: str, simp_para: str, meta_para: str, word_para: str) -> str:
    prompt = f"""Please act as an expert in simplification feature fusion for the task of simplifying articles. You 
    are given an original paragraph from the article, along with several different simplified versions of the same 
    paragraph. These simplification methods include basic simplification, metaphorical sentiment interpretation, 
    and complex terminology explanation. What you need to do is fuse all the simplification features from the 
    original paragraph and its corresponding three simplified versions to produce a final, optimal simplified 
    paragraph. 
    The guidelines:\n[{guidelines}]\n
    original paragraph:\n [{paragraph}]\n
    Basic Simplification:\n [{simp_para}]\n
    Metaphorical Simplification:\n [{meta_para}]\n
    Terminology Simplification:\n [{word_para}]\n
    Fusion Simplification:\n  
    """
    return chat_with_4(prompt)

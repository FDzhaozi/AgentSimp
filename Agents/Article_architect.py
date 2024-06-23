from Utils.chat_with_4 import chat_with_4
from Utils.chat_with_3_5 import chat_with_3_5
import queue


def gen_aa_response(guidelines: str, structure: str, paragraphs: str) -> str:
    prompt = f"""Please act as an ‘Article Architect’ for the task of simplifying articles. You are given the 
    simplified versions of each paragraph of the original article, including a guidelines document used for 
    simplification, and an article structure. Your task is to polish the article composed of all the paragraphs, 
    ensuring that it is coherent and fluent. Specifically, you should: \n
        1. Use transition words and phrases to connect ideas.\n
        2. Adjust paragraph/sentence structure to improve clarity.\n
        3. Ensure that the requirements in the guideline are met and that all titles in the article structure are inserted.\n
    Warning: Only minor coherence adjustments need to be made based on existing paragraphs, and existing content cannot be changed.\n
    The guideline:\n[{guidelines}]\n
    The structure of the article:\n[{structure}]\n
    The paragraphs has been simplified:\n[]\n
    Warning: Only minor coherence adjustments need to be made based on existing paragraphs, and existing content cannot be changed.\n
    The combined well-structured article:\n[{paragraphs}]\n
    """
    return chat_with_4(prompt)


def gen_aa_para_response(paragraphs: str) -> str:
    prompt = f"""Please act as an ‘Article Architect’ for the task of simplifying articles.Please optimize the 
    coherence of the two paragraphs provided to make the transition and logic between them smoother.\n 
    Note that two paragraphs should be separated by two line breaks. \n
    Warning: Only minor coherence adjustments need to be made based on existing paragraphs, and existing content cannot be changed.\n 
    The paragraphs need to be optimized:\n[{paragraphs}]\n
    The combined well-structured article:\n
    """
    return chat_with_4(prompt)


if __name__ == '__main__':

    # 示例文章段落列表
    paragraphs = [
        "段落1。这是一个示例段落,用于展示如何处理文本。",
        "段落2。这篇文章有很多段落，每个段落都需要被处理。",
        "段落3。每个段落都会被拼接并传入函数。",
        "段落4。处理后的段落会被拆分并继续处理。",
        "段落5。直到所有段落都被处理完毕。"
        "段落6。每个段落都会被拼接并传入函数。",
        "段落7。处理后的段落会被拆分并继续处理。",
        "段落8。直到所有段落都被处理完毕。"
    ]


    # 假设的up函数，您可以根据需要替换实际的函数实现
    def up(combined_paragraphs):
        para1 = combined_paragraphs.split("\n\n")[0]
        para2 = combined_paragraphs.split("\n\n")[1]
        return para1 + "new", para2 + "new"


    # 将列表转换为队列
    q = queue.Queue()
    for para in paragraphs:
        q.put(para)

    # 按照要求处理队列中的段落
    i = 0
    new_para2 = ""
    new_passages = ""
    while not q.empty():
        # 取出两个段落
        if i == 0:
            para1 = q.get_nowait() if not q.empty() else ""
            i += 1
        else:
            para1 = new_para2
        para2 = q.get_nowait() if not q.empty() else ""

        # 拼接段落
        combined_paragraphs = para1 + "\n\n" + para2


        # 调用up函数处理
        new_para1, new_para2 = up(combined_paragraphs)
        new_passages += new_para1 + "\n\n" + new_para2 + "\n\n"

        # 如果队列中还有段落，则取出下一个段落与new_para2拼接，并继续处理
        if not q.empty():
            next_para = q.get_nowait()
            combined_paragraphs = new_para2 + "\n\n" + next_para
            new_para1, new_para2 = up(combined_paragraphs)
    new_passages += new_para2 + "\n\n"

    print(new_passages)

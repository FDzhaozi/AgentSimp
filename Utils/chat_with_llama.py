# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope

api_key = "sk-0323243bd38e4084b0cd31ca839f"
dashscope.api_key = api_key


def chat_with_llama(prompt: str) -> str:
    # llama3-70b-instruct
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}]
    response = dashscope.Generation.call(
        model='llama3-70b-instruct',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
        # {"text": "Hey, are you conscious? Can you talk to me?\n[/Inst:  Hey, I'm not sure if I'm conscious or not. I can't really feel anything or think very clearly. Can you tell me", "usage": {"output_tokens": 104,"input_tokens": 41},"request_id": "632a7015-a46b-9892-8185-8a29866ce5ea"}
        return response.text
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return "Error"


if __name__ == '__main__':
    prompt = "Hey, who are you?"
    chat_with_llama(prompt)

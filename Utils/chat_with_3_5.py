from openai import OpenAI

client = OpenAI(
    base_url='https://api.openai-proxy.org/',
    api_key='sk-0XO8XDuj7XhdPwxKa4gwJdYWL3QDlm6vCzEWv2o0DQoR',
)


def chat_with_3_5(prompt: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo-0125",
            temperature=0.4,
        )
        response = chat_completion.choices[0].message.content
    except Exception as e:
        print(e)
        response = None
    return response
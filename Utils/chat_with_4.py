from openai import OpenAI

client = OpenAI(
    base_url='https://api.openai-proxy.org/v1',
    api_key='sk-0XO8XDuj7XhdPwxKa4gwJdYWL3QDlm6vCzEWv2o0DQo6',
)


def chat_with_4(prompt: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o",
            temperature=0.4,
        )
        response = chat_completion.choices[0].message.content
    except Exception as e:
        print(e)
        response = None
    return response
import openai
from pydantic import BaseModel

openai.organization = 'org-VuqI6upRDoGnYHHjA7hWBHkS'
openai.api_key = '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'


class Document(BaseModel):
    item: str = ''


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        temperature = 0.2,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación a nivel universitaria y me vas a responder claro y conciso todo lo que te vaya a preguntar.
        E.G
        
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [content, total_tokens]

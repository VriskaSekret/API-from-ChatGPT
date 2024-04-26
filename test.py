from openai import OpenAI

import os

import pandas as pd

import time

client = OpenAI(api_key="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")


def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(

    model=model,

    messages=messages
    )

    return response.choices[0].message.content


prompt = input("tell me a prompt: ")

response = get_completion(prompt)

print(response)
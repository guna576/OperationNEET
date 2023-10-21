import openai
import os
import pandas as pd
import time
import gradio as gr

openai.api_key = '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'
def get_completion(prompt="", model="gpt-3.5-turbo"):
    try:
        messages = [{"role": "user", "content": "Hi, AI"}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        )

        return response.choices[0].message["content"]
    except:
        return "There is error in communicating with the AI"

demo = gr.Interface(
    fn=get_completion,
    inputs=["text"],
    outputs=["text"],
)
demo.launch(share=True)


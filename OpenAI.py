# RPG Game with chatGPT
# Class for OpenAI

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI



class OpenAI:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.client = OpenAI()
        self.model = "gpt-3.5-turbo"

    def return_completion(self, messages):
        completion = self.clientclient.chat.completions.create(
        model=self.model,
        messages=messages
        )
        return completion.choices[0].message.text
    
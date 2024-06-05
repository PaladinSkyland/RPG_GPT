# RPG Game with chatGPT
# Class for OpenAI
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI



class OpenAIclass:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.client = OpenAI()
        self.model = "gpt-3.5-turbo"

    def return_completion(self, messages):
        response = self.client.chat.completions.create(
        model=self.model,
        response_format={ "type": "json_object" },
        messages=messages
        )
        return response.choices[0].message.content
    
    def system_message(self, message):
        return {
            "role": "system",
            "content": message
        }
    
    def user_message(self, message):
        return {
            "role": "user",
            "content": message
        }
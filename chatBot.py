from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
key_token = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=key_token)

def costum_chatbot(user_prompt:str, all_messages:list ) -> list:
    each_response = "No data"
    if user_prompt.lower() !='':
        all_messages.append( {"role": "user", "content":  user_prompt})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            #model="gpt-4o",
            #model="gpt-4o-2024-05-13",
            messages=all_messages,
            temperature=0.7,
            max_tokens=100,
            frequency_penalty=0,
            presence_penalty=0,
        )
        each_response = response.choices[0].message.content
        all_messages.append( {"role": "assistant", "content":  each_response})
    return each_response

#test function costum_chatbot
#print(costum_chatbot("do you know brahim diaz?", all_messages=list()))

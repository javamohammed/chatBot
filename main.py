from fastapi import FastAPI
from chatBot import costum_chatbot

app = FastAPI(debug=True)
all_messages = list()
prompt_system ='Answer as concisely as possbile'
all_messages.append( {"role": "system", "content":  prompt_system})

@app.get("/costum_chatbot_url")
async def costum_chatbot_url(prompt: str) -> str:
    response:str = costum_chatbot(user_prompt=prompt, all_messages=all_messages )
    return response
    

#uvicorn main:app --reload #To run fastApi service

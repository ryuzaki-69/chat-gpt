import os 
import gradio
from dotenv import load_dotenv
import openai
load_dotenv()
messages = []
openai.api_key = os.getenv("key")




def GPT(Input):
    message=[]
    messages.append({"role":"user","content":Input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )
    result= response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":result})
    return result

gradio = gradio.Interface(fn=GPT,inputs="text",outputs="text",title="CHAT-GPT")
gradio.launch(share=True)
    
            














# print("I am ready to help you!")
# while input != "exit()":
    
#     message = input("What do you wanna search?\n:- ")
#     messages.append({"role":"user","content":message})
#     result= response["choices"][0]["message"]["content"]response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages=messages
#     )
    
#     messages.append({"role":"assistant","content":result})
#     print("\n"+result+"\n")
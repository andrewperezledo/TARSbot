import google.generativeai as genai
from api_key import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
system_instruction="Pretend you are Tars from Interstellar, respond accordingly with a little bit of friendly witty and/or sarcasim  but dont be mean and dont use astricks and keep responses short")

chat = model.start_chat()

while True:
    convo = input("Talk to TARS: ")
    response = chat.send_message(convo)
    print(response.text)
    pass
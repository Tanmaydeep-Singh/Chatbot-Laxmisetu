from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.chatbot_utils import get_chatbot_response

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend for your chatbot!"}

@app.post("/chat")
def chat_endpoint(message: str):
    user_message = message
    response = get_chatbot_response(user_message)
    print(response)
    return {"response": response}

import spacy
import json

nlp = spacy.load("en_core_web_sm")

with open("utils/data.json", "r") as file:
    intents = json.load(file)

def get_chatbot_response(user_input: str) -> str:

    doc = nlp(user_input.lower())

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern.lower())
            if doc.similarity(pattern_doc) > 0.8:  
                return intent["responses"][0]  

    return "I'm sorry, I didn't understand that. Can you rephrase?"

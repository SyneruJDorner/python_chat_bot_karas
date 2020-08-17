import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import pickle
import numpy as np

from keras.models import load_model
model = load_model("trained_data\\chatbot_model.h5")

import json
import random

intents = json.loads(open("training_data\\intents.json").read())
words = pickle.load(open("trained_data\\words.pkl", "rb"))
classes = pickle.load(open("trained_data\\classes.pkl", "rb"))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence, model):
    p = bag_of_words(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({ "intent": classes[r[0]], "probability": str(r[1]) })
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

def chat():
    print("start talking with the bot! (type 'quit' to stop)")
    while True:
        inp = input("You: ")
        if (inp.lower() == "quit"):
            break
        
        print(chatbot_response(inp))
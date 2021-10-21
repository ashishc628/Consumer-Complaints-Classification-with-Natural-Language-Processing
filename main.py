from fastapi import FastAPI
from typing import Optional
import uvicorn
import numpy as np
import pickle
import re
import string
import pandas as pd
import nltk
import joblib
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
s = set(stopwords.words('english'))
app = FastAPI(title="Sentiment Model API",
    description="A simple API that use NLP model to predict the sentiment of the CoronaVirus Tweets ",
    version="0.1",)
from pydantic import BaseModel
class Text(BaseModel):
    text : str
model3 = pickle.load(open('rfc.pkl',"rb"))
bow_vec = pickle.load(open('bow_vec.pkl',"rb"))

#Definitions
def remove_spaces(data):
    res = re.sub(' +', ' ',data)
    return res

@app.get("/greet/{text}")
def greeting(text:str):
    return {"Hi {} welcome to twitter Sentmental Analysis".format(text)}


@app.post("/predict")
def Predict_Sentiment(item:Text):
    text_input = item.text
    df = pd.DataFrame([text_input],columns=['text'])
    df['text'] = df['text'].str.lower()
    df['text'] = df['text'].str.replace("[^a-zA-Z]", " ")
    df['text'] = df['text'].apply(lambda x: " ".join([w for w in x.split() if len(w)>3]))
    bow1 = bow_vec.transform( df['text'])
    final = pd.DataFrame(bow1.toarray())
    prediction = model3.predict(final)
    if prediction == 1 :
        print("credit_reporting")
    elif prediction== 2:
        print("debt_collection")
    elif prediction== 3:
        print("mortgages_and_loans")
    elif prediction== 4:
        print("credit_card")
    else:
        print("retail_banking")
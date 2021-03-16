import requests
import configparser
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    s=''
    if request.method == 'POST':
        from textblob import TextBlob
        r = request.form['r'] 
        edu=TextBlob(r)
        x=edu.sentiment.polarity
        
        if x==0:
            s = "Neutral"
        elif x<0:
            s = "Negative"
        elif x>0 and x<=1:
            s = "Positive"
    return render_template('index.html', Result = s)

if __name__ == '__main__':
    app.run(debug=True) 
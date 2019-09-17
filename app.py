from flask import Flask
from textblob import TextBlob
app = Flask(__name__)

@app.route('/<message>')
def index(message):
    sentiment = "neutral"
    if(TextBlob(message).sentiment.polarity< 0.0):
        sentiment="negative"
    if(TextBlob(message).sentiment.polarity> 0.0):
        sentiment="positive"
    return app.make_response(sentiment)
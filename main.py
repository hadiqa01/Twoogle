from flask import Flask, render_template, request
import pandas as pd
from transformers import pipeline, DistilBertForSequenceClassification, DistilBertTokenizerFast
import tweepy


# Private credentials to be withdrawn at the end of Spring '21
KEY = "WD9TVjUQFAf5m6XuWMJd7vErs" # API Key
SECRET =  "OtKCZvwqqBDiBMqdgip2BCE4Z9N6JpK6yg6ylNDYYxMhun29mn" # API Secret Key
TOKEN = "1384529505696559104-Cxr6keJipox3TCJbBVsIz91poKkyPT" # Access Token
TOKEN_SECRET = "aIDnNeJBKgupUnUBl8V3Sz0DWWCCpAM9cNFtg8LBRlgga" # Access Token Secret

# Sentiment classes
LABELS = {'LABEL_0': 'NEGATIVE', 'LABEL_1': 'POSITIVE'}

# Initialize Twitter API client
auth = tweepy.OAuthHandler(KEY, SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/getTweets')
def getTweets():
    print("Getting tweets now ...")

    # Default keyword if you hit search
    keyword = request.args.get('keyword',
                               default='coronavirus covid vaccine vaccination COVID-19')
    
    # Fetch the 20 most recent tweets matching the query. Change the argument
    # in `items()` to decrease or increase the number of retrieved tweets.
    # The larger the number the longer the retreival time
    query = keyword # text from the search box
    tweets_ = tweepy.Cursor(api.search, query, result_type='recent').items(20)
    tweets = [tweet.text for tweet in tweets_]    

    print("Done ... retrieving tweets from API based on the keyword=" + keyword)
 
    df = pd.DataFrame(data=tweets, columns=['Tweet'])
    print("Done ... creating dataframe")

    # Iterate over the tweet texts in `tweets` and pass each item to the model
    # to obtain a prediction, then write those predictions to a Pandas dataframe
    model = pipeline('sentiment-analysis',
            model=DistilBertForSequenceClassification.from_pretrained("model"),
            tokenizer=DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased'))
    df['Sentiment'] = list(LABELS[model(t)[0].get('label')] for t in tweets)
    df['Score'] = list(model(t_)[0].get('score') for t_ in tweets)

    print("Done ... sentiment-analysis")
    print(df)
    return render_template("covid.html", data=list(df.values.tolist()))   

if __name__ == "__main__":
    app.run(debug=True)

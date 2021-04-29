from flask import Flask, render_template, request
app = Flask(__name__)


import pandas as pd
# from transformers import pipeline
from transformers import pipeline, DistilBertForSequenceClassification, DistilBertTokenizerFast
import tweepy

LABELS = {'LABEL_0': 'NEGATIVE', 'LABEL_1': 'POSITIVE'}

# # for tweet in tweets:
# #     print(tweet)
# df = pd.DataFrame(data=tweets, columns=['Tweet'])
# # df.head(5)
# # print("df=" + df)
# # Iterate over `tweets` and pass each item to `model()` to obtain
# # prediction, then write those predictions to a Pandas dataframe
# model = pipeline('sentiment-analysis')
# df['Sentiment'] = list(model(t)[0].get('label') for t in tweets)
# df['Score'] = list(model(t_)[0].get('score') for t_ in tweets)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

#background process happening without any refreshing
@app.route('/getTweets')
def getTweets():
    print("Getting tweets now...")
    # keyword = requests.get('keyword', args)
    #default keyword if you hit search. 
    keyword = request.args.get('keyword', default='coronavirus covid vaccine vaccination COVID-19')
    print("keyword= " + keyword)
    #our entry to tweets
    api_key = "WD9TVjUQFAf5m6XuWMJd7vErs" # API Key
    api_secret =  "OtKCZvwqqBDiBMqdgip2BCE4Z9N6JpK6yg6ylNDYYxMhun29mn" # API Secret Key
    api_access_token = "1384529505696559104-Cxr6keJipox3TCJbBVsIz91poKkyPT" # Access Token
    api_access_token_secret = "aIDnNeJBKgupUnUBl8V3Sz0DWWCCpAM9cNFtg8LBRlgga" # Access Token Secret

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(api_access_token, api_access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    query = keyword # "coronavirus covid vaccine vaccination COVID-19" # text from the search box
    tweets_ = tweepy.Cursor(api.search, query, result_type='recent').items(10)
    tweets = [tweet.text for tweet in tweets_]    

    print("Done..retrieving tweets from API based on the keyword=" + keyword)
    # auth = tweepy.OAuthHandler(api_key, api_secret)
    # auth.set_access_token(api_access_token, api_access_token_secret)
    # api = tweepy.API(auth, wait_on_rate_limit=True)
    # query = "coronavirus covid vaccine vaccination COVID-19" # text from the search box
    # tweets_ = tweepy.Cursor(api.search, query, result_type='recent').items(50)
    # tweets = [tweet.text for tweet in tweets_]

    # for tweet in tweets:
    #     print(tweet)
    df = pd.DataFrame(data=tweets, columns=['Tweet'])
    
    print("Done..creating dataframe")
    # print(df)
    # df.head(5)
    # print("df=" + df)
    # Iterate over `tweets` and pass each item to `model()` to obtain
    # prediction, then write those predictions to a Pandas dataframe
    model = pipeline('sentiment-analysis',
            model=DistilBertForSequenceClassification.from_pretrained("checkpoint-9500"),
            tokenizer=DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased'))
    # model = pipeline('sentiment-analysis')
    df['Sentiment'] = list(LABELS[model(t)[0].get('label')] for t in tweets)
    df['Score'] = list(model(t_)[0].get('score') for t_ in tweets)
    # df['Sentiment'] = list(model(t)[0].get('label') for t in tweets)
    # df['Score'] = list(model(t_)[0].get('score') for t_ in tweets)
    print("Done..sentiment-analysis")
    print(df)
    return render_template("covid.html", data=list(df.values.tolist()))   

if __name__ == "__main__":
    app.run(debug=True)
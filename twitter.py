import tweepy
import pandas as pd

def get_twitter_text(s):
    
    #enter your api keys here 
    # you will be getting these keys from twitter api
    api_key = ''
    api_key_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    keywords = '#'+s+'-filter:retweets'
    tweets=tweepy.Cursor(api.search_tweets,q=keywords,lang="en",tweet_mode="extended").items(1000)
    columns = ['Tweet']
    data = []
    for tweet in tweets:
        data.append([ tweet.full_text])
    df = pd.DataFrame(data, columns=columns)
    #print(df)
    return df

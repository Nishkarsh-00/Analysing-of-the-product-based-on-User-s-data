import tweepy
import pandas as pd

def get_twitter_text(s):

    api_key = 'V4lpiPa5bFuegeZ48n3Cao1zq'
    api_key_secret = 'ksJwRF0QoJCsFslzgU4zN0utFBrwZu7VaxiFkraGty8t73LJFC'
    access_token = '1540721724295356416-2QrTq7j8r4R6qSw6oi2bXuScc4RFgn'
    access_token_secret = 'qoz4UWuerhr302QWnCXp9oM7GhPfo8GoVHNTJeA6zaNfn'

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

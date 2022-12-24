from textblob import TextBlob
import numpy as np # linear algebra
import pandas as pd # data processing

def my_sentiment_analyser(df):
    count=df.shape[0]
    localrate=0
    # print("total ",count)
    for s in df['Tweet']:
        res = TextBlob(s)
        localrate+=res.sentiment.polarity

    ans=localrate/count
    globalrate=0
    if(ans<-0.6):
        globalrate=1
    elif(ans<0.2):
        globalrate=2
    elif(ans==0.2):
        globalrate=3
    elif(ans<0.6):
        globalrate=4
    else:
        globalrate=5
    return globalrate
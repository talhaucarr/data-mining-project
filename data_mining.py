import tweepy,pymongo,time

def hashtag_df(tweet):
    tweet = tweet.lower()

    tweet = tweet.replace('[^\w\s]', '')#Noktalama işaretlerinin silinmesi

    tweet = tweet.replace('\d', '')

    return tweet

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['VMadenciligi']
mycol = mydb["Tweetler"]

consumer_key = "nOOQvT8V4GBTnFe0JaFrGNVYx"
consumer_secret = "9y668xgL0iqwjgXmYfZoCINbTPzvlkgsub5CSh6tSS12VBUa0k"
access_token = "632956433-EZEY0TkwvaAf3fVjuoqwwu3jnKNLzaqXnpYl4Wzk"
access_token_secret = "UL6BRREmHOdclAX5qiiyx34ddIzjo0zzg7uzokQDxe8D5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


try:
    tweetler = tweepy.Cursor(api.search, q="#pazartesi", lang="tr", result_type="recent").items(10)


    for i in tweetler:

        df = hashtag_df(i.text)


        mydict = {"tweet": df}
        x = mycol.insert_one(mydict)

    print("End.")

except tweepy.TweepError:
    time.sleep(120)

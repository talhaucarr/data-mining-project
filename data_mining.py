import tweepy, pymongo, time
import threading


def hashtag_df(tweet):
    tweet = tweet.lower()

    tweet = tweet.replace('[^\w\s]', '')  # Noktalama işaretlerinin silinmesi

    tweet = tweet.replace('\d', '')

    return tweet


def my_func(c_key, c_secret, a_token, a_token_scret):
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['test']
    mycol = mydb["sa"]

    consumer_key = c_key
    consumer_secret = c_secret
    access_token = a_token
    access_token_secret = a_token_scret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        tweetler = tweepy.Cursor(api.search, q="#pazartesi", lang="tr", result_type="recent").items(50)
        print("Thread calısıyor.")
        for i in tweetler:
            df = hashtag_df(i.text)

            mydict = {"created_at": i.created_at, "status_id": i.id, "status_id_str": i.id_str, "source": i.source,
                      "screen_name": i.user.screen_name,
                      "source_url": i.source_url,
                      "user_id": i.in_reply_to_user_id, "tweet": df, "created_at": i.created_at,
                      "location": i.author.location, "lang": i.lang}
            mycol.insert_one(mydict)

        print("End.")

    except tweepy.TweepError:
        time.sleep(120)


t1 = threading.Thread(target=my_func,
                      args=("nOOQvT8V4GBTnFe0JaFrGNVYx", "9y668xgL0iqwjgXmYfZoCINbTPzvlkgsub5CSh6tSS12VBUa0k",
                            "632956433-EZEY0TkwvaAf3fVjuoqwwu3jnKNLzaqXnpYl4Wzk",
                            "UL6BRREmHOdclAX5qiiyx34ddIzjo0zzg7uzokQDxe8D5"))

t2 = threading.Thread(target=my_func,
                      args=("kHlx5H8uNgSWCVWd4D6YMq7wn", "XDFjowzqfbXWpukKi7fTLgfSqJQecFmI1pzLdLv8y5FkHuEcRk",
                            "632956433-P6qn9lFALYb8YhudMXfJLnjazrnWvINcYzSr4gN1",
                            "9oW0Wyb9pZpfajSF4aj9d0L49NtnIbUBxNWeZUrruQ4dM"))

t3 = threading.Thread(target=my_func,
                      args=("PLwxwR8p0hvsLwiK6SwG2neFt", "8izKtsLzIZN5eoDENyEdbTXFkgCiLLYWCxeahTxqDx36U6YQcg",
                            "632956433-Aa7YBShgrxI4TyC7WeXv8tUShmFkIGXODrTlylH8",
                            "0IhC7pF5urNBwCEmf9dJzA492fM4nlXUtA5WeFtUkOtUy"))


t1.start()
t2.start()
t3.start()
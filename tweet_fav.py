import tweepy
import json
import time
import os
import random


auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])
#apiインスタンスを作成
api = tweepy.API(auth)

#調べる単語
keyword = random.choice(['米谷奈々未','佐藤詩織'])
params = {"q": keyword,'count':5}

search_results = api.search(q=params['q'],count=params['count'])

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id
    user = result.user.name
    tweet = result.text
    time = result.created_at
    print(tweet)
    #リツイートとリプには反応しない
    if 'RT' not in tweet and '@' not in tweet:
        try:
            api.create_favorite(user_id)
            print(user+'をいいねしたんご')
        except:
            print('いいね済みやで')

    print('-'*100)

# coding: utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime
import time


member = random.choice(['07','13'])
markov_dict_file = './dictionary/markov_dic_'+member+'.json'
markov_dic = json.load(open(markov_dict_file,'r'))

#文章生成
def make_sentence(dic,member):
    ret = []
    if not 'top' in dic: return 'no dic'
    top = dic['top']
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    while w1 == '。' or w2 == '。':
        w1 = word_choice(top)
        w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        #メンバーに合わせて最後の一行を変える
        if w3 == '。':
            if member=='13':
                ret.append('\n⊿長沢菜々香')
                break
            elif member=='07':
                ret.append('\nsee you again ⊿⊿')
                break
        w1,w2 = w2,w3
    return ''.join(ret)

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys)) #辞書のキーを選ぶ




#文章生成
def sentence():
    while True:
        s = make_sentence(markov_dic,member)
        if len(s) < 140:
            break
    return s


# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

#ツイート内容
tweet = sentence()

# ツイート本文
params = {"status": tweet}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)

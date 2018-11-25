import requests
import pandas as pd
import tweepy
import os
from bs4 import BeautifulSoup



def getTweets(search_terms=['counterfeit','amazonHelp']):
	consumer_key = '6CM1Yqk0Qz6KUXsDQUS8xmahS'
	consumer_secret = 'LMSBfoJWMTlder205Ihr2t1JDgwJD2XgKQeWYau25gJix4lm24'
	access_token = '753302551840198656-Qx1HSVIZlqjShSsUeWY4BhRaVEbWVAP'
	access_token_secret = 'iwtFUe30YrmDlMyGACLLNYrpZQutuW2e8QzX03YwOlz97'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)


	cfit_tweets = api.search(q=search_terms, count=1000)

	df = pd.DataFrame()
	df['text'] = [x.text for x in cfit_tweets]
	df['source'] = ['twitter: "counterfiet, amazonelp"' for x in cfit_tweets]
	df['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in cfit_tweets]
	df['retweets'] = [x.retweet_count for x in cfit_tweets]
	df['favorites'] = [x.favorite_count for x in cfit_tweets]
	df['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in cfit_tweets]

	keys = ['t1', 't2']
	keys = ['t'+str(x) for x in range(len(df['iframe'].tolist()))]
	values = df['iframe'].tolist()
	return dict(zip(keys, values))


def getTweetsDF():
	consumer_key = '6CM1Yqk0Qz6KUXsDQUS8xmahS'
	consumer_secret = 'LMSBfoJWMTlder205Ihr2t1JDgwJD2XgKQeWYau25gJix4lm24'
	access_token = '753302551840198656-Qx1HSVIZlqjShSsUeWY4BhRaVEbWVAP'
	access_token_secret = 'iwtFUe30YrmDlMyGACLLNYrpZQutuW2e8QzX03YwOlz97'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)


	cfit_tweets = api.search(q=['counterfeit','amazonHelp'], count=1000)
	fake_tweets = api.search(q=['fake','amazonHelp'], count=1000)

	df = pd.DataFrame()
	df['text'] = [x.text for x in cfit_tweets]
	df['source'] = ['twitter: "counterfiet, amazonelp"' for x in cfit_tweets]
	df['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in cfit_tweets]
	df['retweets'] = [x.retweet_count for x in cfit_tweets]
	df['favorites'] = [x.favorite_count for x in cfit_tweets]
	df['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in cfit_tweets]

	df1 = pd.DataFrame()
	df1['text'] = [x.text for x in fake_tweets]
	df1['source'] = ['twitter: "fake, amazonHelp"' for x in fake_tweets]
	df1['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in fake_tweets]
	df1['retweets'] = [x.retweet_count for x in fake_tweets]
	df1['favorites'] = [x.favorite_count for x in fake_tweets]
	df1['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in fake_tweets]


	df_final = df.append(df1)
	df_final.sort_values('retweets',ascending=False).drop_duplicates(['text','source']).reset_index().head(50)

	keys = ['t1', 't2']
	keys = ['t'+str(x) for x in range(len(df1['iframe'].tolist()))]
	values = df1['iframe'].tolist()
	return dict(zip(keys, values))



from helper import getTweets, getReddits
import requests

def test_tweest():
	twit_url_dict = getTweets(search_terms=['amazonHelp', 'counterfeit'])
	for key, value in twit_url_dict.items():
		print(requests.get(value).content)
		assert requests.get(value).status_code == 200





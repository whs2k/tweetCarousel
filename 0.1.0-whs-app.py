from flask import Flask, redirect, render_template
import os
from helper import getTweets, getReddits

app = Flask(__name__)

def goToInsta(hashtag='fakeamazon'):
	return redirect("https://www.instagram.com/explore/tags/fakeamazon/?hl=en",
		code=302)

#https://twitter.com/rufnknme/status/1066006390680866816
@app.route('/')
def carousel():
	twit_url_dict = getTweets(search_terms=['amazonHelp', 'counterfeit']) #keys = [t1,t2,t3....]s
	red_url_dict = getReddits() #keys = r1. r2 ...
	return render_template('carousel.html', **twit_url_dict, **red_url_dict)
def goToInsta(hashtag='fakeamazon'):
	return redirect("https://www.instagram.com/explore/tags/fakeamazon/?hl=en",
		code=302)


if __name__ == '__main__':
	#port = int(os.environ.get('PORT', 5000))
    app.run() #host='0.0.0.0', port=9999
from flask import Flask, redirect, render_template
import os
from helper import getTweets

app = Flask(__name__)

def goToInsta(hashtag='fakeamazon'):
	return redirect("https://www.instagram.com/explore/tags/fakeamazon/?hl=en",
		code=302)

#https://twitter.com/rufnknme/status/1066006390680866816
@app.route('/')
def carousel():
	url_dict = getTweets(search_terms=['amazon', 'counterfeit', 'fake']) #keys = [t1,t2,t3....]s
	return render_template('carousel.html', **url_dict)
def goToInsta(hashtag='fakeamazon'):
	return redirect("https://www.instagram.com/explore/tags/fakeamazon/?hl=en",
		code=302)


if __name__ == '__main__':
	#port = int(os.environ.get('PORT', 5000))
    app.run() #host='0.0.0.0', port=9999
import tweepy
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
consumer_key = os.getenv('APIKEY')
consumer_secret = os.getenv('APISECRET')
access_token = os.getenv('ACCESSTOKEN')
access_token_secret = os.getenv('ACCESSTOKENSECRET')

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)


def get_twitter_data(id):
    df = pd.DataFrame()
    media = []
    favorite_count = []
    retweets = []
    created_at = []
    for page in tweepy.Cursor(api.user_timeline, screen_name=id,count=200).pages():
        for statuses in page:
            if 'media' in statuses.entities:
                for image in  statuses.entities['media']:
                    media.append(image['media_url'])
                    favorite_count.append(statuses.favorite_count)
                    retweets.append(statuses.retweet_count)
                    created_at.append(statuses.created_at)

    df['created_date'] = created_at
    df['media'] = media
    df['favorite_count'] = favorite_count
    df['retweets'] = retweets
    return df





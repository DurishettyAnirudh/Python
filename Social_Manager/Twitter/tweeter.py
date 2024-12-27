
import tweepy
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    bearer_token 
)

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


client.create_tweet(text = "Hello World! I am a bot under testing.")

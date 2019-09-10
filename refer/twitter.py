# https://dev.twitter.com/apps/new
# http://docs.tweepy.org/en/latest/api.html?#API.update_status

# https://realpython.com/twitter-bot-python-tweepy/

import tweepy
from termcolor import colored

from settings import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) # API in the tweepy documenation

# api.update_status("Hello, automation and should include file later")
api.update_with_media("static/images/automate.png", "Hello, automation and should include file later @rustlang")

# https://twitter.com/steadylearner_p?lang=en
# user = api.get_user('steadylearner_p')

user = api.me()
user_name = user.name

num_of_followers = user.followers_count
colored_num_of_followers = colored(num_of_followers, "blue", attrs=['bold'])

steadylearner = "Steadylearner"
colored_steadylearner = colored(steadylearner, "yellow", attrs=['bold'])

print(f"You({user.name}) have {colored_num_of_followers} followers in Twitter.")

response = input(f"Do you wnat the latest contents from {colored_steadylearner}?([y]/n)\n")

if response.startswith("n"):
    print("Ends the Tweepy api test")
else:
    # docs.tweepy.org/en/latest/api.html?#API.create_friendship
    api.create_friendship("@steadylearner_p")
    print("You start to follow Steadylearner at Twitter. You can visit www.steadylearner.com also.")

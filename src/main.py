# Start for program, will maybe consider an MVC framework later if needed

# Python imports
import os
from dotenv import load_dotenv

# Repo imports
from data.fetch_data.Twitter_API import Twitter_API

load_dotenv()

token = 'Bearer ' + os.getenv('APP_ONLY_BEARER_TOKEN')

Twitter = Twitter_API(token)

username_response = Twitter.search_usernames('BotEngagement')
tweet_id_response = Twitter.search_tweets(1588905886051102721)

print(username_response)
print(tweet_id_response)

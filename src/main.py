# Start for program, will maybe consider an MVC framework later if needed.

# Python imports
import os
from dotenv import load_dotenv

# Repo imports
from data.fetch_data.twitter_api import TwitterAPI
from data.process_data.twitter_db_adapter import TwitterDBAdapter
from data.process_data.twitter_interpreter import TwitterInterpreter

load_dotenv()

token = 'Bearer ' + os.getenv('APP_ONLY_BEARER_TOKEN')

Twitter = TwitterAPI(token)
TwitterDatabase = TwitterDBAdapter()
TwitterIntrepret = TwitterInterpreter()

recent_tweets_response = Twitter.search_recent_tweets_with_query('elon -is:retweet -is:reply -is:quote')

validated_tweets = TwitterIntrepret.filtered_tweets_by_validation(recent_tweets_response)

TwitterIntrepret.print_tweets(validated_tweets)

print('End')

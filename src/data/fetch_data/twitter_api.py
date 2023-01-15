# Twitter API Wrapper, to handle all interactions to Twitter API.

# Python imports
from datetime import datetime, timezone, timedelta

# Repo imports
from data.fetch_data.wrapper_api import WrapperAPI

class TwitterAPI(WrapperAPI):
  TWEETS_LOOKUP = '/2/tweets'
  USERS_LOOKUP = '/2/users'
  TWEET_OBJECT_FIELDS = 'author_id,context_annotations,conversation_id,lang,in_reply_to_user_id,public_metrics,referenced_tweets'
  USER_OBJECT_FIELDS = 'verified,public_metrics,protected'
  EXPANSIONS_FIELDS = 'author_id'

  def __init__(self, bearer_token):
    super().__init__('https://api.twitter.com', bearer_token)

  # 
  # Search based on username: https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start/user-lookup
  # 
  # Return: Response Object
  def search_usernames(self, usernames):
    path = f"{self.USERS_LOOKUP}/by?usernames={usernames}"
    return self.search(path)

  # 
  # Search based on tweet ids: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/quick-start
  # 
  # Return: Response Object
  def read_tweets_by_ids(self, tweet_ids):
    path = f"{self.TWEETS_LOOKUP}?ids={tweet_ids}&tweet.fields={self.TWEET_OBJECT_FIELDS}"
    return self.search(path)

  # 
  # Search by query: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/quick-start
  # 
  # Return: Response Object
  # Exception: if call throws a ValueError from http call
  def search_recent_tweets_with_query(self, query):
    query_param = f"query={query}"
    tweet_fields_param = f"tweet.fields={self.TWEET_OBJECT_FIELDS}"
    user_fields_param = f"user.fields={self.USER_OBJECT_FIELDS}"
    expansion_param = f"expansions={self.EXPANSIONS_FIELDS}"
    max_results_param = 'max_results=100'
    end_time = "end_time=" + self.six_days_ago_end_time_calculation()

    path = f"{self.TWEETS_LOOKUP}/search/recent?{query_param}&{tweet_fields_param}&{user_fields_param}&{expansion_param}&{max_results_param}&{end_time}"
    try:
      return self.search(path)
    except ValueError as err:
      print(err.args)
      return None

  #  
  # Return 6 days ago end time in RFC339 standard
  # 
  # Return: String
  def six_days_ago_end_time_calculation(self):
    time_now_minus_6_days = datetime.now(timezone.utc) - timedelta(days=6)
    return time_now_minus_6_days.strftime("%Y-%m-%dT%H:%M:%S.000Z")

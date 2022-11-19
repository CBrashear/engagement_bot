# Twitter API Wrapper, to handle all interactions to Twitter API.

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
  def search_tweets_by_ids(self, tweet_ids):
    path = f"{self.TWEETS_LOOKUP}?ids={tweet_ids}&tweet.fields={self.TWEET_OBJECT_FIELDS}"
    return self.search(path)

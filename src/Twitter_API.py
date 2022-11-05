# Twitter API Wrapper, to handle all interactions to Twitter API 

from API_Wrapper import API_Wrapper

class Twitter_API(API_Wrapper):
  def __init__(self, bearer_token):
    super().__init__('https://api.twitter.com', bearer_token)

  # 
  # Search based on username: https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start/user-lookup
  # 
  def search_username(self, username):
    path = '/2/users/by/username/' + username

    self.search(path)

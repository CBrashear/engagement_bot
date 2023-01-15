""" 
  Interpret responses from Twitter API.
  Used to validate conditions we want to impose on data extraction before we submit as input.
  Conditions:
    1. Has to be English.
    2. Has to be the Root Tweet, not a reply. As for editted tweets, it has to be the latest one.
    3. Has to be a somewhat popular user.
      i: user > 10k followers

  Conditions left out for now:
    - Has to be a somewhat popular tweet. i: replies > 100, likes > 250
    - Has to be a plain tweet, no links, or hashtags.
"""

import json

class TwitterInterpreter:
  def filtered_tweets_by_validation(self, api_tweet_return):
    tweet_return = json.loads(api_tweet_return)
    filtered_tweets_data = []

    for tweet in tweet_return['data']:
      if self.validate_tweet_entity(tweet, tweet_return['includes']) == True:
        filtered_tweets_data.append(tweet)

    return filtered_tweets_data
  
  # Assume data content is passed
  def print_tweets(self, tweets):
    for tweet in tweets:
      clean_text_for_one_line = tweet['text'].replace('\n',"")
      print(f"Tweet id: {tweet['id']}\tAuthor id: {tweet['author_id']}\tText: {clean_text_for_one_line}")
  
  def validate_tweet_entity(self, entry, includes):
    if self.is_english(entry['lang']) == False: return False
    if self.is_root_tweet(entry['id'], entry['conversation_id'], entry['edit_history_tweet_ids']) == False: return False
    if self.is_user_popular(entry['author_id'], includes) == False: return False

    return True
  
  def is_english(self, lang):
    return True if lang == 'en' else False
  
  def is_root_tweet(self, tweet_id, conversation_id, edit_history_tweet_ids):
    if tweet_id == conversation_id and tweet_id == edit_history_tweet_ids[-1]:
      return True
    else:
      return False
  
  def is_tweet_popular(self, replies, likes):
    return True if replies > 100 and likes > 250 else False

  def is_user_popular(self, author_id, includes):
    users = includes['users']

    for user in users:
      if user['id'] == author_id:
        if user['public_metrics']['followers_count'] > 10000:
          return True
        else:
          return False

  def is_tweet_plain(self, tweet):
    if self.contains_link(tweet) == False: return False
    if self.contains_hashtag(tweet) == False: return False
    return tweet

  def contains_link(tweet):
    return False

  def contains_hashtag(tweet):
    return False

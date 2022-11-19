""" 
  Interpret responses from Twitter API.
  Used to validate conditions we want to impose on data extraction before we submit as input.
  Conditions:
    1. Has to be English.
    2. Has to be the Root Tweet, not a reply. As for editted tweets, it has to be the latest one.
    3. Has to be a somewhat popular tweet.
      i: replies > 100, likes > 250
    4. Has to be a somewhat popular user.
      i: user > 10k followers
    5. Has to be a plain tweet, no links, or hashtags.
"""

import json

class TwitterInterpreter:
  tweet_return = '{ "data": [ { "author_id": "16806754", "lang": "en", "context_annotations": [ { "domain": { "id": "3", "name": "TV Shows", "description": "Television shows from around the world" }, "entity": { "id": "10000612773", "name": "NFL Football", "description": "Replays of classic NFL games." } }, { "domain": { "id": "6", "name": "Sports Event" }, "entity": { "id": "1524906805368827905", "name": "Steelers at Eagles" } }, { "domain": { "id": "11", "name": "Sport", "description": "Types of sports, like soccer and basketball" }, "entity": { "id": "689566306014617600", "name": "American football" } }, { "domain": { "id": "12", "name": "Sports Team", "description": "A sports team organization, like Arsenal and the Boston Celtics" }, "entity": { "id": "689566306027188224", "name": "Pittsburgh Steelers" } }, { "domain": { "id": "26", "name": "Sports League", "description": "" }, "entity": { "id": "689566314835259392", "name": "NFL" } }, { "domain": { "id": "27", "name": "American Football Game", "description": "Sports Event specific to American Football, such as Notre Dame vs. Stanford" }, "entity": { "id": "1524906805368827905", "name": "Steelers at Eagles" } }, { "domain": { "id": "28", "name": "NFL Football Game", "description": "Sports Event specific to NFL Football, such as Buffalo Bills vs. New England Patriots" }, "entity": { "id": "1524906805368827905", "name": "Steelers at Eagles" } }, { "domain": { "id": "29", "name": "Events [Entity Service]", "description": "Real world events. " }, "entity": { "id": "1524906805368827905", "name": "Steelers at Eagles" } }, { "domain": { "id": "46", "name": "Business Taxonomy", "description": "Categories within Brand Verticals that narrow down the scope of Brands" }, "entity": { "id": "1557697289971322880", "name": "Sports & Fitness Business", "description": "Brands, companies, advertisers and every non-person handle with the profit intent related to sports nutrition, athletic apparel, sports apps, fitness venues" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566306014617600", "name": "American football" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566306027188224", "name": "Pittsburgh Steelers" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566314835259392", "name": "NFL" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "847900493514891265", "name": "Sports", "description": "Sports" } } ], "edit_history_tweet_ids": [ "1586866222888407041" ], "id": "1586866222888407041", "public_metrics": { "retweet_count": 21, "reply_count": 792, "like_count": 446, "quote_count": 79 }, "conversation_id": "1586866222888407041", "text": "How many of these final nine games will the #Steelers win? https://t.co/tQvVNpy7H4" }, { "author_id": "16806754", "lang": "en", "context_annotations": [ { "domain": { "id": "3", "name": "TV Shows", "description": "Television shows from around the world" }, "entity": { "id": "10000612773", "name": "NFL Football", "description": "Replays of classic NFL games." } }, { "domain": { "id": "3", "name": "TV Shows", "description": "Television shows from around the world" }, "entity": { "id": "10032425201", "name": "NFL Football" } }, { "domain": { "id": "10", "name": "Person", "description": "Named people in the world like Nelson Mandela" }, "entity": { "id": "1253866060207415296", "name": "Chase Claypool" } }, { "domain": { "id": "11", "name": "Sport", "description": "Types of sports, like soccer and basketball" }, "entity": { "id": "689566306014617600", "name": "American football" } }, { "domain": { "id": "12", "name": "Sports Team", "description": "A sports team organization, like Arsenal and the Boston Celtics" }, "entity": { "id": "689566302801768449", "name": "Chicago Bears" } }, { "domain": { "id": "12", "name": "Sports Team", "description": "A sports team organization, like Arsenal and the Boston Celtics" }, "entity": { "id": "689566306027188224", "name": "Pittsburgh Steelers" } }, { "domain": { "id": "26", "name": "Sports League", "description": "" }, "entity": { "id": "689566314835259392", "name": "NFL" } }, { "domain": { "id": "46", "name": "Business Taxonomy", "description": "Categories within Brand Verticals that narrow down the scope of Brands" }, "entity": { "id": "1557697289971322880", "name": "Sports & Fitness Business", "description": "Brands, companies, advertisers and every non-person handle with the profit intent related to sports nutrition, athletic apparel, sports apps, fitness venues" } }, { "domain": { "id": "60", "name": "Athlete", "description": "An athlete in the world, like Serena Williams or Lionel Messi" }, "entity": { "id": "1253866060207415296", "name": "Chase Claypool" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566302801768449", "name": "Chicago Bears" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566306014617600", "name": "American football" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566306027188224", "name": "Pittsburgh Steelers" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "689566314835259392", "name": "NFL" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "847900493514891265", "name": "Sports", "description": "Sports" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "1253866060207415296", "name": "Chase Claypool" } }, { "domain": { "id": "131", "name": "Unified Twitter Taxonomy", "description": "A taxonomy of user interests. " }, "entity": { "id": "1263187885970227200", "name": "NFL players" } } ], "edit_history_tweet_ids": [ "1588905886051102721" ], "id": "1588905886051102721", "public_metrics": { "retweet_count": 0, "reply_count": 0, "like_count": 2, "quote_count": 0 }, "conversation_id": "1588905886051102721", "text": "Chase Claypool Already Turning Heads At Bears Practices #Steelers #NFL https://t.co/hEs5EokM6T" }, { "author_id": "2615749790", "lang": "en", "edit_history_tweet_ids": [ "1588564617907044353" ], "referenced_tweets": [ { "type": "replied_to", "id": "1586866222888407041" } ], "in_reply_to_user_id": "16806754", "id": "1588564617907044353", "public_metrics": { "retweet_count": 0, "reply_count": 0, "like_count": 0, "quote_count": 0 }, "conversation_id": "1586866222888407041", "text": "@Steelersdepot Unfortunately, they\'ll win just enough games to finish in the middle of the pack in regard to the draft. They need a top five draft pick position next year along with having hopefully a decently high second round Bears pick they got." } ], "includes": { "users": [ { "public_metrics": { "followers_count": 115581, "following_count": 2150, "tweet_count": 641916, "listed_count": 1377 }, "name": "Steelers Depot 7⃣🦃", "id": "16806754", "protected": false, "username": "Steelersdepot", "verified": false }, { "public_metrics": { "followers_count": 15, "following_count": 129, "tweet_count": 635, "listed_count": 5 }, "name": "AhhtaStateYinzer", "id": "2615749790", "protected": false, "username": "ChippedHam67", "verified": false } ] } }'

  def tweet_lookup_input(self):
    tweet_return = json.loads(self.tweet_return)
    tweet_includes = tweet_return['includes']

    for entry in tweet_return['data']:
      print(self.validate_tweet_entity(entry, tweet_includes))
  
  def validate_tweet_entity(self, entry, includes):
    if self.is_english(entry['lang']) == False: return False
    if self.is_root_tweet(entry['id'], entry['conversation_id'], entry['edit_history_tweet_ids']) == False: return False
    if self.is_tweet_popular(entry['public_metrics']['reply_count'], entry['public_metrics']['like_count']) == False: return False
    if self.is_user_popular(entry['author_id'], includes) == False: return False
    if self.is_tweet_plain(entry['text']) == False: return False

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
      if user['id'] == author_id and user['public_metrics']['followers_count'] > 10000:
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

F = TwitterInterpreter()
F.tweet_lookup_input()

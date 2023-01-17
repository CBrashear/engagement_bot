# Class to handle twitter data to/from DB

import psycopg2

class TwitterDBAdapter:
  def __init__(self):
    db_props = {
      "host": -,
      "dbname": -,
      "user": -,
      "password": -
    }

    self.conn_properties = db_props

  def open_connection(self):
    self.conn = psycopg2.connect(host=self.conn_properties['host'], dbname=self.conn_properties['dbname'], user=self.conn_properties['user'], password=self.conn_properties['password'])
    self.cur = self.conn.cursor()

  def close_connection(self):
    self.cur.close()
    self.conn.close()
  
  def commit_transaction(self):
    self.conn.commit()

  def get_all_tweets(self):
    self.cur.execute('SELECT * FROM tweets')
    return self.cur.fetchall()

  def get_all_users(self):
    self.cur.execute('SELECT * FROM users')
    return self.cur.fetchall()

  def get_all_contexts(self):
    self.cur.execute('SELECT * FROM contexts')
    return self.cur.fetchall()

  def insert_tweet_from_json(self, tweet_json):
    tweet_id = tweet_json['id']
    tweet_text = tweet_json['text']
    tweet_lang = tweet_json['lang']
    tweet_popular = True if tweet_json['public_metrics']['like_count'] > 100 else False
    user_author_id = tweet_json['author_id']

    insert_tweet_tuple = (tweet_id, tweet_text, tweet_lang, tweet_popular, user_author_id)
    self.insert_tweet(insert_tweet_tuple)

  def insert_tweet(self, tweet):
    insert_tweet_sql = "INSERT INTO tweets (tweet_id, tweet_text, lang, is_tweet_popular, user_author_id) VALUES (%s, %s, %s, %s, %s);"
    try:
      self.cur.execute(insert_tweet_sql, tweet)
    except psycopg2.Error as e:
      print(f"ERROR: {e.pgcode}|{e.pgerror}")

  def insert_user(self, user):
    insert_user_sql = "INSERT INTO users (author_id, is_user_popular, protected, verified, handle_name, name) VALUES (%s, %s, %s, %s, %s, %s);"
    self.cur.execute(insert_user_sql, user)

  def insert_context(self, context):
    insert_context_sql = "INSERT INTO contexts (domain_id, domain_name, domain_description) VALUES (%s, %s, %s);"
    self.cur.execute(insert_context_sql, context)
  
  def display_all(self):
    print("Tweets")
    print(self.get_all_tweets())
    print("Users")
    print(self.get_all_users())
    print("Context")
    print(self.get_all_contexts())

# tweet_to_insert = (1, 'tweet tweet tweet', 'ENG', True, 1, 1)
# user_to_insert = (3, True, True, True, "testhandle", "testname")
# context_to_insert = (1, 'domain name 1', 'description')

# TwitterDB = TwitterDBAdapter(db_props)
# TwitterDB.open_connection()

# TwitterDB.insert_tweet(tweet_to_insert)
# TwitterDB.insert_user(user_to_insert)
# TwitterDB.insert_context(context_to_insert)
# TwitterDB.commit_transaction()

# TwitterDB.display_all()

# TwitterDB.close_connection()

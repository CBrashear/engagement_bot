# Start for program, will maybe consider an MVC framework later if needed

import os
from Twitter_API import Twitter_API
from dotenv import load_dotenv

load_dotenv()

token = 'Bearer ' + os.getenv('APP_ONLY_BEARER_TOKEN')

Twitter = Twitter_API(token)
Twitter.search_username('BotEngagement')

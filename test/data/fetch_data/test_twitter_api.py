from data.fetch_data.twitter_api import TwitterAPI

class TestTwitterAPI:
  base_url_twitter_api = 'https://api.twitter.com'
  mock_bearer_token = 'mocktoken'
  mock_twitter_wrapper = TwitterAPI(mock_bearer_token)

  def test_init(self):
    assert self.mock_twitter_wrapper.api_base_url == self.base_url_twitter_api
    assert self.mock_twitter_wrapper.bearer_token == self.mock_bearer_token

  def test_search_usernames(self, mocker):
    mock_usernames = 'user1,user2'
    path = f"{self.mock_twitter_wrapper.USERS_LOOKUP}/by?usernames={mock_usernames}"

    search_usernames = mocker.patch('data.fetch_data.twitter_api.TwitterAPI.search', return_value=MockResponse.text)

    assert self.mock_twitter_wrapper.search_usernames(mock_usernames) == '{"fake_data":1}'
    search_usernames.assert_called_once_with(path)

  def test_search_tweets_by_ids(self, mocker):
    mock_tweet_ids = '123,321'
    path = f"{self.mock_twitter_wrapper.TWEETS_LOOKUP}?ids={mock_tweet_ids}&tweet.fields={self.mock_twitter_wrapper.TWEET_OBJECT_FIELDS}"

    search_usernames = mocker.patch('data.fetch_data.twitter_api.TwitterAPI.search', return_value=MockResponse.text)

    assert self.mock_twitter_wrapper.search_tweets_by_ids(mock_tweet_ids) == '{"fake_data":1}'
    search_usernames.assert_called_once_with(path)

class MockResponse:
  text = '{"fake_data":1}'

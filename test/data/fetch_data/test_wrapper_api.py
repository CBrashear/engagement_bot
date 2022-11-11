# Python imports
import requests as req

# Repo imports
from data.fetch_data.wrapper_api import WrapperAPI

class TestWrapperAPI:
  mock_base_uri = 'mock.com'
  mock_bearer_token = 'mocktoken'
  mock_wrapper = WrapperAPI(mock_base_uri, mock_bearer_token)

  def test_init(self):
    assert self.mock_wrapper.api_base_url == self.mock_base_uri
    assert self.mock_wrapper.bearer_token == self.mock_bearer_token

  def test_set_bearer_token(self):
    self.mock_bearer_token = 'newtoken'
    self.mock_wrapper.set_bearer_token(self.mock_bearer_token)

    assert self.mock_wrapper.bearer_token == self.mock_bearer_token

  def test_search(self, monkeypatch):
    def mock_request(*args, **kwargs):
      return MockResponse()

    monkeypatch.setattr(req, "request", mock_request)

    result = self.mock_wrapper.search('/fakePath')
    assert result == '{"fake_data":1}'

class MockResponse:
  text = '{"fake_data":1}'

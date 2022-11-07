# Base Wrapper class for API's

import requests as req

class API_Wrapper:
  def __init__(self, api_base_url, bearer_token):
    self.api_base_url = api_base_url
    self.bearer_token = bearer_token

  # 
  # Set instance variable of bearer token to the input parameter
  #
  # @param: bearer_token - string
  def set_bearer_token(self, bearer_token):
    self.bearer_token = bearer_token

  # 
  # Search a relative path from the registered base url.
  # 
  # @param: path - string
  # 
  # Return: Response object
  def search(self, path):
    url = self.api_base_url + path
    headers = {
      'Authorization': self.bearer_token
    }

    return req.request('GET', url, headers=headers)

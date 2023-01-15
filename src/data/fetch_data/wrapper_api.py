# Base Wrapper class for API's.

import requests as req

class WrapperAPI:
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
  # Return: text response
  def search(self, path):
    url = self.api_base_url + path
    headers = {
      'Authorization': self.bearer_token
    }

    response_object = req.request('GET', url, headers=headers, timeout=5)

    if response_object.status_code != 200: raise ValueError('HTTP Error', response_object.status_code, response_object.text)
    return response_object.text

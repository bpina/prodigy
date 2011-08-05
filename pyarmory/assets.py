import urllib
import simplejson as json
from settings import ARMORY_BASE_URL
from tools import fetch_asset, asset_path


class Character:
  name = ''
  realm = ''
  data = {}

  def __init__(self, realm, character):
    self.realm = realm
    self.character = character

  def load(self, *args):
    fields = ''
    
    if args:
      fields = ','.join(args)
  
    self.data = fetch_asset(asset_path('character', self.realm, self.character), fields)
    return self.data



from connections import mongodb
from pyarmory import assets
from datetime import datetime, timedelta

class DocumentWrapper:
  def __init__(self, data):
    for k,v in data.iteritems():
      if isinstance(v, dict):
        v = DocumentWrapper(v)
      self.__dict__[k] = v

def get_character_info(realm, name):
  document = mongodb.characters.find_one({'name': name, 'realm': realm})
  if document:
    return DocumentWrapper(document)
  else:
    asset = assets.Character(realm, name)
    return DocumentWrapper(set_character_info(asset.load('guild', 'progression')))

def set_character_info(data):
  data['last_updated'] = datetime.now()
  mongodb.characters.insert(data)
  return data

def get_appropriate_raids(character):
  relevant_raids = ['Firelands','The Bastion of Twilight', 'Blackwing Descent']
  raids = []
  for raid in character.progression.raids:
    if raid['name'] in relevant_raids:
      raids.append(raid)
  return raids

  

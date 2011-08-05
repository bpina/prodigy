import urllib
import simplejson as json
import settings

def fetch_asset(asset_path, fields):
  path = asset_path
  
  if fields:
    path += '?fields=' + fields

  print path
  f = urllib.urlopen(path)
  contents = f.read()
  asset = json.loads(contents)
  
  return asset

def asset_path(*args):
  path = settings.ARMORY_BASE_URL

  if args:
    path += '/'.join(args)

  return path

'''
Imagehandler:
    * Cache data is stored in a NoSQL database
'''
from unqlite import UnQLite
import datetime
import urllib
import os

class apihandler:

    def __init__(self):
        self.db = UnQLite('cachehandlerdata')
        self.api_cache = self.db.collection('imagecache')
        self.api_cache.create()

    def write_cache(self,image_link):
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        name = self.api_cache.last_record_id() + 1
        extension = image_link.split('.')[-1]
        filename = name + '.' + extension
        image_location = filename
        urllib.urlretrieve(image_link, image_location)
        self.api_cache.store({'image_link':image_link,'location':image_location, 'time':datetime.datetime.now()})
        return image_location

    def read_cache(self, image_link):
        cache_data = self.api_cache.filter(lambda api: api['image_link']==image_link)
        if not cache_data:
            return cache_data
        else :
            return cache_data[0]['location']

    def get_image(self, image_link):
        cache_data = self.read_cache(image_link)
        if not cache_data :
            print ('Downloading image...')
            location = write_cache(image_link)
            return location
        else :
            print ('Getting image from cache...')
            location = cache_data
            return location

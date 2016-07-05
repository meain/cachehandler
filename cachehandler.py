from unqlite import UnQLite
import datetime
import os
import urllib

class apihandler:
    '''
    Apihandler:
        * Cache data is stored in a NoSQL database
        * On incoming api request check for availability in cache for those which can be cached, otherwise jsut make a request and ...
        * Image caching will be done using another class, make calls to that when we get image links
        * The final image returned from the api will be a address of image from eywa server
    '''
    def __init__(self):
        self.db = UnQLite('cachehandlerdata')
        self.api_cache = self.db.collection('apicache')
        self.api_cache.create()

    def write_cache(self, api_function, args, kwargs, data):
        self.api_cache.store({'api_function':str(api_function).split(' ')[2], 'args':str(args), 'kwargs':str(kwargs), 'data':data, 'time':datetime.datetime.now()})

    def read_cache(self, api_function, args, kwargs):
        cache_data = self.api_cache.filter(lambda api: api['api_function']==str(api_function).split(' ')[2] and api['args']==str(args) and api['kwargs']==str(kwargs))
        if not cache_data:
            return cache_data
        else :
            return cache_data[0]['data']

    def api_call(self, api_function, *args, **kwargs):
        cache_data = self.read_cache(api_function, args, kwargs)
        if not cache_data :
            print ('Querying api as no data found in cache...')
            data = api_function(*args, **kwargs)
            self.write_cache(api_function, args, kwargs, data)
            return data
        else :
            print ('Getting data from cache...')
            data = cache_data
            return data


class imagehandler:
    '''
    imagehandler:
        * cache data is stored in a nosql database
    '''
    def __init__(self):
        self.db = unqlite('cachehandlerdata')
        self.api_cache = self.db.collection('imagecache')
        self.api_cache.create()

    def write_cache(self,image_link):
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        name = self.api_cache.__len__() + 1
        extension = image_link.split('.')[-1]
        filename = str(name) + '.' + str(extension)
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
            location = self.write_cache(image_link)
            return location
        else :
            print ('Getting image from cache...')
            location = cache_data
            return location

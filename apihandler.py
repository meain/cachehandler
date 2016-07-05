'''
Apihandler:
    * Cache data as file(database maybe?)
    * On incoming api request check for availability in cache for those which can be cached, otherwise jsut make a request and ...
    * Image caching will be done using another class, make calls to that when we get image links
    * The final image returned from the api will be a address of image from eywa server
'''
import os
from unqlite import UnQLite
import datetime
from locu.api import VenueApiClient
from apikeys import *

class apihandler:

    def __init__(self):
        self.db = UnQLite('datahandlerdata')
        self.api_cache = self.db.collection('apicache')
        self.api_cache.create()

    def write_cache(self, api_function, args, kwargs, data):
        self.api_cache.store({'api_function':str(api_function).split(' ')[2], 'args':args, 'kwargs':kwargs, 'data':data, 'time':datetime.datetime.now()})

    def read_cache(self, api_function, args, kwargs):
        cache_data = self.api_cache.filter(lambda api: api['api_function']==str(api_function).split(' ')[2] and api['args']==args and api['kwargs']==kwargs)
        import ipdb; ipdb.set_trace()
        # if length(cache_data) == 0:
        #     return cache_data
        # else :
        #     return cache_data[0]['data']
        return cache_data

    def api_call(self, api_function, *args, **kwargs):
        cache_data = self.read_cache(api_function, args, kwargs)
        print cache_data
        if not cache_data :
            print ('Getting data from cache...')
            data = api_function(*args, **kwargs)
            self.write_cache(api_function, args, kwargs, data)
            return data
        else :
            data = cache_data
            return data



# DEBUG
def main():
    venue = VenueApiClient(key_locu.key)
    handle = apihandler()
    data = handle.api_call(venue.search, locality='Boston')
    print (data)

if __name__ == '__main__':
    main()

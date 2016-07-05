from apihandler import apihandler
from locu.api import VenueApiClient
from apikeys import *

def main():
    venue = VenueApiClient(key_locu.key) # Create locu object
    handle = apihandler() # Create cache handler object
    '''
    Making calls:
        Original : venue.search(locality='New York')
    '''
    data = handle.api_call(venue.search, locality='New York')
    print data

if __name__ == '__main__':
    main()

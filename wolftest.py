from cachehandler import apihandler
import wolframalpha
from apikeys import *
import pickle

def main():
    client = wolframalpha.Client(key_wolfram.key)
    handle = apihandler()
    '''
    Making calls:
        Original : venue.search(locality='New York')
    '''
    data = handle.api_call(client.query, 'New York')
    print data

if __name__ == '__main__':
    main()

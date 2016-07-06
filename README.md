# Cachehandler

## ! Apihandler
Caches the result of apis and on consequent call gets the data from the cached data
### Usage
If the original funciton is :

```python
venue.search(locality='NY', menu='pizza')
```
You can use :

```python
from cachehandler import apihandler

handle=apihandler()
handle.api_call(venue.search, locality='NY', menu='pizza')
```

## ! Imagehandler
You can sent in a request and it will always return the adderss of the local file.
If file not available in cache, then it will be downloaded and then gives you the local file location
### Usage
Just pass in the link and if file is available locally it will serve the local copy immediately, otherwise it will download and server the downloaded copy.

`The address of the file given will be relative to the location of the code`

```python
from cachehandler import imagehandler

img = imagehandler()
location = img.get_image('http://ak-hdl.buzzfed.com/static/2015-04/21/16/enhanced/webdr05/enhanced-31550-1429646952-7.jpg')
```

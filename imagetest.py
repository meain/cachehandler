from cachehandler import imagehandler

def main():
    img = imagehandler()
    location = img.get_image('http://ak-hdl.buzzfed.com/static/2015-04/21/16/enhanced/webdr05/enhanced-31550-1429646952-7.jpg')
    print location

if __name__ == '__main__':
    main()

'''
Apihandler:
    * Cache data as file(database maybe?)
    * On incoming api request check for availability in cache for those which can be cached, otherwise jsut make a request and ...
    * Image caching will be done using another class, make calls to that when we get image links
    * The final image returned from the api will be a address of image from eywa server
'''
import os

class filehandler:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    data_file_location = base_dir + '/apihandlerdata'

    def __init__(self):
        print "Caching location :" + self.data_file_location

    def wirtedata(data):
        file = open(w)


class apihandler:
    pass




# DEBUG
def main():
    filehandler()

if __name__ == '__main__':
    main()

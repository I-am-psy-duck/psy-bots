from urllib import request

class RequestSource():
    def downloadFromSource(self, source:str, path:str):
        # download and saves from source to the path
        request.urlretrieve(source, path)
import httplib

def httptest(host, path="/"):
    """
    >>> httptest("stackoverflow.com","/nope")
    200
    
    """
    conn = httplib.HTTPConnection(host)
    conn.request("HEAD", path)
    return conn.getresponse().status

if __name__ == "__main__":
    import doctest
    doctest.testmod()

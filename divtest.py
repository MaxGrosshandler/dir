import httplib


def get_status_code(host, path=("/" + a)):
    """
    >>> get_status_code("stackoverflow.com", "questions")
    200
    
    """
    conn = httplib.HTTPConnection(host)
    conn.request("HEAD", path)
    return conn.getresponse().status


if __name__ == "__main__":
    import doctest
    doctest.testmod()

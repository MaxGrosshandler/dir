import requests

def reqtest(a):
    """
    >>> reqtest(questions)
    200
    """
    r = requests.head("http://stackoverflow.com" + "\"" + a )
    return(r.status_code)

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

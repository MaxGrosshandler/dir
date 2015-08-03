import requests


def reqtest(a):
    """
    >>> reqtest(1)
    200
    
    """
    r = requests.head("http://maxgrosshandler.pythonanywhere.com")
    return(r.status_code)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

import requests


def reqtest(a):
    """
    >>> reqtest("questions")
    200
    
    """
    a = raw_input("Enter where you want to go on stackoverflow")
    r = requests.head("http://stackoverflow.com/" + a )
    return(r.status_code)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

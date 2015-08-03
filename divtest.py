import requests


try:
    r = requests.head("http://stackoverflow.com")
    return(r.status_code)
except requests.ConnectionError:
    print("failed to connect")

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

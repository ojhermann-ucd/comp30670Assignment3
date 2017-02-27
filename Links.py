#valid connection to file
import urllib.request
from urllib.error import URLError, HTTPError


#validLink
def validLink(theLink):
    try:
        theSource = urllib.request.urlopen(theLink)
        return True
    except ValueError:
        return False
    except HTTPError:
        return False
    except URLError:
        return False
    else:
        return False
import urllib2
import json


def http_get(url_parts):
    """
    Make http GET reuqest for Python2

    Args:
        url_parts (dict):
            has "protocal" , "host" and "path" as keys.

    Raises:
        ValueError("No JSON object could be decoded")

    Return: 
        status_code (string)
        data (dict)
    """
    extended_url = url_parts['protocal'] + \
        '://' + url_parts['host'] + url_parts['path']
    req = urllib2.Request(extended_url)
    try:
        response = urllib2.urlopen(req)
        status_code = response.getcode()
    except urllib2.HTTPError as error:
        "TODO: What if json.loads raise error ?"
        response = ""
        status_code = error.getcode()
        # raise HttpError(error.getcode())
    data = json.loads(response.read())
    status_code = str(status_code)
    return str(status_code), data


def http_post(url_parts, data):

    headers = {'Content-Type': 'application/json'}
    data_str = json.dumps(data)

    extended_url = url_parts['protocal'] + \
        '://' + url_parts['host'] + url_parts['path']
    req = urllib2.Request(extended_url)

    try:
        response = urllib2.urlopen(req, data_str, headers)
        status_code = response.getcode()

    except urllib2.HTTPError as error:
        "TODO: What if json.loads raise error ?"
        response = ""
        status_code = error.getcode()
        # raise HttpError(error.getcode())
    data = json.loads(response.read())
    status_code = str(status_code)
    return str(status_code), data

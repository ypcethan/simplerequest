import json
import http.client


def http_get(url_parts):
    """
    Make http GET reuqest for Python3

    Args:
        url_parts (dict):
            has "protocal" , "host" and "path" as keys.

    Return: 
        status_code (string)
        data (dict)
    """
    conn = http.client.HTTPSConnection(url_parts['host'])
    conn.request('GET', url_parts['path'])
    response = conn.getresponse()
    data = json.loads(response.read())
    status_code = str(response.status)

    return status_code, data

import sys
import json
from simplehttp.utils import process_url
from simplehttp.error import HttpError

def encode_dict(obj):
    for k in obj:
        obj[k] = obj[k].encode('utf-8')
    return obj

def make_request(method, url, params=None, data=None):
    """[summary]

    Args:
        method (string): either GET or POST 
        url (string): 
        params (dict, optional):  Addtional parameters wish to add to the query string. Defaults to {}.
        data (dict, optional): Request body for POST request. Defaults to {}.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5. 

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format 
    """

    params = params or {} 
    data = data or {} 

    try: 
        # Python 3 
        import http.client
        from urllib.parse import urlencode
        url_parts = process_url(url, params)
        conn = http.client.HTTPSConnection(url_parts['host'])
        if method == 'GET':
            conn.request('GET', url_parts['path'])
        elif method == 'POST':
            headers = {'Content-Type': "application/json"}
            conn.request('POST', url_parts['path'],
                         body=json.dumps(data), headers=headers)

        try:
            response = conn.getresponse()
        except ConnectionError: 
            print('ConnectionError')
            raise

        status = str(response.status)
        if status.startswith('4') or status.startswith('5'):
            # raise HttpError(f"HTTP Status Code: {status}", int(status))
            raise HttpError(status)
        # if status.startswith('4') or status.startswith('5'):
        #     # raise HttpError(f"HTTP Status Code: {status}", int(status))
        #     raise HttpError(status)
        # # body here is byte string.
        # body = response.read()
        # json_data = json.loads(body)
        # return json.loads(body)
    except ImportError:
        # Python 2
        import urllib2
        params = encode_dict(params)
        url_parts = process_url(url, params)
        extended_url = url_parts['protocal'] + "://"+ url_parts['host'] + url_parts['path']
        if method == 'GET':
            req = urllib2.Request(extended_url)
        elif method == 'POST':

            headers = {'Content-Type': "application/json"}
            data_str = json.dumps(data)
            
            req = urllib2.Request(extended_url, data_str 
, headers)
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            raise HttpError(e.getcode())


    # body here is byte string.
    body = response.read()
    json_data = json.loads(body)
    return json.loads(body)
            

        



def get_json(url, params={}):
    """API for sending GET reuqest

    Args:
        url (string): 
        params (dict, optional): Addtional parameters wish to add to the query string. Defaults to {}.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    try:
        response = make_request('GET', url, params)

    except Exception as e:
        sys.last_value = e
        # re-raise the exception (allow the caller to handle)
        raise
    return response


def post_json(url, params={}, data={}):
    """API for sending POST reuqest

    Args:
        url (string): 
        params (dict, optional): Addtional parameters wish to add to the query string. Defaults to {}.
        data (dict, optional): Request body.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    try:
        response = make_request('POST', url, params, data)
    except Exception as e:
        sys.last_value = e
        raise
    return response

# def post_json(url, params={}, data={}):
#     url_parts = process_url(url, params)
#     conn = http.client.HTTPSConnection(url_parts['host'])
#     headers = {'Content-Type': "application/json"}
#     conn.request('POST', url_parts['path'],
#                  body=json.dumps(data), headers=headers)
#     response = conn.getresponse()
#     status = str(response.status)
#     if not status.startswith('2'):
#         raise simplehttp.HttpError(f"HTTP Status Code: {status}", status)
#     body = response.read()
#     return json.loads(body)

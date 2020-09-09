import json


def http_get(url_parts):

    try:
        import http.client
        conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('GET', url_parts['path'])
        response = conn.getresponse()
        status_code = str(response.status)

    except ImportError:
        import urllib2
        extended_url = url_parts['protocal'] + \
            '://' + url_parts['host'] + url_parts['path']
        req = urllib2.Request(extended_url)
        try:
            response = urllib2.urlopen(req)
            status_code = response.getcode()
        except urllib2.HTTPError as error:
            # TODO: What if json.loads raise error ?"
            response = ""
            status_code = error.getcode()
            # raise HttpError(error.getcode())
        status_code = str(status_code)

    data = json.loads(response.read())
    return str(status_code), data


def http_post(url_parts, data):

    headers = {'Content-Type': 'application/json'}
    data_str = json.dumps(data)
    try:
        import http.client

        conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('POST', url_parts['path'],
                     body=data_str, headers=headers
                     )
        response = conn.getresponse()
        data = json.loads(response.read())
        status_code = str(response.status)

        return status_code, data
    except ImportError:
        import urllib2

        extended_url = url_parts['protocal'] + \
            '://' + url_parts['host'] + url_parts['path']
        req = urllib2.Request(extended_url)

        try:
            response = urllib2.urlopen(req, data_str, headers)
            status_code = response.getcode()

        except urllib2.HTTPError as error:
            # TODO: What if json.loads raise error ?"
            response = ""
            status_code = error.getcode()
            # raise HttpError(error.getcode())
        status_code = str(status_code)
    data = json.loads(response.read())
    return status_code, data
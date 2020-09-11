# encoding=utf-8
from __future__ import unicode_literals
from simplehttp.error import InvalidUrlError
try:
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode


def process_url(url, params=None):
    """Extract host name and resources path

    Args:
        url (string): Full url.
        params (dict, optional): Addtional query paramters. Defaults to {}.

    Returns:
        [dict]: {host,path, protocal}
            host: Host name
            path: Resource path, constructed by appending
                    orginal resource path given parameters.
            protocal: Scheme used, (http or https)
    """
    # Split url into components.
    parsed_url = urlparse(url)
    (host, query, resources_path, protocal) = (parsed_url.hostname,
                                               parsed_url.query,
                                               parsed_url.path,
                                               parsed_url.scheme)
    if query:
        resources_path += "?" + query
    if params:
        resources_path = merge_path_with_params(resources_path, params)

    if not host or not protocal:
        raise InvalidUrlError(url)
    if not protocal in ['http', 'https']:
        raise InvalidUrlError(url)
    return {'host': host, 'path': resources_path, 'protocal': protocal}


def merge_path_with_params(path_string, params):
    """Appending path string with query parameters

    Args:
        path_string (str): Resource path
        params (dict): Query parameters

    Returns:
        [string]: Updated resource path.
    Examples:
        >>> merge_path_with_params('/get', {'debug': "true"})
        "/get?debug=true"

        >>> merge_path_with_params('/get?debug=true', {'limit': "20"})
        "/get?debug=true&limit=20"
    """
    if not params:
        return path_string
    process_params = join_params(params)
    # append '&' or "?" base on whether the path already
    # contain query parameters.
    path_string += "&" if "?" in path_string else "?"

    return path_string + process_params


def encode_params(params):
    """
        Convert unicode type to string.
        This is specifically for Python 2
        As urlencode only takes in tuple or dict 
        with str or byte as input.
    """

    encoded_params = {}

    for key, value in params.items():
        try:
            key = key.encode('utf-8')
        except AttributeError as e:
            key = str(key)
        try:
            value = value.encode('utf-8')
        except AttributeError as e:
            value = str(value)

        encoded_params[key] = value
    return encoded_params


def join_params(params):
    """Return a string of parameters join togeter with & as delemeter
       The order of parameters is determined by the key values,
       from left to right in ascending order.
       This is to keep the order consistant across Python versions.

    Args:
        params (dict): A dictionary of parameters

    Returns:
        string: A string of parameters join togeter with & as delemeter.
    Examples:
        >>> join_params({'debug':'true','limit':'20'})
        "debug=true&limit=20"
    """
    encoded_params = encode_params(params)
    params_array_sorted_by_keys = sorted(
        params.items(), key=lambda item: item[0])

    joined_params = urlencode(params_array_sorted_by_keys)
    return joined_params

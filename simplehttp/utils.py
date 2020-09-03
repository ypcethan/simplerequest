# encoding=utf-8
from collections import OrderedDict
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
            host: host name
            path: resource path, constructed by appending orginal resource path given parameters.
            protocal: scheme used, (http or https)
     Examples:
    """
    # Split url into components.
    parsed_url = urlparse(url)
    (host, query, resources_path, protocal) = (parsed_url.hostname,
                                               parsed_url.query, parsed_url.path, parsed_url.scheme)
    if query:
        resources_path += "?" + query
    if params:
        resources_path = merge_path_with_params(resources_path, params)

    return {'host': host, 'path': resources_path, 'protocal': protocal}


# def get_url_parts(url):

#     parsed_url = urlparse(url)

#     return {'host': parsed_url.hostname, 'path': parsed_url.path,
#             "query": parsed_url.query}


def merge_path_with_params(path_string, params):
    """Appending path string with query parameters

    Args:
        path_string (str): resource path 
        params (dict): query parameters 

    Returns:
        [string]: updated resource path.  
    Examples:
        >>> merge_path_with_params('/get', {'debug': "true"})
        "/get?debug=true"

        >>> merge_path_with_params('/get?debug=true', {'limit': "20"})
        "/get?debug=true&limit=20"
    """
    if len(params) == 0:
        return path_string
    process_params = join_params(params)
    if '?' in path_string:
        # path already contains query parameters.
        path_string += "&" + process_params
    else:
        path_string += '?' + process_params
    return path_string


def join_params(params):
    """Return a string of parameters join togeter with & as delemeter
       The order of parameters is determined by the key values, from left to right 
       in ascending order.

    Args:
        params (dict): A dictionary of parameters 

    Returns:
        string: A string of parameters join togeter with & as delemeter.
    Examples:
        >>> join_params({'debug':'true','limit':'20'})
        "debug=true&limit=20"
    """
    params_string = []
    for k in sorted(params.keys()):
        v = params[k]
        params_string.append(str(k) + "=" + str(v))
    joined_params = "&".join(params_string)
    return joined_params

# encoding=utf-8
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


def process_url(url, params=None):
    """Extract host name and resources path

    Args:
        url (string): Full url.
        params (dict, optional): Addtional query paramters. Defaults to {}.

    Returns:
        [dict]: {host,path, protocal}
            host: host name
            path: resource path, constructed by appending
                    orginal resource path given parameters.
            protocal: scheme used, (http or https)
     Examples:
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

    return {'host': host, 'path': resources_path, 'protocal': protocal}


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
    # append '&' or "?" base on whether the path already
    # contain query parameters.
    path_string += "&" if "?" in path_string else "?"

    return path_string + process_params


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
    params_array = []
    for param in sorted(params.keys()):
        value = params[param]
        params_array.append(str(param) + "=" + str(value))
    joined_params = "&".join(params_array)
    return joined_params

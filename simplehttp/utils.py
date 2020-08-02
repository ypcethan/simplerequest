from urllib.parse import urlparse, urlencode


def process_url(url, params={}):
    url_parts = get_url_parts(url)
    host = url_parts['host']
    query = url_parts['query']
    resources_path = url_parts['path']
    if len(query) > 0:
        resources_path += "?" + query
    if len(params) > 0:
        resources_path = merge_path_with_params(resources_path, params)

    return {'host': host, 'path': resources_path}


def get_url_parts(url):
    parsed_url = urlparse(url)

    return {'host': parsed_url.hostname, 'path': parsed_url.path,
            "query": parsed_url.query}


def merge_path_with_params(path_string, params):
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

    Args:
        params (dict): A dictionary of parameters 

    Returns:
        string: A string of parameters join togeter with & as delemeter.
    Examples:
        >>> join_params({'debug':'true','limit':'20'})
        "debug=true&limit=20"
    """
    joined_params = urlencode(params)

    return joined_params

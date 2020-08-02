from urllib.parse import urlparse, urlencode


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

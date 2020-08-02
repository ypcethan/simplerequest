import http.client
from simplehttp.utils import merge_path_with_params, get_url_parts


def get_json(url, params={}):
    url_parts = get_url_parts(url)
    host = url_parts['host']
    query = url_parts['query']
    resources_path = url_parts['path']
    if len(query) > 0:
        resources_path += "?" + query
    if len(params) > 0:
        resources_path = merge_path_with_params(resources_path, params)

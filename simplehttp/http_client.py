import sys
import logging
from simplehttp.error import HttpError, UnexpectedHttpError
from simplehttp.request import http_get, http_post


def get_json(url, params=None):
    """API for sending GET reuqest

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    params = params or {}
    try:
        # response = make_request('GET', url, params)

        response = http_get(url, params)

    except Exception as error:
        sys.last_value = error
        # re-raise the exception (allow the caller to handle)
        raise
    return response


def post_json(url, params=None, data=None):
    """API for sending POST reuqest

    Args:
        url (string): URL path
        params (dict, optional): Addtional parameters
            to  be added to the query string.
        data (dict, optional): Request body.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """

    params = params or {}
    data = data or {}
    try:
        # response = make_request('POST', url, params, data)
        response = http_post(url, params, data)
    except Exception as error:
        sys.last_value = error
        raise
    return response

# coding=utf-8
from __future__ import unicode_literals
import sys
import pytest
from simplehttp.http_client import get_json, post_json
from simplehttp.error import HttpError


@pytest.mark.parametrize('expected_response', [
    ({"isbn": "9789863479116", "title": u"流暢的 Python"}),
    ({"limit": "20", "title": u"流暢的 Python"})
])
def test_get_json(mocker, expected_response):
    # The function get mock is determined on where it is called,
    # not where is ia defined.
    http_get = mocker.patch('simplehttp.http_client.http_get',
                            return_value=expected_response)
    response = get_json('https://httpbin.org/get')
    assert response == expected_response
    assert http_get.called_once()


@pytest.mark.parametrize('expected_response', [
    ({"isbn": "9789863479116", "title": u"流暢的 Python"}),
    ({"limit": "20", "title": u"流暢的 Python"})
])
def test_post_json(mocker, expected_response):
    mocker.patch('simplehttp.http_client.http_post',
                 return_value=expected_response)
    response = post_json('dummy_url')
    assert response == expected_response


@pytest.mark.parametrize('expecetd_error_code', [400, 404, 500])
def test_get_json__http_error(mocker, expecetd_error_code):
    mocker.patch('simplehttp.http_client.http_get',
                 side_effect=HttpError(expecetd_error_code))
    with pytest.raises(HttpError) as error:
        get_json('dummy_url')
    assert error.value.message == "HTTP Status Code: %s" % str(
        expecetd_error_code)
    # If HttpError were raised, sys.last_value should
    # have status_code attribute.
    assert sys.last_value.status_code == expecetd_error_code


@pytest.mark.parametrize('expecetd_error_code', [400, 404, 500])
def test_post_json__http_error(mocker, expecetd_error_code):
    mocker.patch('simplehttp.http_client.http_post',
                 side_effect=HttpError(expecetd_error_code))
    with pytest.raises(HttpError) as error:
        post_json('dummy_url')
    assert error.value.message == "HTTP Status Code: %s" % str(
        expecetd_error_code)
    # If HttpError were raised, sys.last_value should
    # have status_code attribute.
    assert sys.last_value.status_code == expecetd_error_code


# def test_post_json_ConnectionError(mocker):
#     mocker.patch('http.client.HTTPConnection.getresponse',
#                  side_effect=ConnectionError())
#     with pytest.raises(ConnectionError) as error:
#         conn = http.client.HTTPSConnection('host')
#         response = conn.getresponse()

# def test_post_json_ConnectionError(mocker):
#     mocker.patch('http.client.HTTPConnection.getresponse',
#                  side_effect=ConnectionError())
#     with pytest.raises(ConnectionError) as error:
#         get_json('dummy_url')

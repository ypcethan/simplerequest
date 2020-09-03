from __future__ import unicode_literals
# coding=utf-8
import sys
import json
import pytest
from simplehttp import get_json, post_json
from simplehttp.error import HttpError


@pytest.mark.parametrize('url,params,expected_result', [
    ('https://httpbin.org/get', {}, {}),
    ('https://httpbin.org/get?debug=true', {}, {'debug': 'true'}),
    ('https://httpbin.org/get?debug=true', {'limit': '20'}, {'debug': 'true',
                                                             'limit': '20'})
])
def test_get_json(url, params, expected_result):
    response = get_json(url, params)
    assert response['args'] == expected_result


@pytest.mark.parametrize('url,params,data,expected_args, expected_data', [
    ('https://httpbin.org/post', {}, {}, {}, {}),
    ('https://httpbin.org/post?debug=true', {}, {}, {'debug': 'true'}, {}),
    ('https://httpbin.org/post?debug=true', {}, {
        "isbn": "9789863479116", "title": "流暢的 Python"
    }, {'debug': 'true'}, {
        "isbn": "9789863479116", "title": "流暢的 Python"
    }),
    ('https://httpbin.org/post?debug=true', {}, {
        "isbn": "9789863479116", "title": "常⾒見見問題 Q&A"
    }, {'debug': 'true'}, {
        "isbn": "9789863479116", "title": "常⾒見見問題 Q&A"
    }),
])
def test_post_json(url, params, data, expected_args, expected_data):
    response = post_json(url, params, data)
    assert response['args'] == expected_args
    assert json.loads(response['data']) == expected_data


@pytest.mark.parametrize('url,error_code', [
    ('https://httpbin.org/status/400',  400),
    ('https://httpbin.org/status/500',  500),
])
def test_post_json_error_code(url,  error_code):
    with pytest.raises(HttpError) as e:
        response = post_json(url)
    assert e.value.message == "HTTP Status Code: %s" % str(error_code)
    assert sys.last_value.status_code == error_code


@pytest.mark.parametrize('url,error_code', [
    ('https://httpbin.org/status/400',  400),
    ('https://httpbin.org/status/500',  500),
])
def test_get_json_error_code(url,  error_code):
    with pytest.raises(HttpError) as e:
        response = get_json(url)
    assert e.value.message == "HTTP Status Code: %s" % str(error_code)
    assert sys.last_value.status_code == error_code

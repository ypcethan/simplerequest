# encoding=utf-8
from __future__ import unicode_literals
import pytest
from simplehttp.utils import join_params, merge_path_with_params, process_url


@pytest.mark.parametrize('params,expected_result', [
    ({'a': 1, 'b': 2, 'A': 3, 'C': 4}, 'A=3&C=4&a=1&b=2'),
    ({'debug': "true"}, "debug=true"),
    ({'debug': "true", 'limit': '20'}, "debug=true&limit=20"),
    ({'debug': "true", 'limit': '20', 'time': "1h"}, "debug=true&limit=20&time=1h"),
])
def test_join_params(params,  expected_result):
    assert join_params(params) == expected_result


@pytest.mark.parametrize('path, params,expected_result', [
    ('/post', {}, '/post'),
    ('/post', {'debug': "true"}, '/post?debug=true'),
    ('/get', {'debug': "true"}, '/get?debug=true'),
    ('/get?debug=true', {'limit': "20"}, '/get?debug=true&limit=20'),
    ('/get?debug=true', {'limit': "20", 'time': '1h'},
     '/get?debug=true&limit=20&time=1h'),
])
def test_merge_path_with_params(path, params, expected_result):
    assert merge_path_with_params(path, params) == expected_result


@pytest.mark.parametrize('url,params ,expected_result', [
    ('https://httpbin.org/get?debug=true&par2=232', {},
        {'host': 'httpbin.org', 'path': '/get?debug=true&par2=232', 'protocal': 'https'}),
    ('https://httpbin.org/post?debug=true&par2=232', {},
     {'host': 'httpbin.org', 'path': '/post?debug=true&par2=232', 'protocal': 'https'}),
    ('https://httpbin.org/post?debug=true&par2=232', {'limit': 20},
     {'host': 'httpbin.org', 'path': '/post?debug=true&par2=232&limit=20', 'protocal': 'https'}),
    ('https://httpbin.org/post?debug=true&par2=232', {'limit': 20, 'time': '1h'},
     {'host': 'httpbin.org', 'path': '/post?debug=true&par2=232&limit=20&time=1h', 'protocal': 'https'}),
    ('http://httpbin.org/post', {'limit': 20, 'time': '1h'},
     {'host': 'httpbin.org', 'path': '/post?limit=20&time=1h', 'protocal': 'http'}),
])
def test_process_url(url, params, expected_result):
    assert process_url(url, params) == expected_result

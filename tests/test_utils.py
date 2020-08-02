import pytest
from simplehttp.utils import join_params, merge_path_with_params, get_url_parts


@pytest.mark.parametrize('params,expected_result', [
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


@pytest.mark.parametrize('url, expected_result', [
    ('https://httpbin.org/get?debug=true&par2=232',
     {'host': 'httpbin.org', 'path': '/get', 'query': 'debug=true&par2=232'}),
    ('https://httpbin.org/post?debug=false&par2=232',
     {'host': 'httpbin.org', 'path': '/post', 'query': 'debug=false&par2=232'}),
])
def test_get_url_parts(url,  expected_result):
    assert get_url_parts(url) == expected_result

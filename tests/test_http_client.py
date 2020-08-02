import pytest
from simplehttp import get_json


@pytest.mark.parametrize('url,params,expected_result', [
    ('https://httpbin.org/get', {}, {}),
    ('https://httpbin.org/get?debug=true', {}, {'debug': 'true'}),
    ('https://httpbin.org/get?debug=true', {'limit': '20'}, {'debug': 'true',
                                                             'limit': '20'})
])
def test_get_json(url, params, expected_result):
    response = get_json(url, params)
    assert response['args'] == expected_result

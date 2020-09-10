
from __future__ import unicode_literals
# coding=utf-8
import sys
import json
import pytest
from simplehttp.request import http_get, http_post
from simplehttp.http_client import get_json, post_json
from simplehttp.error import HttpError


@pytest.fixture
def test_get_json(mocker):
    mocker.patch('http_get', return_value=5)
    actual = http_get()
    expected = 6
    assert expected == actual

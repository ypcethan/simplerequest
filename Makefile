setup:
	pip install pipenv
	pipenv install --dev
	pipenv install -e .

test:
	tox -- tests/test_http_client.py tests/test_utils.py

test-large:
	tox -- tests/test_request.py

test-all:
	tox

test-only-local:
	pytest


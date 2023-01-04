test:
	poetry run coverage run -m pytest

coverage:
	poetry run coverage report

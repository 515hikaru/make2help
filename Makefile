## exec unit test
test: tests/test_make2help.py
	python -m unittest tests/test_make2help.py
## Show target list
help:
	@python make2help.py

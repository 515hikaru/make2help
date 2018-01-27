## install this command
install:
	python setup.py install
## exec unit test
test: tests/test_make2help.py
	python -m unittest tests/test_make2help.py
## Show target list
help:
	@make2help 

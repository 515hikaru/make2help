## install this command
install:
	python setup.py install
## install for development
develop:
	python setup.py develop
## exec unit test
test: tests/test_make2help.py
	python -m unittest tests/test_make2help.py
## Show target list
help:
	@make2help 

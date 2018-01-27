## install this command
install:
	python3 setup.py install
## install for development
develop:
	python3 setup.py develop
## exec unit test
test: tests/test_make2help.py
	python3 -m unittest tests/test_make2help.py
## Show target list
help:
	@make2help 

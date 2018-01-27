"""
Unit Test for make2help.py
"""
import unittest

import make2help


class TestPrintString(unittest.TestCase):
    """Testing for expected format string"""

    def test_makefile_format(self):
        """
        target = 'foo'
        detail = 'help'
        => return 'foo:\thelp'
        """
        result = make2help.format_makehelp('foo', 'help')
        self.assertEqual(result, 'foo:\thelp')


class TestParseMakefile(unittest.TestCase):
    """Testing for Makefile parser"""

    def test_makefile_parse_normal_target(self):
        """
        ```
        ## help
        target: foo
        	@echo "foo"
        ```
        expected return value is ('target', 'help')
        """
        result = make2help.parse_makefile(
            ['## help', 'target: foo', '\t@echo "foo"'])
        self.assertEqual(next(result), ('target', 'help'))

    def test_makefile_none_help(self):
        """
        ```
        target: foo
        	@echo "foo"
        ```
        expected return value is ('target', '')
        """
        result = make2help.parse_makefile(['target: foo', '\t@echo "foo"'])
        self.assertEqual(next(result), ('target', 'help'))


if __name__ == '__main__':
    unittest.main()

"""
Unit Test for make2help.py
"""
import os
import unittest

import make2help

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

class TestPrintString(unittest.TestCase):
    """出力文字列が想定通りかをテスト"""

    def test_example_makefile(self):
        """
        ```
        ## foo
        bar:
        	@echo "foo"
        ```
        という形式のMakefileのテスト
        出力されるヘルプは 'bar:\tfoo' となる
        """
        makefile_path = os.path.join(BASE_DIR, 'sample/Makefile1')
        result = make2help.format_makehelp(makefile_path)
        expected = ('bar:\tfoo')
        self.assertEqual(next(result), expected)


if __name__ == '__main__':
    unittest.main()

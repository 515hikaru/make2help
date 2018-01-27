"""
Unit Test for make2help.py
"""
import pathlib
import unittest

import make2help

BASE_DIR = pathlib.Path(__file__).absolute().parent.parent / pathlib.Path(
    'sample')


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
        makefile_path = BASE_DIR / pathlib.Path('Makefile1')
        result = make2help.format_makehelp(makefile_path)
        expected = 'bar:\tfoo'
        self.assertEqual(next(result), expected)

    def test_comment_empty_target(self):
        """
        ```
        bar:
        	@echo "foo"
        ```
        のように `##` がなかった場合でも `bar` は出力をする
        """
        makefile_path = BASE_DIR / pathlib.Path('Makefile2')
        result = make2help.format_makehelp(makefile_path)
        expected = 'bar'
        self.assertEqual(next(result), expected)


if __name__ == '__main__':
    unittest.main()

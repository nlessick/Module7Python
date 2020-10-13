import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as basic_list_exception


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        basic_list_exception.make_list()


if __name__ == '__main__':
    unittest.main()

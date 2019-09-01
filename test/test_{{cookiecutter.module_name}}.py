import unittest

import {{cookiecutter.module_name}}


class {{cookiecutter.module_name}}TestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.module_name}}.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('{{cookiecutter.module_name}}', rv.data.decode())


if __name__ == '__main__':
    unittest.main()

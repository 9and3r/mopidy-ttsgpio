from __future__ import unicode_literals

import unittest

# from mopidy_ttsgpio import frontend as frontend_lib
from mopidy_ttsgpio import Extension


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = Extension()

        config = ext.get_default_config()

        self.assertIn('[ttsgpio]', config)
        self.assertIn('enabled = true', config)

    def test_get_config_schema(self):
        ext = Extension()
        schema = ext.get_config_schema()
        self.assertIn('pin_button_main', schema)

        # TODO Test the content of your config schema
        # self.assertIn('username', schema)
        # self.assertIn('password', schema)

    # TODO Write more tests

from __future__ import unicode_literals

import mock
import unittest

from mopidy_ttsgpio import frontend
from mopidy_ttsgpio import Extension


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = Extension()
        config = ext.get_default_config()
        # ext = frontend.TtsGpio(config, mock.sentinel.core)
        self.assertIn('[ttsgpio]', config)
        self.assertIn('enabled = true', config)

    def test_get_config_schema(self):
        ext = Extension()
        schema = ext.get_config_schema()
        self.assertIn('pin_button_main', schema)
        self.assertIn('pin_button_next', schema)
        self.assertIn('pin_button_previous', schema)
        self.assertIn('pin_button_vol_up', schema)
        self.assertIn('pin_button_vol_up', schema)
        self.assertIn('pin_button_vol_down', schema)

import unittest

import linefind_setting as S

# Example test with valid imports and a test to get started.
class SettingTest(unittest.TestCase):

  def test_str(self):
    settings = S.LinefindSetting(debug = True)
    self.assertEqual("LinefindSetting(debug=True)", str(settings))

import unittest

import pendulum

from tz.timezones import create_list, get_tz_time


class TestTzApp(unittest.TestCase):

    def test_create_list(self):
        tz_list = create_list()
        self.assertEqual(len(tz_list), 593)
        self.assertIn('Australia/Sydney', tz_list)
        self.assertIn('Europe/Madrid', tz_list)
        self.assertNotIn('Europe/Alicante', tz_list)

    def test_get_tz(self):
        utc = pendulum.now(tz='UTC')
        cet_str = get_tz_time('Europe/Amsterdam')
        # could get a one off second
        cet_dt = pendulum.parse(cet_str).add(seconds=2)
        diff = cet_dt.diff(utc).in_hours()
        self.assertEqual(diff, 2)
        aus_str = get_tz_time('Australia/Sydney')
        aus_dt = pendulum.parse(aus_str).add(seconds=2)
        diff = aus_dt.diff(utc).in_hours()
        self.assertEqual(diff, 10)


if __name__ == '__main__':
    unittest.main()

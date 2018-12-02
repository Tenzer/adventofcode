#!/usr/bin/env python3

import unittest

import calibrate


class TestAdjust(unittest.TestCase):
    def test_adjust(self):
        frequency = 0

        frequency = calibrate.adjust(frequency, "+1")
        self.assertEqual(frequency, 1)

        frequency = calibrate.adjust(frequency, "-2")
        self.assertEqual(frequency, -1)

        frequency = calibrate.adjust(frequency, "+3")
        self.assertEqual(frequency, 2)

        frequency = calibrate.adjust(frequency, "+1")
        self.assertEqual(frequency, 3)


if __name__ == "__main__":
    unittest.main()

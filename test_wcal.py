#!/usr/bin/env python

import unittest
import random
from wcal import get_month_index

class wcalTestCase(unittest.TestCase):
    """Testing for wcal"""

    def test_get_month_index(self):
        """Test that three character month given returns correct numeric index.

        Returns:
            expected True
        """
        months = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12
        }

        MONTH_TO_TEST_ABBREVIATION = random.sample(months ,1)[0]
        MONTH_TO_TEST_INDEX = months[MONTH_TO_TEST_ABBREVIATION]

        self.assertEqual(get_month_index(MONTH_TO_TEST_ABBREVIATION), str(MONTH_TO_TEST_INDEX).zfill(2))

if __name__ == '__main__':
    unittest.main()

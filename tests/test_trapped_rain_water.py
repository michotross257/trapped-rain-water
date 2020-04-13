import os
import sys
import unittest
sys.path.insert(1, os.getcwd().rstrip('/tests'))

from trapped_rain_water import count_trapped_water


class TestTrappedRainWater(unittest.TestCase):

    tests = [
        {
            'elevation_map': [1,0,2,1,0,1,3,2,1,2,1],
            'expected': 6
        },
        {
            'elevation_map': [1,0,2,1,0,1,3,2,1,3,0],
            'expected': 8
        },
        {
            'elevation_map': [0,1,2,3,4],
            'expected': 0,
        },
        {
            'elevation_map': [4,3,2,1,0],
            'expected': 0
        },
        {
            'elevation_map': [4,3,0,2,1],
            'expected': 2
        },
        {
            'elevation_map': [4,3,0,2,1,4,1,1,0],
            'expected': 10
        },
        {
            'elevation_map': [1,1,1],
            'expected': 0
        },
        {
            'elevation_map': [0,0],
            'expected': 0
        },
        {
            'elevation_map': [1,0,4,0,0,4,0,1],
            'expected': 10
        }
    ]

    def test_count_trapped_water(self):
        """
        Test that the count_trapped_water function returns a list that sums to
        the expected count.
        """
        for axis in [0,1]:
            for test in self.tests:
                elevation_map, expected = test['elevation_map'], test['expected']
                with self.subTest(elevation_map=elevation_map, axis=axis, expected=expected):
                    self.assertEqual(sum(count_trapped_water(elevation_map, axis=axis)), expected)


if __name__ == '__main__':
    unittest.main()

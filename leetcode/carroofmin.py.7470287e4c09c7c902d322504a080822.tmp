import unittest
import sys


def min_roof_length(parking_spots, k):
    # Input validations...
    # what if k > len(parking_spots)?
    if not parking_spots or k == 0:
        return 0
    if k > len(parking_spots):
        return sys.maxsize

    parking_spots.sort()
    ans = sys.maxsize
    for i in range(0, len(parking_spots) - k + 1):
        ans = min(ans, parking_spots[i + k - 1] - parking_spots[i] + 1)
    return ans


class TestMinRoofLength(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(5, min_roof_length([12, 6, 5, 2], 3))
        self.assertEqual(8, min_roof_length([2, 5, 6, 9, 12], 4))


if __name__ == "__main__":
    unittest.main()

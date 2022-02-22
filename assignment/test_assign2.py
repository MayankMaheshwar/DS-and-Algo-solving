import unittest
import assign2


class TestMedian(unittest.TestCase):
    def test_median(self):
        # test median with odd numbers

        obj = assign2.MedianFinder()
        obj.addNum(3)
        obj.addNum(1)
        obj.addNum(5)
        obj.addNum(4)
        obj.addNum(2)

        self.assertAlmostEqual(obj.findMedian(), 3)

    def test_median(self):
        # test median with odd numbers

        obj = assign2.MedianFinder()
        obj.addNum(3)
        obj.addNum(1)
        obj.addNum(5)
        obj.addNum(4)
        obj.addNum(2)

        self.assertAlmostEqual(obj.findMedian(), 3)

        # test median with odd numbers

        obj.addNum(6)
        self.assertAlmostEqual(obj.findMedian(), 3.5)


if __name__ == '__main__':
    unittest.main()

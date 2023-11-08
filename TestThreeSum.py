import unittest
from ThreeSum import threeSum

class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        target = 1000000005
        arr = [1,2,3,4,1000000000]
        self.assertTrue(threeSum(target,arr))


if __name__ == '__main__':
    unittest.main()
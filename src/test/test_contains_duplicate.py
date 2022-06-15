"""
unittest
"""

import unittest
from LeetProblem.contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self) -> None:
        self.nums_1 = [1, 2, 3, 1]
        self.nums_2 = [1, 2, 3, 4]
        self.nums_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

        self.output_1 = True
        self.output_2 = False
        self.output_3 = True

    def test_contains_duplicate(self):
        self.assertEqual(Solution().containsDuplicate_1(self.nums_1), self.output_1)
        self.assertEqual(Solution().containsDuplicate_1(self.nums_2), self.output_2)
        self.assertEqual(Solution().containsDuplicate_1(self.nums_3), self.output_3)

        self.assertEqual(Solution().containsDuplicate_2(self.nums_1), self.output_1)
        self.assertEqual(Solution().containsDuplicate_2(self.nums_2), self.output_2)
        self.assertEqual(Solution().containsDuplicate_2(self.nums_3), self.output_3)


if __name__ == "__main__":
    unittest.main()

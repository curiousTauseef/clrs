import random
import unittest
from selection_sort import sort_nondecreasing

class InsertionSortTests(unittest.TestCase):

    def test_nondecreasing_empty(self):
        self.assertEqual(sort_nondecreasing([]), [])

    def test_nondecreasing_single(self):
        self.assertEqual(sort_nondecreasing([0]), [0])

    def test_random(self):
        sequence = [random.randint(0, 100) for i in range(100)]
        self.assertListEqual(sort_nondecreasing(sequence), sorted(sequence))

    def test_decreasing(self):
        sequence = list(range(100, 0, -1)) 
        self.assertListEqual(sort_nondecreasing(sequence), sorted(sequence))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

import unittest
from divisor_count import DivisorCounter

class TestDivisorCounter(unittest.TestCase):
    def test_divisor_count_example(self):
        counter = DivisorCounter(max_k=15)
        self.assertEqual(counter.solve_for_k(15), 2)

    def test_divisor_count_edge_cases(self):
        counter = DivisorCounter(max_k=10)
        self.assertEqual(counter.solve_for_k(0), 0)
        self.assertEqual(counter.solve_for_k(1), 0)
        self.assertEqual(counter.solve_for_k(2), 0)
        self.assertEqual(counter.solve_for_k(3), 1)

    def test_k_out_of_bounds_raises_error(self):
        counter = DivisorCounter(max_k=10)
        with self.assertRaisesRegex(ValueError, "k exceeds precomputed max_k"):
            counter.solve_for_k(11)

    def test_larger_k(self):
        counter = DivisorCounter(max_k=20)
        self.assertEqual(counter.solve_for_k(16), 2)

if __name__ == '__main__':
    unittest.main()

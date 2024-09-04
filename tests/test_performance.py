import time
import unittest
from lib.helper import factorial

class TestPerformance(unittest.TestCase):
    def test_factorial_performance(self):
        start_time = time.time()
        factorial(100000)  # This is a large computation
        duration = time.time() - start_time
        self.assertLess(duration, 1.0, "Performance test failed, took too long.")

if __name__ == "__main__":
    unittest.main()

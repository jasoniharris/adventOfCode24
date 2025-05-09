#!/usr/bin/env python3
import unittest
import tempfile
import os
from solution import calculate_total_distance

class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with the example data from the challenge
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        with open(self.temp_file.name, 'w') as f:
            f.write("3   4\n")
            f.write("4   3\n")
            f.write("2   5\n")
            f.write("1   3\n")
            f.write("3   9\n")
            f.write("3   3\n")
    
    def tearDown(self):
        # Clean up the temporary file
        os.unlink(self.temp_file.name)
    
    def test_example_data(self):
        # Test with the example data from the challenge
        # Expected result: 2 + 1 + 0 + 1 + 2 + 5 = 11
        result = calculate_total_distance(self.temp_file.name)
        self.assertEqual(result, 11, "The total distance should be 11 for the example data")
    
    def test_empty_file(self):
        # Test with an empty file
        empty_file = tempfile.NamedTemporaryFile(delete=False)
        empty_file.close()
        
        try:
            result = calculate_total_distance(empty_file.name)
            self.assertEqual(result, 0, "The total distance should be 0 for an empty file")
        finally:
            os.unlink(empty_file.name)
    
    def test_single_line(self):
        # Test with a single line
        single_line_file = tempfile.NamedTemporaryFile(delete=False)
        with open(single_line_file.name, 'w') as f:
            f.write("10  20\n")
        
        try:
            result = calculate_total_distance(single_line_file.name)
            self.assertEqual(result, 10, "The total distance should be 10 for a single line with values 10 and 20")
        finally:
            os.unlink(single_line_file.name)
    
    def test_negative_numbers(self):
        # Test with negative numbers
        neg_file = tempfile.NamedTemporaryFile(delete=False)
        with open(neg_file.name, 'w') as f:
            f.write("-5  10\n")
            f.write("15  -3\n")
        
        try:
            # After sorting:
            # Left list: [-5, 15]
            # Right list: [-3, 10]
            # Distances: |-5-(-3)| + |15-10| = 2 + 5 = 7
            result = calculate_total_distance(neg_file.name)
            self.assertEqual(result, 7, "The total distance should be 7 for the given negative numbers")
        finally:
            os.unlink(neg_file.name)

if __name__ == "__main__":
    unittest.main()
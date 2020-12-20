#!/usr/bin/env python3

'''
This script runs the unit tests on the existing script to find a problem and
correct it.The tests are run to overcome the existing problems in the script and give solution
to it.
1st param  = script name itself. Hence we pass here "None" as we are calling it from the tests and not directly
2nd, 3rd params =  names
'''
import unittest
from emails import find_email

class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

  def test_two_name(self):
    testcase = [None, "Roy","Cooper"]
    expected = "No email address found"
    self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
  unittest.main()
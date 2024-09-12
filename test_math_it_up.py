import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(4) == True
  assert math_it_up.is_even(-2) == True
  assert math_it_up.is_even(1) != True
  assert math_it_up.is_even(-1004) == True
  assert math_it_up.is_even(0) == True
  assert math_it_up.is_even(-3) == False

def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert math_it_up.is_odd(1) == True
  assert math_it_up.is_odd(23) == True
  assert math_it_up.is_odd(24) == False
  assert math_it_up.is_odd(7) != False
  assert math_it_up.is_odd(9) == True
  assert math_it_up.is_odd(12) == False
  assert math_it_up.is_odd(5) == True

def test_mean():
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean([1, 2, 2, 4, 5, 0, 0]) == 2
  assert math_it_up.mean([2, 2, 0, 0]) == 1
  assert math_it_up.mean([0, 0, 0, 0, 0, 0, 0, 0]) == 0
  assert math_it_up.mean([-10, -20, -30]) == -20
  assert math_it_up.mean([6]) == 6

def test_median():
  """
  Tests for the `median` function
  """
  assert math_it_up.median([0, 2, 2, 3, 3]) == 2
  assert math_it_up.median([23, 24, 25, 34, 39]) == 25
  assert math_it_up.median([0, -2, -2, -3, -3]) == -2
  assert math_it_up.median([0, 12, 22, 33, 43]) == 22
  assert math_it_up.median([0, 42, 68, 73, 133]) == 68

def test_mode():
  """
  Tests for the `mode` function
  """
  assert math_it_up.mode([2, 2, 2, 2, 3, 4]) == [2]
  assert math_it_up.mode([-5, -5, -5, -5, -7, -8, -10, -14, -20]) == [-5]
  assert math_it_up.mode([16, 24, 30, 44, 65, 65, 65, 65, 80]) == [65]
  assert math_it_up.mode([9]) == [9]
  assert math_it_up.mode([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0]
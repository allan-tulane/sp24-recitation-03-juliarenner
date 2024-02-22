from main import *


## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
  assert quadratic_multiply(BinaryNumber(5), BinaryNumber(6)) == 5 * 6
  assert quadratic_multiply(BinaryNumber(12), BinaryNumber(1)) == 12 * 1
  assert quadratic_multiply(BinaryNumber(150), BinaryNumber(0)) == 150 * 0


print(test_multiply())

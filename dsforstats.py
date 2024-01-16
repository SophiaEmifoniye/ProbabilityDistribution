  # Solving problems in statistics

import math
from utils import probability
from utils.testing import test_equal, test_close
import utils.counting as C

print("\nSOME PROBABILITY PROBLEMS\n")

# Question 1
print("Q: Find the probability of getting a head when you toss a fair coin?")
p_head = probability(1, 2)
print(p_head)
print("A: The probability is {}".format(p_head) )
expected_p_head = 0.5
test_equal(p_head, expected_p_head)
print("")
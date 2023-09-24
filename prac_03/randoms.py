""" CP1404/CP5632 - Practical 3 randoms.py"""

import random

# What did you see on line 1?
# 15, 16 and 11
# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# What did you see on line 2?
# 5, 3, and 3
# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4?
# No.  It is set in increments of 2 beginning at 3 so will not select 4

# What did you see on line 3?
# 5.377053169956014, 3.3388253724450174 and 4.8011705322152105
# What was the smallest number you could have seen, what was the largest?
# 2.5, 5.444444444444449

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
# assuming a random integer
random_number = random.randint(0, 100)

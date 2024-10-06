# What did you see on line 1?
# The print statement was generating a random integer between 5 and 20 inclusive.
# What was the smallest number you could have seen, what was the largest?
# 5 was the smallest and 20 was the largest.
# What did you see on line 2?
# The print statement was generating a  random integer selected from the range starting at 3, up to but not including
# 10, with a step of 2.
# What was the smallest number you could have seen, what was the largest?
# 3 was the smallest and 9 was the largest.
# Could line 2 have produced a 4?
# No, the step of 2 only produces odd numbers (3, 5, 7, 9).
# What did you see on line 3?
# The print statement was generating a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# 2.5471868652035234 was the smallest and 5.455893537149981 was the largest
# Write code, not a comment, to produce a random number between 1 and 100 inclusive
import random
print(random.randint(1, 100))

# You are given an integer n representing the number of steps to reach the top
#  of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:

# Input: n = 2

# Output: 2
# Explanation:

# 1 + 1 = 2
# 2 = 2
# Example 2:

# Input: n = 3

# Output: 3

def climbStairs( n: int) -> int:
    if n <= 2:
        return n

    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


print(climbStairs(5))
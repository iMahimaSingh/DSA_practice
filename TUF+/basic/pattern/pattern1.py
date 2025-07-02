# https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-1

"""
Pattern 1

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****

*****

*****

*****

*****



Print the pattern in the function given to you.
"""

class Solution:
    def pattern1(self, n):
        for i in range(1,n+1):
            for j in range(n):
                print("*", end="")
            print()

# Time Complexity:O(N2) As two for loops are being used to print the patterns and both of them runs for N time.

# Space Complexity: As no additional space is used, so the Space Complexity is O(1)


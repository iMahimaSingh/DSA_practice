#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-17
"""

Pattern 17

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

Print the pattern in the function given to you.
"""
class Solution:
    def pattern17(self, n):
        
         for i in range(n):
            # Spaces before letters
            spaces = " " * (n - i - 1)
            print(spaces, end="")

            # Increasing letters (left side)
            letter = 'A'
            for j in range(i + 1):
                print(letter, end="")
                letter = chr(ord(letter) + 1)

            # Decreasing letters (right side)
            letter = chr(ord(letter) - 2)
            for j in range(i):
                print(letter, end="")
                letter = chr(ord(letter) - 1)

            print()
#Time Complexity : O(N2). The overall complexity will be O(N2), due to nested loops iterating over each row for spaces and characters to be printed. Where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
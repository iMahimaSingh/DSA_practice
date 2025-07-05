#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-15

"""
Pattern 15

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

ABCDE
ABCD
ABC
AB
A

Print the pattern in the function given to you.
"""
class Solution:
    def pattern15(self, n):
        for i in range(n):
            letter=65
            for j in range(n-i):
                print(chr(letter),end="")
                letter +=1
            print()

#Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
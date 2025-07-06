#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-16
"""
Pattern 16

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

A
BB
CCC
DDDD
EEEEE

Print the pattern in the function given to you.
"""
class Solution:
    def pattern16(self, n):
        letter=65
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(chr(letter),end="")
            letter+=1    
            print()

#Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
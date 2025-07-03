#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-11

"""
Pattern 11

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1



Print the pattern in the function given to you.
"""

class Solution:
    def pattern11(self, n):
        for i in range(1,n+1):
            for j in range(i,2*i):
                if j%2!=0:
                    print("1 ",end="")
                else:
                    print("0 ",end="")
            print()

#Time Complexity : O(N2). Where, N is the number of rows provided as an input.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
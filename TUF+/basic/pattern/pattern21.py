#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-21
"""
Pattern 21

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
*   *
*   *
*   *
*****

Print the pattern in the function given to you.
"""
class Solution:
    def pattern21(self, n):
        for i in range(1,n+1):
            if i==1:
                print("*"*n)

            elif i<n:
                spaces=" "*(n-2)
                print("*"+spaces+"*")
            else:
                if i==n:
                    print("*"*n)

#Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-10

"""
Pattern 10

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****
****
***
**
*

Print the pattern in the function given to you.
"""

class Solution:
    def pattern10(self, n):
        for i in range(1,2*n):
            if i<=n:
                print(("*"*i)+((" ")*(n-i)))
            else:
                if i>n:
                    print((("*")*(2*n-i))+((" ")*(i-n)))

#Time Complexity : O(N2). Where N is the input provided. This quadratic complexity arises due to the nested loops iterating over N rows and printing a number of stars that sums up to approximately N2 stars in total.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
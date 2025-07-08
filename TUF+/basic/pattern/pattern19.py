#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-19?tab=submissions
"""
Pattern 19

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

Print the pattern in the function given to you.
"""
class Solution:
    def pattern19(self, n):
        for i in range(2*n):
            if i==0:
                print("*"*2*n)
            elif i>=1 and i<n:
                stars="*" * (n-i)
                spaces=" "*i
                print(stars+spaces+spaces+stars)
            else:
                if i>=n:
                    stars="*"* (i-n+1)
                    spaces=" "* (2*n-i-1)
                    print(stars+spaces+spaces+stars)

#Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
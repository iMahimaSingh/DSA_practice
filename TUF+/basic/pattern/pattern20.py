#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-20
"""
Pattern 20

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

Print the pattern in the function given to you.
"""
class Solution:
    def pattern20(self, n):
        for i in range(1,2*n):
            stars ="*"*i
            spaces=" "*(n-i)
            if i<=n:
                print(stars+spaces+spaces+stars)
            else:
                stars="*"*((2*n)-i)
                spaces=" "*(i-n)
                print(stars+spaces+spaces+stars)

#Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
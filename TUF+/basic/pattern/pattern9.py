#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-9
"""
Pattern 9

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *


Print the pattern in the function given to you.
"""
class Solution:
    def pattern9(self, n):
        for i in range(1,2*n+1):
            if i <=n:
                print(((" ")*(n-i))+(("*" )*(2*i-1))+((" ") *(n-i)))
            else:
                if i>n and i<=2*n:
                    print(((" ")*(i-n-1))+(("*")*(2*(2*n-i)+1))+((" ")*(i-n-1)))

#Time Complexity : O(2*N2). As both functions take O(N2) each.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
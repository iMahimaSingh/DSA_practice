#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-7

"""
Pattern 7
100

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    *
   ***
  *****
 *******
*********


Print the pattern in the function given to you.
"""

class Solution:
    def pattern7(self, n):
        for i in range(1,n+1):
            print( ( " ")*(n-i)+ "*" *(i*2-1)+" "*(n-i))

#Time Complexity : O(N2). As the outer loop runs for N times and the first inner loop runs for(N-1 + N-2 + ... + 1), the second inner loop runs incrementally in each iteration(1 + 3 + 5 + ...+2* N-1). So, overall it is O(N2).

#Space Complexity :O(1). As no extra space is being used to print the patterns.
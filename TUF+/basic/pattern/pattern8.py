#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-8

"""
Pattern 8

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*********
 *******
  *****
   ***
    *


Print the pattern in the function given to you.

"""
class Solution:
    def pattern8(self, n):
        for i in range(n):
            print(" "*i+("*")*(2*n-2*i-1)+" "*i)

#Time Complexity : O(N2). As the outer loop runs for N times and the first inner loop runs for(0 + 1 + 2 + .. + N-1), the second inner loop runs in decreasing manner in each iteration((2*N -1) + (2*N - 3) + ... + 1) . So, overall it is O(N2).

#pace Complexity :O(1). As no extra space is being used to print the patterns.
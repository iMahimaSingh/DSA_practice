#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-12
"""
Pattern 12

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1        1
12      21
123    321
1234  4321
1234554321

Print the pattern in the function given to you.
"""
class Solution:
    def pattern12(self, n):
        for i in range(1,n+1):
            left_side=''
            for j in range(1,i+1):
                left_side+=str(j)
                spaces=" "*(2*n-2*i)
                right_side=""
            for j in range(i,0,-1):
                right_side+=str(j)
            print(left_side+spaces+right_side)
#Time Complexity : O(N2). Where, N is the number of rows provided as an input.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
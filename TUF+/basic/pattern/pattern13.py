#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-13
"""
Pattern 13

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

Print the pattern in the function given to you.
"""
class Solution:
    def pattern13(self, n):
        value=1
        for i in range(1,n+1):#loop runs for 5 times
            for j in range(i,2*i):
                print(value,end=" ")
                value+=1
            print() 

#Time Complexity : O(N2). Where N is the number of rows provided as a input.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
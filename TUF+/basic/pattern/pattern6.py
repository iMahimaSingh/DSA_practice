#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-6

"""
Pattern 6

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



12345

1234

123

12

1



Print the pattern in the function given to you.

"""

class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(1,n-i+1):
                print(j,end="")
            print()

#Time Complexity : O(N2). As the outer loop runs for N times and the inner loop runs in decreasing manner in each iteration(N + (N-1) + (N-2) + ... + 1), which is equal to (N*(N+1)/2). So, overall it is O(N2).

S#pace Complexity :O(1). As no extra space is being used to print the patterns.
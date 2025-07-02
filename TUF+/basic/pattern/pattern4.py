#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-4

"""
Pattern 4

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1

22

333

4444

55555



Print the pattern in the function given to you.


"""
class Solution:
    def pattern4(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end="")
            print()

#Time Complexity : O(N2). As the outer loop runs for N time and the inner loop runs incrementally in each iteration(1+2+3+...+N), which is equal to (N*(N+1)/2). So, overall it is O(N2).

#Space Complexity :O(1). As no extra space is being used to print the patterns.

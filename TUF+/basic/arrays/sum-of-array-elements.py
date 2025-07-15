#https://takeuforward.org/plus/dsa/beginner-problem/basic-arrays/sum-of-array-elements
"""
Sum of Array Elements

Given an array arr of size n, the task is to find the sum of all the elements in the array.

Examples:
Input: n=5, arr = [1,2,3,4,5]
Output: 15
Explanation: Sum of all the elements is 1+2+3+4+5 = 15

Input: n=6, arr = [1,2,1,1,5,1]
Output: 11
Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11
"""
class Solution:
    def sum(self,arr, n): 
        add=0
        for i in range(n):
            add +=arr[i]
        return add
#Time Complexity: O(N) – Array with N elements is traversed, once

#Space Complexity: O(1) – A single variable is used to store the sum, regardless of the array size.
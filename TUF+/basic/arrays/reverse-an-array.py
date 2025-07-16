#https://takeuforward.org/plus/dsa/beginner-problem/basic-arrays/reverse-an-array

"""
Reverse an array
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Examples:
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]

Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Input: n=6, arr = [1,2,1,1,5,1]
Output: [1,5,1,1,2,1]

Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

Input: n=3, arr = [1,2,1]
Output:
[1,2,1]
Constraints:
1 <= n <= 104
1 <= arr[i] <= 105
"""
class Solution:
    def reverse(self, arr, n):
        output=[]
        for i in range(n//2):
            output=arr[i]
            arr[i]=arr[n-i-1]
            arr[n-i-1]=output
        return output

#Time Complexity: O(N), A single-pass of the array with N elements is being done to reverse the array

#Space Complexity: O(1), no extra data structure is being used so no extra space.
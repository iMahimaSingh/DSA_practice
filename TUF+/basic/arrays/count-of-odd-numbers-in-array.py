#https://takeuforward.org/plus/dsa/beginner-problem/basic-arrays/count-of-odd-numbers-in-array

"""
Count of odd numbers in array

Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

Examples:
Input: n=5, array = [1,2,3,4,5]
Output: 3
Explanation: The three odd elements are (1,3,5).

Input: n=6, array = [1,2,1,1,5,1]
Output: 5
Explanation: The five odd elements are one 5 and four 1's.

Input: n=5, array = [1,3,5,7,9]
Output:
5
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104
"""
class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        count=0
        for num in arr:
            if num%2!=0:
                count+=1
        return count
#Time Complexity : O(N)
#Each element in the array has to be inspected once to determine if it's odd, resulting in a linear time complexity where N is the number of elements in the array.

#Space Complexity : O(1)
#The space used is constant, as we only use a single counter regardless of the size of the input array.
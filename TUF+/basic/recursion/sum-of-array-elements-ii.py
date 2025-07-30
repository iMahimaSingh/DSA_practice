#https://takeuforward.org/plus/dsa/beginner-problem/basic-recursion/sum-of-array-elements-ii
"""
Sum of Array Elements
Given an array nums, find the sum of elements of array using recursion.

Examples:
Input : nums = [1, 2, 3]
Output : 6
Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Input : nums = [5, 8, 1]
Output : 14
Explanation : The sum of elements of array is 5 + 8 + 1 => 14.

Constraints:
1 <= n <= 100
1 <= nums[i] <= 100
"""
class Solution:
    def arraySum(self, nums):
       return self.sum_of_array(nums,0)
    def sum_of_array(self,nums,index):
        if (index>=len(nums)):
            return 0
        return nums[index]+self.sum_of_array(nums,index+1)

#T.C:- O(N)
#S.C: O(N)
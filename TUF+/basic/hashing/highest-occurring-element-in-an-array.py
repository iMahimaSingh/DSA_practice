#https://takeuforward.org/plus/dsa/beginner-problem/basic-hashing/highest-occurring-element-in-an-array
"""
Highest Occurring Element in an Array
Given an array of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.

Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!

Examples:
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Input: arr = [4, 4, 5, 5, 6]
Output: 4
Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

Input: arr = [10, 9 ,7]
Output:
7
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104
"""
class Solution:
    def mostFrequentElement(self, nums):
        hashmap: dict[int,int]={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1 
        # set first value   
        max_value=nums[0]
        for key, value in hashmap.items():
            if value > hashmap[max_value]:
                max_value=key
            if  hashmap[key]==hashmap[max_value]:
                max_value=min(key,max_value)
        return max_value

#Using a single loop, performing insertion, updation opertion on HashMap takes O(1) TC resulting in O(N) TC.
#Space Complexity: O(N) – In the worst-case scenario, the HashMap will store all the elements in the array when array elements are unique.
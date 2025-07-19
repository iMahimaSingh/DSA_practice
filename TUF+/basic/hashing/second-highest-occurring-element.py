#https://takeuforward.org/plus/dsa/beginner-problem/basic-hashing/second-highest-occurring-element
"""
Second Highest Occurring Element
Given an array of n integers, find the second most frequent element in it. If there are multiple elements that appear a maximum number of times, find the smallest of them. If second most frequent element does not exist return -1.

Examples:
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 2
Explanation: The number 2 appears the second most (2 times) and number 3 appears the most(3 times). 

Input: arr = [4, 4, 5, 5, 6, 7]
Output: 6
Explanation: Both 6 and 7 appear second most times, but 6 is smaller.

Input: arr = [10, 9 ,7, 7]
Output:
9
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104
"""
class Solution:
    def secondMostFrequentElement(self, nums):

        if len(nums) <2:
            return -1

        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        max_value=-1 
        second_max_value=-1
        max_key=-1
        second_max_key=-1
        for key,value in hashmap.items():
            if value>max_value:
                second_max_value=max_value
                second_max_key=max_key
                max_value=value
                max_key=key
            elif value==max_value:
                max_key=min(max_key, key)
            elif value < max_value:
                if value>second_max_value:
                    second_max_value=value
                    second_max_key=key
                elif value == second_max_value:
                    second_max_key=min(key,second_max_key)
            
        return second_max_key
# class Solution:
#     def secondMostFrequentElement(self, nums):
#         hashmap={
#             -1:0
#         }
#         for num in nums:
#             if num in hashmap:
#                 hashmap[num]+=1
#             else:
#                 hashmap[num]=1

#         max_key=-1
#         second_max_key=-1
#         for key, value in hashmap.items():
#             if value > hashmap[max_key]:
#                 second_max_key=max_key
#                 max_key=key
#             elif value==hashmap[max_key]:
#                 max_key=min(key,max_key)
#             elif value<hashmap[max_key]:
#                 if value>hashmap[second_max_key]:
#                     second_max_key=key
#                 elif value==hashmap[second_max_key]:
#                     second_max_key=min(key,second_max_key)
#         return second_max_key

#Using a single loop, performing insertion, and updation operations on HashMap takes O(1) TC resulting in O(N) TC.
#Space Complexity: O(N) – In the worst-case scenario, the HashMap will store all the elements in the array when array elements are unique.
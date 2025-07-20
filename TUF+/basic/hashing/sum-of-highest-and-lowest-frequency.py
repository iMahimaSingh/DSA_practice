#https://takeuforward.org/plus/dsa/beginner-problem/basic-hashing/sum-of-highest-and-lowest-frequency
"""
Sum of Highest and Lowest Frequency
Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number.

Examples:
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 4
Explanation: The highest frequency is 3 (element 3), and the lowest frequency is 1 (element 1). Their sum is 3 + 1 = 4.

Input: arr = [4, 4, 5, 5, 6]
Output: 3
Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.

Input: arr = [10, 9, 7, 7, 8, 8, 8]
Output:
4
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104
"""
class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        if len(nums)<2:
            return 2
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

        max_freq=0
        min_freq=len(nums)
        
        for value in hashmap.values():
            if value>max_freq:
                max_freq=value
                
            if value<min_freq:
                min_freq=value
        return max_freq+min_freq
#Iterating the array results in O(N) TC. In every iteration, the hashmap is updated, which is a constant time operation. This results in overall O(N) TC.
#Iterating on HashMap, will take O(N) in the worst-case.
#Space Complexity: O(N) – In the worst-case scenario, the HashMap will store all the elements in the array when array elements are unique.
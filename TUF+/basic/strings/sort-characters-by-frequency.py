#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/sort-characters-by-frequency
"""
Sort Characters by Frequency

You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order.

Examples:
Input : s = "tree"
Output : ['e', 'r', 't' ]
Explanation : The occurrences of each character are as shown below :
e --> 2
r --> 1
t --> 1.
The r and t have same occurrences , so we arrange them by alphabetic order.

Input : s = "raaaajj"
Output : ['a' , 'j', 'r' ]
Explanation : The occurrences of each character are as shown below :
a --> 4
j --> 2
r --> 1

Input : s = "bbccddaaa"

Output:
['c', 'a', 'b', 'd']
['c', 'a', 'd', 'b']
['a', 'b', 'c', 'd']
['a', 'b', 'd', 'c']
🎉 Correct! You’ve earned 10 points!
Constraints:
1 <= s.length <= 105
s consist of only lowercase English characters.
"""
class Solution:
    def frequencySort(self, s):
        #your code goes here
        hashmap={}
        for char in s:
            if char in hashmap:
                hashmap[char]+=1
            else:
                hashmap[char]=1

        result=[i for i in hashmap.keys()]

        result.sort(key=lambda item: (-hashmap[item], item))

        return result
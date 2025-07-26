#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/valid-anagram
"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:
Input : s = "anagram" , t = "nagaram"
Output : true

Explanation : We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.
Input : s = "dog" , t = "cat"
output : false
Explanation : We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.

Input : s = "eat" , t = "tea"
Output:
true
Constraints:
1 <= s.length , t.length <= 5*104
s and t consist of only lowercase English letters
"""
class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        if len(s)!=len(t):
            return False
        # return sorted(s)==sorted(t)
        #to store the count of each character
        #optimal code
        frequency=[0]*26
        for char in s:
            frequency[ord(char)-ord('a')] +=1
        for char in t:
            frequency[ord(char)-ord('a')] -=1
        for i in frequency:
            if i!=0:
                return False
           
        return True
    #T.C : O(N) where N is the length of string
    #S.C : O(1) constant size array(length of 26) 

        
            
#https://takeuforward.org/plus/dsa/beginner-problem/basic-recursion/reverse-a-string-i
"""
Reverse a String I
Given an input string as an array of characters, write a function that reverses the string.

Examples:
Input : s = ["h", "e", "l", "l", "o"]
Output : ["o", "l", "l", "e", "h"]
Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Input : s = ["b", "y", "e" ]
Output : ["e", "y", "b"]
Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".

Input : s = ["h", "a", "n", "n", "a", "h"]
Output:
['h', 'a', 'n', 'n', 'a', 'h']
['h', 'n', 'a', 'n', 'a', 'h']
['h', 'n', 'a', 'a', 'n', 'h']
['h', 'a', 'n', 'a', 'n', 'h']

Constraints:
1 <= s.length <= 103
s consist of only lowercase and uppercase English characters.
"""
class Solution:
    def reverseString(self,s):
        #your code goes here
        length_of_string=len(s)
        if length_of_string<1:
            return ""
        if (length_of_string==1):
            return s[0]
        return(s[length_of_string-1]+self.reverseString(s[0:length_of_string-1]))
#T.C: O(N)
#S.C: O(N) 
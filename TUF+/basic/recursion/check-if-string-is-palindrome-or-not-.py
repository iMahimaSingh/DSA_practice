#https://takeuforward.org/plus/dsa/beginner-problem/basic-recursion/check-if-string-is-palindrome-or-not-
"""
Check if String is Palindrome or Not
Given a string s, return true if the string is palindrome, otherwise false.
A string is called palindrome if it reads the same forward and backward.

Examples:
Input : s = "hannah"
Output : true
Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Input : s = "aabbaaa"
Output : false
Explanation : The string when reversed is --> "aaabbaa", which is not same as original string, So we return false.
Constraints:
1 <= s.length <= 103
s consist of only uppercase and lowercase English characters.
"""
class Solution:    
    def palindromeCheck(self, s):
        return self.isPalindrome(s, 0)

    def isPalindrome(self, s, i):
        l=len(s)

        if i==l:
            return True

        if s[i]!=s[l-i-1]:
            return False

        return self.isPalindrome(s, i+1)
#T.C:O(N)
#S.C:O(N)
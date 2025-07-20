#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/palindrome-check
"""
Palindrome Check
You are given a string s. Return true if the string is palindrome, otherwise false. A string is called palindrome if it reads the same forward and backward.

Examples:
Input : s = "hannah"
Output : true
Explanation : The given string when read backward is -> "hannah", which is same as when read forward.
Hence answer is true.

Input : s = "aabbaaa"
Output : false
Explanation : The given string when read backward is -> "aaabbaa", which is not same as when read forward.
Hence answer is false.

Input : s = "aabbccbbaa"
Output:
true
false
Constraints:
1 <= s.length <= 105
s consist of only uppercase and lowercase English characters.
"""
class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        #brute force
        # reverse=s[::-1]
        # if reverse==s:
        #     return True
        #optimal
        # take two pointer to compare the character
        left=0
        right=len(s)-1
        while left <right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

#time complexity O(n)
#space complexity 0(1)

#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/reverse-a-string-ii
"""
Reverse a String II
Given a string, the task is to reverse it. The string is represented by an array of characters s. Perform the reversal in place with O(1) extra memory.

Note: no need to return anything, modify the given list.

Examples:
Input : s = ["h", "e" ,"l" ,"l" ,"o"]
Output : ["o", "l", "l", "e", "h"]
Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Input : s = ["b", "y" ,"e" ]
Output : ["e", "y", "b"]
Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".
"""
class Solution: 
    def reverseString(self, s):
        #your code goes here
        letter_at_left=0
        letter_at_right=len(s)-1
        while letter_at_left<letter_at_right:
            s[letter_at_left],s[letter_at_right]=s[letter_at_right],s[letter_at_left]
            letter_at_left+=1
            letter_at_right-=1
        return s   

#Time Complexity O(N) - Linear time complexity, where n is the length of the string. The algorithm iterates through half of the string.

#SpaceComplexity O(1) - Constant space complexity. The algorithm only uses a few extra variables regardless of the input size.
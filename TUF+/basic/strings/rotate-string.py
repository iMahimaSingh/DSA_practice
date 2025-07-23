#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/rotate-string
"""
Rotate String
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Examples:
Input : s = "abcde" , goal = "cdeab"
Output : true
Explanation : After performing 2 shifts we can achieve the goal string from string s.
After first shift the string s is => bcdea
After second shift the string s is => cdeab.

Input : s = "abcde" , goal = "adeac"
Output : false
Explanation : Any number of shift operations cannot convert string s to string goal.
Input : s = "abcde" , goal = "abcde"
Output:
true
Constraints:
1 <= s.length <= 100
1 <= goal.length <= 100
s and goal consist of only lowercase English letters.
"""
class Solution:    
    def rotateString(self, s, goal):
        #your code goes here
        # for i in range(len(s)):
        #     rotated_string=s[i:]+s[:i]
            
        #     if rotated_string==goal:
        #         return True
            
        # return False

    #optimal Solution
        if len(s)!=len(goal):
            return False

        concatenated_string=s+s
        return goal in concatenated_string
#T.C: O(N)
 #S.C: O(N)        
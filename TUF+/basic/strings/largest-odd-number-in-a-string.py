#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/largest-odd-number-in-a-string
"""
Largest Odd Number in a String
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero.

Examples:
Input : s = "5347"
Output : "5347"
Explanation : The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.
So the largest among all the possible odd numbers for given string is 5347.

Input : s = "0214638"
Output : "21463"
Explanation : The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.
We cannot include 021463 as the number contains leading zero.
So largest odd number in given string is 21463.

Input : s = "0032579"
Output:
"32579"
Constraints:
1 <= s.length <= 103
'0' <= s[i] <= '9'
"""
class Solution:
    def largeOddNum(self, s: str) -> str:
        #write code here
        substring=""
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 != 0:
                substring = s[:i + 1]
                break

        first_digit_index = 0
        while first_digit_index < len(substring) and substring[first_digit_index] == '0':
            first_digit_index += 1
        
        return substring[first_digit_index:]

        return ""
#Time complexity :- O(n)
#space complexity:-O(n)
        
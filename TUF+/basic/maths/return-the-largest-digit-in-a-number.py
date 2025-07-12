#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/return-the-largest-digit-in-a-number
"""
Return the Largest Digit in a Number

You are given an integer n. Return the largest digit present in the number.

Examples:
Input: n = 25

Output: 5

Explanation: The largest digit in 25 is 5.

Input: n = 99

Output: 9

Explanation: The largest digit in 99 is 9.

Input: n = 1

Output:
1
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
"""
class Solution:
    def largestDigit(self, n):
        largest_digit=0
        while n>0:
            last_Digit=n%10
            if last_Digit>largest_digit:
                largest_digit=last_Digit
            else:
                largest_digit=largest_digit
            n //=10
        return largest_digit

#Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

#Space Complexity: O(1) – Using a couple of variables i.e., constant space.
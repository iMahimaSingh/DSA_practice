#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/palindrome-number

"""
Palindrome Number

You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.

A palindrome number is a number which reads the same both left to right and right to left.

Examples:
Input: n = 121

Output: true

Explanation: When read from left to right : 121.

When read from right to left : 121.

Input: n = 123

Output: false

Explanation: When read from left to right : 123.

When read from right to left : 321.

Input: 101

Output:
true

Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
"""

class Solution:
    def isPalindrome(self, n):
        original_number=n
        reverse_number=0
        while n>0:
            lastDigit=n%10
            reverse_number=(reverse_number*10)+lastDigit
            n//=10
        if reverse_number==original_number:
            return True
        else:
            return False

#Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

#Space Complexity: O(1) – Using a couple of variables i.e., constant space.
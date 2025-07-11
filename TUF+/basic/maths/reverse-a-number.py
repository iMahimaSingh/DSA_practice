#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/reverse-a-number
"""
Reverse a number

You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

Examples:
Input: n = 25

Output: 52

Explanation: Reverse of 25 is 52.

Input: n = 123

Output: 321

Explanation: Reverse of 123 is 321.

Input: n = 54

Output:
45

Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
"""
class Solution:
    def reverseNumber(self, n):
        # nums=str(n)
        # for digits in nums:
        #     if digits==0:
        #         return 0
        #     elif digits ==1:
        #         return 1
        # else:
        #     reverse_number=nums[-1::-1]
        #     return int(reverse_number)
        
        reverse_number=0
        while n>0:
            last_digit=n%10
            reverse_number=(reverse_number*10)+(last_digit)
            n//=10
        return (reverse_number)

#Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

#Space Complexity: O(1) – Using a couple of variables i.e., constant space.
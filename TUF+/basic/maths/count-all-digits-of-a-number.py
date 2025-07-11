# https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/count-all-digits-of-a-number

"""
Divisors of a Number

You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.

A number which completely divides another number is called it's divisor.

Examples:
Input: n = 6

Output = [1, 2, 3, 6]

Explanation: The divisors of 6 are 1, 2, 3, 6.

Input: n = 8

Output: [1, 2, 4, 8]

Explanation: The divisors of 8 are 1, 2, 4, 8.
"""
class Solution:
    def divisors(self, n):
        number=[]
        for i in range(1,n+1):
            if n%i==0:
                number.append(i)
        return number
#Time Complexity: O(N) – Iterating N times, and performing constant time operations in each pass.

#Space Complexity: O(sqrt(N)) – A number N can have at max 2*sqrt(N) divisors, which are stored in the array.
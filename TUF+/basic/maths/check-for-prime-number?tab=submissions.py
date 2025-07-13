#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/check-for-prime-number?tab=submissions
"""
Check for Prime Number
You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.

A prime number is a number which has no divisors except 1 and itself.

Examples:
Input: n = 5

Output: true
Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Input: n = 8
Output: false

Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.
"""
import math

class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

#Time Complexity: O(sqrt(N)) – Looping sqrt(N) times to find the count of all divisors of N.

#Space Complexity: O(1) – Using a couple of variables i.e., constant space.
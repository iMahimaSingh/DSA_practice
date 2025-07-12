#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/factorial-of-a-given-number-i

"""
Factorial of a given number
You are given an integer n. Return the value of n! or n factorial.

Factorial of a number is the product of all positive integers less than or equal to that number.

Examples:
Input: n = 2

Output: 2

Explanation: 2! = 1 * 2 = 2.

Input: n = 0

Output: 1

Explanation: 0! is defined as 1.

Input: 3

Output:
6
Constraints:
0 <= n <= 10
"""
class Solution:
    def factorial(self, n):
        output=1
        for i in range(1,n+1):
            output *=i
        return output

#Time Complexity: O(N) – Iterating once from 1 to N.

#Space Complexity: O(1) – Using a couple of variables i.e., constant space.
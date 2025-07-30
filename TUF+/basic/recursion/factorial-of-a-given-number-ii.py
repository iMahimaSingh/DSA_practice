#https://takeuforward.org/plus/dsa/beginner-problem/basic-recursion/factorial-of-a-given-number-ii
"""
Factorial of a Given Number
Given an integer n, return the factorial of n.
Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).

Examples:
Input : n = 3
Output : 6
Explanation : Factorial = 1 * 2 * 3 => 6

Input : n = 5
Output : 120
Explanation : Factorial = 1 * 2 * 3 * 4 * 5 => 120

Input : n = 4
Output:
24
Constraints:
0 <= n <= 15
"""
class Solution:
    def factorial(self, n):
        if(n==0 or n==1):
            return 1
        return(self.factorial(n-1)*n)
#T.C:O(N)
#S.C:O(N)
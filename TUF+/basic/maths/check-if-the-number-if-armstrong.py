#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/check-if-the-number-if-armstrong
"""
Check if the Number is Armstrong
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Examples:
Input: n = 153

Output: true

Explanation: Number of digits : 3.

13 + 53 + 33 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.

Input: n = 12

Output: false

Explanation: Number of digits : 2.

12 + 22 = 1 + 4 = 5.

Therefore, it is not an Armstrong number.
"""
class Solution:
    def isArmstrong(self, n):
        input_n=str(n)
        length=len(input_n)
        output=0
        for digits in input_n:
            output +=int(digits)**length
        return output==n

#Time Complexity: O(log10(N)) – N is being divided by 10 until it becomes zero resulting in log10(N) iterations and in each iteration constant time operations are performed.

#Space Complexity: O(1) – Using a couple of variables i.e., constant space, regardless of the size of the input.
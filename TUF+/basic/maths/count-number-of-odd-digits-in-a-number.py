#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/count-number-of-odd-digits-in-a-number
"""
Count number of odd digits in a number

You are given an integer n. You need to return the number of odd digits present in the number.

The number will have no leading zeroes, except when the number is 0 itself.

Examples:
Input: n = 5

Output: 1

Explanation: 5 is an odd digit.

Input: n = 25

Output: 1

Explanation: The only odd digit in 25 is 5.

Input: n = 15

Output:
2
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
"""
class Solution:
    def countOddDigit(self, n):
        count=0
        nums=str(n)
        for digits in nums:
            if int(digits)%2!=0:
                count+=1
        return count

#Time Complexity: O(log10(N)) – In every iteration we are dividing N by 10 (equivalent to the number of digits in N).

#Space Complexity: O(1) – Using only couple of variables i.e., constant space.

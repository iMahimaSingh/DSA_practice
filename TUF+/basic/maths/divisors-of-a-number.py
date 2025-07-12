#https://takeuforward.org/plus/dsa/beginner-problem/basic-maths/divisors-of-a-number

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

Input: n = 7

Output:
[1, 7]
Constraints:
1 <= n <= 1000
"""
import math
class Solution:
    def divisors(self, n):
#Brute solution
        # number=[]
        # for i in range(1,n+1):
        #     if n%i==0:
        #         number.append(i)
        # return number
            
  # optimal solution:-
        numbers=[]  
        square_rootN=int(math.sqrt(n))
        
        for i in range(1,square_rootN+1):
            if n%i==0:
                numbers.append(i)
                if i!=n//i:
                    numbers.append(n//i) 
        numbers.sort() 
        return numbers        
#Time Complexity: O(sqrt(N)) + O(K*Log(K)) – Iterating sqrt(N) times, and performing constant time operations in each pass to get all the divisors in the list. Sorting the list of divisors takes O(K*Log(K)) time where K is the number of divisors of the number.

#Space Complexity: O(sqrt(N)) – A number N can have at max 2*sqrt(N) divisors, which are stored in the array.
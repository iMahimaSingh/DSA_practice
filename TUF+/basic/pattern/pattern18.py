#https://takeuforward.org/plus/dsa/beginner-problem/patterns/pattern-18
"""
Pattern 18

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

E 
D E 
C D E 
B C D E 
A B C D E

Print the pattern in the function given to you.
"""
class Solution:
    def pattern18(self, n):
        for i in range(1,n+1):
            char='A'
            letter_first=chr(ord(char)+n-i)
            
            for j in range(1,i+1):
                print(letter_first,end=" ")
                letter_first=chr(ord(letter_first)+1)
            print()

#Time Complexity : O(N2). The overall complexity will be O(N2) due to the nested loops, where N is the number of rows.

#Space Complexity :O(1). As no extra space is being used to print the patterns.
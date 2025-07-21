#https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/isomorphic-string
"""
Isomorphic String
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Examples:
Input : s = "egg" , t = "add"
Output : true
Explanation : The 'e' in string s can be replaced with 'a' of string t.
The 'g' in string s can be replaced with 'd' of t.
Hence all characters in s can be replaced to get t.

Input : s = "apple" , t = "bbnbm"
Output : false
Explanation : It can be proved that no solution exists for this example.
All the "b"s in t have to take places of "a", "p", "l", which requires "p" to be mapped to "b", but that makes it impossible for "p" at index 2 (0-indexed) to become "n". Thus no solution exists.

Input : s = "paper" , t = "title"
Output:
true
Constraints:
1 <= s.length <= 103
s.length == t.length
s and t consist of only lowercase English letters.
"""
class Solution:
    def isomorphicString(self, s, t):
        hm={}
        l=len(s)
        for i in range(l):
            if s[i] not in hm:
                # make sure t[i] is not already mapped to some other character before mapping it to s[i]
                if t[i] in hm.values(): 
                    return False
                hm[s[i]]=t[i]
            else:
                # t[i] must be equal to hm['g'], if not then it is not isomorphic
                if t[i] != hm[s[i]]:
                    return False
            
        return True

            
# TC: O(n+k), k=26 ~ O(n)
# SC: O(k), k= constant, max=26 ~ O(1)
            
            


        
        
        

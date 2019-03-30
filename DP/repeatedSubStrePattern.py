https://leetcode.com/problems/repeated-substring-pattern/

https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination

The explanation for why that works is pretty straight forward.

Consider a string S="helloworld". Now, given another string T="lloworldhe",
 can we figure out if T is a rotated version of S? Yes, we can! We check if
  S is a substring of T+T.

Fine. How do we apply that to this problem? We consider every rotation of
 string S such that it's rotated by k units [k < len(S)] to the left.
  Specifically, we're looking at strings "elloworldh", "lloworldhe", 
  "loworldhel", etc...

If we have a string that is periodic (i.e. is made up of strings that 
    are the same and repeat R times), then we can check if the string 
is equal to some rotation of itself, and if it is, then we know that the
 string is periodic. Checking if S is a sub-string of (S+S)[1:-1] basically 
 checks if the string is present in a rotation of itself for all values of 
 R such that 0 < R < len(S).

!!!
if s1 contains repeating blocks

abcabcabc     abc is a repeating block

abababab      ab and abab is a repeating block

abc   abc is a repeating block

we can get s1 by itself via ratate to left a repeating block size

so if s2 is a rotated version of s1, and s2 == s2,
as long as its rotation size is 
< len(s1), it must has repeating block, rotation size = repeating block size

if s2 in s1 + s1 (s2 s1 same size), then s2 is rotated version of s1

and as long as rotation index does not equal to 0 or len(s1), it has repeating
block

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not str:
            return False
        newS = s + s
        #search from index 1 to make sure we have rotation index > 0
        rotationIndex = newS.find(s, 1)
        #as long as rotation index != len(s), it has repeating block
        return rotationIndex != len(s)


        
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not str:
            return False
        newS = s + s
        #remove first char to make sure the rotation index > 0
        newS = newS[1:]
        foundIndex = newS.find(s)
        #baaba
        rotationIndex = foundIndex + 1
        #as long as rotation index != len(s), it has repeating block
        return rotationIndex != len(s)

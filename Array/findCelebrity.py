https://leetcode.com/problems/find-the-celebrity/
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


# We are sure that if A knows B, A cannot be the celebrity while B may be,
#  i.e., B is the candidate. Since there is only one celebrity, one loop is enough to decide the candidate.

# however, being largest not = be the celebrity, we need to verify it

class Solution(object):
    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            #if cadidate know anyone, we invalid
            if knows(candidate, i):
                candidate = i
        #print candidate
        #we have a potentail winner know, we check if he does not know anyone and everyone knows he
        for i in range(n):
            if i == candidate:
                continue
            #if someone not know candidate, or candidate know some one
            #we invalid it
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate

    #practice 
    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate



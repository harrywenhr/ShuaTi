#https://leetcode.com/problems/insert-delete-getrandom-o1/
import random

class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            idx = self.pos[val] # get val index in list
            last = self.nums[-1] # get the last addition
            self.nums[idx] = last # overwrite val index with last addition
            self.pos[last] = idx # update the last addition's index to it's new spot
            self.nums.pop() # get rid of the last addition from it's original spot...it now has a new home elsewhere
            del self.pos[val] # original line was "self.pos.pop(val, 0)". we don't need pop-or-default semantics here, del will work
            return True
        return False
            
    def getRandom(self):
        return random.choice(self.nums)
#practiced

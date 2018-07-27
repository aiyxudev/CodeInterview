#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:31:53 2018

@author: admin
"""

class Stack:

    def __init__(self):
        """
        initialize stack data structure as Array
        """
        self.p = []
        
    def isEmpty(self):
        """
        check if the stack is empty
        rtype: boolean
        """
        return len(self.p) == 0
        

    def push(self, x):
        """
        push x into the stack
        :rtype: void
        """
        self.p.append(x)

    def pop(self):
        """
        Removes the element on top of the stack
        :rtype: void
        """
        self.p.pop()
    
    def top(self):
        """
        get the top element
        rtype: int 
        """
        if self.isEmpty(): 
            return None
        return self.p[-1]
  
'''
Implement stack using queue in Python
'''
class Solution: 
    def __init__(self):
        self._queue = collections.deque() #Returns a new deque object initialized left-to-right

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft()) #Remove and return an element from the left side of the deque
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue) 
        

        
if __name__ == "__main__":

    nums = [1,3,-1,-3,5,3,6,7] 
    k = 3 
    s = Solution()
    print(s.maxSlidingWindow(nums, k)) # [3,3,5,5,6,7]
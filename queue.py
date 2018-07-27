#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:32:05 2018

@author: admin
"""

class Queue: 
    
    def __init__(self,k):
        self.front = self.size = 0 
        self.rear = k -1 
        self.q = [None]*k 
        self.k = k
        
    def isEmpty(self):
        return self.size == 0
    
    
    def EnQueue(self,item):
        self.rear = (self.rear+1) % (self.k)
        self.q[self.rear] = item 
        self.size = self.size + 1
    
    
    def DeQueue(self):
        print("%s dequeued from queue" %str(self.q[self.front]))
        self.front = (self.front+1) % (self.k)
        self.size = self.size -1
    
    def Front(self):
        return self.q[self.front]
    
    
    def Rear(self):
        return self.q[self.rear]
        
        
        
if __name__ == '__main__':
    q = Queue(5)
    q.EnQueue(0)
    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)
    q.EnQueue(4)
    q.DeQueue()
    q.DeQueue()
    print(q.Front())
    print(q.isEmpty())
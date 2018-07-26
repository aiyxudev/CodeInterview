#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:38:49 2018

@author: admin
"""

class Node: 
    # create container
    def __init__(self, data):
        self.data = data;
        self.next = None; 
        
class LinkedList: 
    def __init__(self):
        self.head = None
    
    
    def traversal(self):
        temp = self.head 
        while(temp):
            val = temp.data
            print(val)
            temp = temp.next
            
    #add a node at the front
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node;
        
    # insert node after the current node    
    def insert(self, prev_node, new_data):
        new_node = Node(new_data)  
        new_node.next = prev_node.next  
        prev_node.next = new_node
        
    def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # 6. Change the next of last node
        last.next =  new_node
    
    
    def delete(self, key):
        #1) Find previous node of the node to be deleted.
        temp = self.head    
        while(temp is not None):
            if (temp.data == key):
                break   # use break instead of return??
            prev = temp
            temp = temp.next
        #2) Changed next of previous node
        prev.next = temp.next
        #3) Free memory of the node
        temp = None
        

    def removeNthFromEnd(self, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #find the prev node of the target node 
        
        dummy = Node(0)
        fast = dummy 
        slow = dummy 
        dummy.next = self.head
        
        for i in range(0,n):
            fast = fast.next 
            
        while( fast.next is not None):
            fast = fast.next
            slow = slow.next 
        slow.next = slow.next.next 
        
        return slow, fast, dummy
        
    # i don't understand pointer point to different thing but when they return they
    # are the same
    
    def rotateRight(self,k):
        
        
        # create a circle
        llen = 0
        fast =  self.head 
        slow = self.head
        
        while( fast.next is not None):
            fast = fast.next #5
            llen += 1
        
        #move the circle len - l % len time
        for i in range(0, llen - k % llen):
            slow = slow.next 
        
        #print( "slow is" + str(slow.data))
        fast.next = self.head
        self.head = slow.next
        slow.next = None
        
        return self.head
       
    
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    
    #llist.removeNthFromEnd(2)
    llist.rotateRight(2);
    llist.traversal()
    
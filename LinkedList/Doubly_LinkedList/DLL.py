from typing import List
class Node:
    def __init__(self,val,next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def convert_array_to_dll(self,arr: List[int]):
        self.head = Node(arr[0])
        prev = self.head
        for val in arr[1:]:
            new_node = Node(val)
            prev.next = new_node
            new_node.prev = prev
            prev = new_node

    def insert_at_position(self,val,pos):
        pass

    def print_ll(self):
        curr = self.head
        while curr:
            print(curr.val," -> ", end=" ")
            curr = curr.next
        print("None")

ll = DoublyLinkedList()
ll.convert_array_to_dll([1,2,3,4,5])
ll.print_ll()
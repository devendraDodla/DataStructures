class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_position(self,val,pos):
        if(pos == 1):
            if self.head is None:
                node = Node(val)
                self.head = node
                self.tail = node
                return
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        elif(pos == -1):
            if self.tail is None:
                node = Node(val)
                self.head = node
                self.tail = node
                return
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node
        else:
            pass
    def del_head(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    def del_tail(self):
        if(self.tail is None):
            return 
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            # Remove the tail node
            current.next = None
            self.tail = current
    def remove_ele_based_on_pos(self,pos):
        if(pos == 1):
            self.del_head()
        elif(pos == -1):
            self.del_tail()
        else:
            c = 1
            current = self.head
            prev = None
            while current:
                if(c == pos):
                    prev.next = prev.next.next
                c += 1
                prev = current
                current = current.next
    def remove_ele_based_on_val(self,val):
        current = self.head
        prev = None
        while current:
            if(current.val == val):
                prev.next = prev.next.next
            prev = current
            current = current.next
    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.val,"-> ", end=" ")
            temp = temp.next
        print("None")
ll = LinkedList()
ll.insert_at_position(3,1)
ll.insert_at_position(2,1)
ll.insert_at_position(1,1)
ll.insert_at_position(4,-1)
ll.print_ll()
# ll.del_head()
# ll.del_tail()
# ll.print_ll()
# ll.remove_ele_based_on_pos(2)
ll.remove_ele_based_on_val(4)
ll.print_ll()
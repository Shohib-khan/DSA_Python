# WAP TO CREATE A SINGLE LINKED LIST INSIDE A STACK A STACK DATA STRUCTURE

class Node:
    def __init__(self,val):
        self.data = val
        self.addr = None

class Stack_linked_list:
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.addr = self.head
            self.head = newNode

    def pop(self):
        pass

    def display(self):
        if self.head is None:
            print("No elements to display")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.addr
            print()

    def peek(self):
        if self.head is None:
            print("No elements to peek")
        else:
            print(self.head.data)

sll = Stack_linked_list()
sll.push(10)
sll.push(20)
sll.push(30)
sll.display()
sll.peek()
# Design Linked List

# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, 
# and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the 
# linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new 
# node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the 
# length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the 
# node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.



class MyLinkedList:

    def __init__(self):
        self.list = []

    def get(self, index: int) -> int:
        if index < len(self.list):
            return self.list[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.list.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.list.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == len(self.list):
            self.list.append(val)
        elif index > len(self.list):
            return
        else:
            self.list.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.list):
            self.list.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
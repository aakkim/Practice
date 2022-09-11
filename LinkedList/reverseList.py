# Reverse Linked List (REVIEW RECURSION)

# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list
from array import array
from tkinter import N


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative T O(n) M 0(1) - we are only using two pointers, no data structures
class Solution():
    def reverseList(self, head:ListNode) -> ListNode:    
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

head = [1,2,3,4,5]
x = Solution()
print(x.reverseList(head))


# OR


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive T O(n) M 0(n) - need extra memory for recursive both time and space are linear
class Solution():
    def reverseList(self, head:ListNode) -> ListNode:
        if not head: # base case
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

# Two-branch recursive algorithm
def mergeSort(arr, s, e): # array, start, end indices
    if e-s+1 <= 1: # check if we are at the base case, if the length of the array is less than or equal to 1
        return arr
    
    m = (s+e)/2 # get middle index of array
    mergeSort(arr,s,m) # sort the left half
    mergeSort(arr,m+1,e) # sort the right half

    merge(arr,s,m,e) # merge the sorted halves (first half start at s end at m, second half start at m and end at e)

    return arr
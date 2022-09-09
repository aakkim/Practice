# Design Browser History

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in 
# the history number of steps or move forward in the history number of steps.
# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, 
# you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and 
# steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        # init history as a doubly linked list pointing to homepage
        self.history = ListNode(self.homepage)

    def visit(self, url: str) -> None:
        # add to (next) history the new url
        # set next to None
        self.history.next = ListNode(url, prev=self.history, next=None)
        # move where history points one step to right
        self.history = self.history.next

    def back(self, steps: int) -> str:
        curr = self.history
        while steps > 0 and curr.prev:  # check if there's some history
            curr = curr.prev            # move backward 
            steps -= 1        
        self.history = curr             # move history pointer to new position
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.history
        while steps > 0 and curr.next:
            curr = curr.next            # move forward through history
            steps -= 1
        self.history = curr             # move history pointer to new position
        return curr.val
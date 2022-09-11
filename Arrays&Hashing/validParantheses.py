# Valid Parentheses (REVIEW)

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# use stack and hashmap
class Solution:
    def isValid(self, s: str) -> bool: # O(n) in time and in memory complexity
        stack = []
        closeToOpen = { ')':'(', ']':'[', '}':'{' } # keys are the closing brackets in the hashmap. closing maps to opening
        
        for i in s:
            if i in closeToOpen: #if this is a closing parentheses
                # if stack is not empty and the top value in the stack is a matching opening parentheses 
                if stack and stack[-1] == closeToOpen[i]: 
                    stack.pop() #if it is a match, we got the match so pop parentheses
                else:
                    return False # if stack empty or not matching
            else:
                stack.append(i)
        return True if not stack else False # return True if stack is empty, else return False

s = '()[]{{}}'
x = Solution()
print(x.isValid(s))
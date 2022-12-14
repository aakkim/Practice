# Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        newArray = []
        for i in range(n):
            newArray.append(nums[i])
            newArray.append(nums[n+i])
        return newArray
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftof = []
        running = 1
        for x in nums:            # walk left to right
            leftof.append(running)
            running *= x

        rightof = []
        running = 1
        for x in reversed(nums):  # walk right to left
            rightof.append(running)
            running *= x
        rightof.reverse()         # built back-to-front, flip it

        product = []
        for i in range(len(nums)):
            product.append(leftof[i] * rightof[i])
        return product

        
        

        
        

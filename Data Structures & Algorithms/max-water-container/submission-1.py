class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        maxarea = 0
        for height in range(len(heights)):
            for height2 in range(len(heights)):
                width =  height2 - height
                if width <= 0:
                    continue
                lowest = min(heights[height], heights[height2])
                area = lowest * width
                if area > maxarea:
                    maxarea = area

        return maxarea
        """
        


        left = 0
        right = len(heights) - 1
        highest = 0
        for i in range(len(heights)):
            width = right - left
            high = max(heights[left], heights[right])
            low = min(heights[left], heights[right])
            if low * width > highest:
                highest = low * width
            
            if heights[left] == low:
                left += 1
            if heights[right] == low:
                right -= 1

        return highest 




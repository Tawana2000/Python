# Write a function to find the area of the largest rectangle that can be formed in a histogram.

def largestRectangleArea(heights):
    stack, max_area = [], 0
    for i in range(len(heights) + 1):
        h = 0 if i == len(heights) else heights[i]
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))

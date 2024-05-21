def maxArea(height):
    ans = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return ans


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

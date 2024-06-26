def threeSum(nums):
    ans = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1]:
            continue

        left, right = index + 1, len(nums) - 1
        while left < right:
            threeSum = value + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                ans.append([value, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]))

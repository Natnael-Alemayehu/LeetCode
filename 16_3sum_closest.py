def threeSumClosest(nums, target):
    nums.sort()
    distance = float("inf")

    for index in range(len(nums) - 2):
        left, right = index + 1, len(nums) - 1
        new_target = target - nums[index]

        while left < right:
            sum_val = nums[left] + nums[right]

            if abs(distance) > abs(new_target - sum_val):
                distance = new_target - sum_val

            if sum_val == new_target:
                return target
            elif sum_val < new_target:
                left += 1
            else:
                right -= 1

    return target - distance

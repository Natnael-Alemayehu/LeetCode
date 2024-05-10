# This will me the starting first leetcode challenge for May 10 

def main():
    l = [3,2,4]
    print(twoSum(nums=l, target=6))

def twoSum(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                output.append(i)
                output.append(j)
    return output
main()
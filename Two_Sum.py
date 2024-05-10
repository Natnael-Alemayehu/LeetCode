# This will me the starting first leetcode challenge for May 10 

def main():
    l = [3,2,4]
    print(twoSum_n(nums=l, target=6))

def twoSum_n2(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                output.append(i)
                output.append(j)
    return output

# This is the best solution for this problem. It uses hashmap which is pair_index in this solution
def twoSum_n(nums,target):
    pair_index = {}
    
    for i, num in enumerate(nums):
        if target-num in pair_index:
            return [i, pair_index[target-num]]
        pair_index[num] = i
    
main()
# Question -> Givien an array of values, design a data structure that can query the sum of a subarray of the values

class PrefixSum:
    def __init__(self,nums): # O(n)
        self.prefix = [ ]
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right): # O(1)
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0 # ensures we dont go out of bounds
        return (preRight - preLeft)

# 303. Range Sum Query - Immutable

class NumArray(object):
    def __init__(self,nums):
        self.prefix = [ ]
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
    def sumRange(self, left, right):
        if right > len(self.prefix):   
            return 0
        return self.prefix[right] - self.prefix[left - 1] if left > 0 else self.prefix[right]

# 724. Find Pivot Index
# pivot index -> index where the sum of all the numbers strictly to the left is equal to sum strictly to the right

class Solution(object):
    def sumRange(self, left, right,prefix):
        if right > len(prefix):   
            return 0
        return prefix[right] - prefix[left - 1] if left > 0 else prefix[right]

    def pivotIndex(self, nums):
        prefix_sum = [ ]
        total = 0
        for num in nums:
            total += num
            prefix_sum.append(total)
        pivot = 0
        for pivot in range(0,len(nums)):
            if Solution.sumRange(self,0,pivot,prefix_sum) == Solution.sumRange(self,pivot,len(nums)-1,prefix_sum):
                return pivot
        return -1


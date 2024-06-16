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



from typing import List
class TwoSum:
    def findTarget(self, nums: List[int], target: int) -> List[int]:
        indices={}
        for i, n in enumerate(nums):
            diff = target- n 
            if diff in indices:
                return [indices[diff], i]
            indices[n]=i
        return []
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the target value: "))
obj = TwoSum()
result = obj.findTarget(nums, target)
print("Indices of two numbers:", result)   
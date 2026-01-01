from typing import List
class ContainsDuplicate:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False
number=int(input("Enter number of elements: "))
nums = []
for i in range(number):
    n=int(input(f"Enter element{i+1}: "))
    nums.append(n)
obj=ContainsDuplicate()
print(obj.hasDuplicate(nums))
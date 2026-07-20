class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        for x in nums:
            if nums.count(x)>1:
                flag=True
        return flag
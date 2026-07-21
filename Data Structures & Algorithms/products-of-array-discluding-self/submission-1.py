class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            product=1
            for num in nums[:i]+nums[i+1:]:
                product*=num
            res.append(product)
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}
        for num in nums:
            if num in group.keys():
                group[num]=group.get(num,0)+1
            else:
                group[num]=1
        keys=sorted(group,key=group.get)
        return keys[-k:]
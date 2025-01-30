class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]>=(n/2):
                return i

        
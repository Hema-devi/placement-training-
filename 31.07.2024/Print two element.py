class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                max_pro.append((nums[i]-1)*(nums[j]-1))
        return max(max_pro)

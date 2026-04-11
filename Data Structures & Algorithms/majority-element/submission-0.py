class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count =0
        l=0
        k=len(nums) 
        for i in nums:
            if count==0:
                l=i
            if l!=i:
                count-=1
            else:
                count+=1
            if count >k/2:
                return l
        return l
            
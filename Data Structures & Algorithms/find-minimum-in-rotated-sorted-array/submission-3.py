class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        print(nums)
        mn=nums[0]
        if nums[l]<nums[r]:
            return nums[0]
        while l<=r:
                mid=(r+l)//2
                print(l,r,mid)
                if nums[mid]>nums[r]:
                    mn=min(mn,nums[r])
                    l=mid+1
                elif nums[mid]>nums[l]:
                    mn=min(mn,nums[l])
                    r=mid-1
                else:
                    if l+1==mid or l==mid:
                        return nums[mid]
                    else:
                        l+=1
                        r-=1
        return 0
class Solution:
    def findMin(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[r]:
                r=mid
            elif nums[mid]>nums[r]:
                l=mid+1
        return nums[r]

if __name__ == '__main__':
    seq=[3,4,5,6,1,2]
    print(Solution().findMin(seq))
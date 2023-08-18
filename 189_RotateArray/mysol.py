# Same logic could be done by using the reverse function from list, in this solution I reverse the list usign for loop.
# Other interesting solution would be nums[:] = nums[-k:] + nums[:-k] and k%=len(nums)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=0
        m=k%len(nums)
        for i in range((len(nums)-m)//2):
            nums[i], nums[(len(nums)-1-m)-i]=nums[(len(nums)-1-m)-i], nums[i]
        for j in range((len(nums)-m), (len(nums)-m)+(len(nums)-(len(nums)-m))//2):
            nums[j], nums[(len(nums)-1)-c]=nums[(len(nums)-1)-c], nums[j]
            c+=1
        print(nums)
        for n in range(len(nums)//2):
            nums[n], nums[-(n+1)]=nums[-(n+1)], nums[n]
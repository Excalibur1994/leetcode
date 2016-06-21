class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buf_dict={}
        for n in range(len(nums)):
            if nums[n] in buf_dict:
                return [buf_dict[nums[n]],n]
            else:
                buf_dict[target-nums[n]]=n

test = Solution()
print test.twoSum([1,1,5,3,1], 8)

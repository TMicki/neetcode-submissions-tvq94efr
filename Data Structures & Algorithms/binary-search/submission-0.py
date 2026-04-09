class Solution:
    def search(self, nums: List[int], target: int) -> int:
        t = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return t
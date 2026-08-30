class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
        #     highest = nums[i] + (nums[len(nums)-1])
        #     if highest < target: # go next if current can't add higher than target
        #         continue
            for j in range(i + 1, len(nums)):
                cur = nums[i] + nums[j]
                if cur == target:
                    return [i, j]

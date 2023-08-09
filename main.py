class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_side = 0
        right_side = len(nums) - 1
        middle = 0
        
        while left_side < right_side :
            middle = left_side + (right_side - left_side) // 2

            if target <= nums[middle] :
                right_side = middle
            else :
                left_side = middle + 1

        if target == nums[right_side] :
            return right_side
        else :
            return -1
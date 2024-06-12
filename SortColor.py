class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize three pointers
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap the elements at low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move mid pointer to the right
                mid += 1
            else:
                # Swap the elements at mid and high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
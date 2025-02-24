def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target:
            right = pivot - 1
        elif nums[pivot] < target:
            left = pivot + 1
    return None


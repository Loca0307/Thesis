







#Sol:2
# Below code seems to be simplified and generate by chatgpt
# def singleNonDuplicate(nums):
#     # Initialize start and end pointers
#     start = 0
#     end = len(nums) - 1

#     # Binary search
#     while start < end:
#         # Find the mid index
#         mid = start + (end - start) // 2

#         # Ensure mid is even for proper pair checking
#         if mid % 2 == 1:
#             mid -= 1

#         # Check the pair condition
#         if nums[mid] == nums[mid + 1]:
#             # If mid and mid+1 are equal, single element is in the right half
#             start = mid + 2
#         else:
#             # Otherwise, the single element is in the left half
#             end = mid

#     # When start == end, the single element is found
#     return nums[start]

# 
# nums = [1, 1, 3, 3, 4, 4, 5, 8, 8]
# print("Single element:", singleNonDuplicate(nums))

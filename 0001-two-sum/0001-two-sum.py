class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the index of elements
        seen = {}
        
        # Iterate over the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in seen, return the indices
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the number and its index
            seen[num] = i

# Example Usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))   # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]

        
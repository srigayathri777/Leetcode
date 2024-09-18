from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Custom comparator to sort based on which concatenation is larger
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        # Convert the numbers to strings
        nums_str = list(map(str, nums))
        
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # If the first number is '0', return '0' (all are zeros)
        if nums_str[0] == '0':
            return '0'
        
        # Join all strings to form the largest number
        return ''.join(nums_str)

# Example Usage:
solution = Solution()
print(solution.largestNumber([10, 2]))        # Output: "210"
print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"



        
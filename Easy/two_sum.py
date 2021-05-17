# Two Sum
# Given an array of integer numbers and an integer target, return indices of the two numbers such that they add up to target.

# Constraints:
# 1. Only one valid answer exists.
# 2. May not use the same element twice.

def calculate_two_sum(nums, target):
    new_nums = []

    print("Target value: {}".format(target))
    print("Full list: {}".format(nums))

    # First, reduce computational complexity by eliminating values that are larger than the target
    for current_value in nums:
        if current_value < target:
            new_nums.append(current_value)

    print("Reduced list: {}".format(new_nums))

    # Second, iterate through the lists to find the first pair that sum to the target value
    for i, compare_i in enumerate(new_nums):
        for j, compare_j in enumerate(new_nums):
            if i == j:
                pass
            elif compare_i + compare_j == target:
                return [compare_i, compare_j]

if __name__ == "__main__":
    nums = [1,5,2,7,11,15]
    target = 9

    two_sum = calculate_two_sum(nums, target)
    print("Calculated two-sum: {}".format(two_sum))
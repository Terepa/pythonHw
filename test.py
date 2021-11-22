
def dist_closest(nums, n):
    difference = 10 ** 20
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(nums[i] - nums[j]) < difference:
                difference = abs(nums[i] - nums[j])
    return difference


numbers = [123, 56, 709, 98, 42, 64, 99, -123, 510]
n = len(numbers)
print("Minimum difference is " + str(dist_closest(numbers, n)))


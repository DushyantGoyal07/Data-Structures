# Find the Missing Number

arr = [1,3,4]
n = len(arr)
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
print(expected_sum - actual_sum)
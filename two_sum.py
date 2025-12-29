arr = [3,5,8,11,15]
target = 13
left = 0
right = len(arr) - 1

while left<right:
    sum = arr[left] + arr[right]

    if sum == target:
        result = [arr[left], arr[right]]
        break
    elif sum < target:
        left += 1
    else:
        right -= 1

print(result)
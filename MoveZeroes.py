# Move all Zeroes at the End

arr = [3,2,0,5,0,1,0]
# Expected = [3,2,5,1,0,0,0]
left = 0
right = len(arr)-1

while(left<right):
    if arr[left] != 0:
        left += 1
    elif arr[right] == 0:
        right -= 1
    else:
        arr[left], arr[right] = arr[right], arr[left]

print(arr)
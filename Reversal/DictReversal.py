# Program to Reverse a Dictionary
arr = {'1':'a', '2': 'b', '3':'c'}

# Manually

# arr = list(arr.items())
# left = 0
# right = len(arr) - 1

# while(left<right):
#     temp = arr[left]
#     arr[left] = arr[right]
#     arr[right] = temp

#     left += 1
#     right -= 1

# print(dict(arr))

# Using Built-in Function (Reversed)
arr = dict(reversed(arr.items()))
print(arr)
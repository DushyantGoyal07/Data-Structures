# For String

text = "dushyant"
text = list(text)

# print(text[::-1])  # Using Slicing

# Using Swapping
left = 0
right = len(text)-1

while(left<right):
    temp = text[left]
    text[left] = text[right]
    text[right] = temp

    left += 1
    right -= 1

print("".join(text))
# Remove Duplicates in Sorted Array

arr = [1,1,2,2,3,3,3,4,4]
seen = set()
result = []

for item in arr:
    if item not in seen:
        seen.add(item)
        result.append(item)
    else:
        continue

print(result)
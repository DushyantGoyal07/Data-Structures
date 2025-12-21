# Find Largest Frequently Occurring Element in List

arr = [1,2,2,3,4,3,5]
freq = {}

for item in arr:
    freq[item] = freq.get(item, 0) + 1

max_count = max(freq.values())

result = max([k for k,v in freq.items() if v == max_count])

print(result)
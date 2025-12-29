arr = [1,2,3,2,1]
freq = {}

for item in arr:
    freq[item] = freq.get(item, 0) + 1

result = [k for k,v in freq.items() if v == 1]
print(result)
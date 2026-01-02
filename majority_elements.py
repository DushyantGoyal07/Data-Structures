arr = [2, 2, 1, 1, 2, 2, 2]
freq = {}

for item in arr:
    freq[item] = freq.get(item, 0) + 1

result = [k for k,v in freq.items() if v > (len(arr)/2)]
print(result[0])
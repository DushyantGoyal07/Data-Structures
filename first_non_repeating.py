s = "swiss"
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

result = [k for k,v in freq.items() if v == 1]

print(result[0])
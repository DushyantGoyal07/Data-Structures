s = "abcabcbb"
longest = ""

for i in range(len(s)):
    for j in range(len(s)):
        sub = s[i:j+1]
        if len(sub) == len(set(sub)):
            if len(sub) > len(longest):
                longest = sub

print(longest)
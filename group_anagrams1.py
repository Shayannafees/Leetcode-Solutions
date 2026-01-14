

strs = ["act","pots","tops","cat","stop","hat"]
hm = {}

for i in strs:
    sorted_word = tuple(sorted(i))  # key
    if sorted_word in hm:
        hm[sorted_word].append(i)
    else:
        hm[sorted_word] = [i]


# print(hm)

print(hm.values())
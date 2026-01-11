# abcabcbb -> 3 (abc)
# pwwkew -> 3 (wke)
# bbbbb -> 1 (b)


string = "bbbbb"

set1 = set()

x = 0
max_len = 0

for y in range(len(string)):
    while string[y] in set1:
        set1.remove(string[x])
        x += 1


    set1.add(string[y])
    max_len = max(max_len, y - x + 1)


print(max_len)
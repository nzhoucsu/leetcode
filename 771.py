# SOLUTION ONE
sum = 0
for item in J:
    if item in S:
        sum += S.count(item)
return sum

# SOLUTION TWO
set_S = set(S)
dict = {}
for item in set_S:
    dict[item] = S.count(item)
sum = 0
for item in J:
    if item in set_S:
        sum += dict[item]
return sum
 if not s:
    return 0

dict = {}
t = ''

for i in range(len(s)):
    if s[i] not in t:
        t += s[i]
    else:
        dict[t] = len(t)
        t = t[t.index(s[i])+1:] + s[i]
if t:
    dict[t] = len(t)
return max(dict.values())
rtnLst = []
        
if not numbers:
    return rtnLst

sorted_set = sorted(set(numbers))
for a in sorted_set:
    if a>target:
        return rtnLst
    b = target-a
    if a != b and b in sorted_set:
        return [numbers.index(a)+1, numbers.index(b)+1]
    if a == b and numbers.count(a) > 1:
        idx = numbers.index(a)+1
        return [idx, numbers[idx:].index(b)+1+idx]
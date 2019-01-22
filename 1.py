s = sorted(set(nums))
for a in s:
    b = target - a
    if b in s:
        if a == b and nums.count(a) > 1:
            idx = nums.index(a)
            return [idx, nums[idx+1:].index(a)+idx+1]
        if a != b:
            idx_a = nums.index(a)
            idx_b = nums.index(b)
            if idx_a < idx_b:
                return [idx_a, idx_b]
            else:
                return [idx_b, idx_a]
return []
a = set(nums1)
b = set(nums2)
List = []
if len(a)<len(b):
    for item in a:
        if item in b:
            List.append(item)
else:
    for item in b:
        if item in a:
            List.append(item)
return List
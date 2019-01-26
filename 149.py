res = 0
for i in range(len(points)):
    h, same_point = {}, 1
    x1, y1 = points[i].x, points[i].y
    for j in range(i + 1, len(points)):
        x2, y2 = points[j].x, points[j].y
        if x1 == x2 and y1 == y2:
            same_point += 1
        elif x1 == x2:
            h[float('inf')] = h.get(float('inf'), 0) + 1
        else:
            slope = (y2 - y1) * 100.0 / (x2 - x1)
            h[slope] = h.get(slope, 0) + 1
    local_max = 0
    for val in h.values():
        local_max = max(local_max, val)
    local_max += same_point
    res = max(res, local_max)
    
return res  









# if not points:
#     return 0
# if len(points) == 1:
#     return 1

# dict = {}
# for i in range(len(points)-1):
#     for j in range(i+1, len(points)):
#         p1 = points[i]
#         p2 = points[j]
#         if p1.x == p2.x:
#             a = p1.x
#             s = (a)
#         elif p1.y == p2.y:
#             b = p1.y
#             s = (b)
#         else:                    
#             a = (p2.y - p1.y) / (p2.x - p1.x)
#             b = p1.y - a*p1.x
#             s = (a,b)
#         if s in dict.keys():
#             dict[s].add(i)
#             dict[s].add(j)
#         else:
#             dict[s] = {i, j}
# return max([len(item) for item in dict.values()])            
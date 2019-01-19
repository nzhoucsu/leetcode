if x == 0 or x == 1:
    return x

start = 1
end = x

while start < end:     
    mid = start + (end-start)//2
    a = mid**2
    b = (mid+1)**2
    if a == x:
        return mid
    elif b == x:
        return mid+1
    elif a < x and b > x:
        return mid
    elif a > x:
        end = mid
    elif b < x:
        start = mid
dict = {'0':0,
        '1':1,
        '2':4,
        '3':9,
        '4':16,
        '5':25,
        '6':36,
        '7':49,
        '8':64,
        '9':81}

sum = 0
k = set()
while True:
    s = str(n)
    for item in s:
        sum += dict[item]
    if sum == 1:
        return True
    else:
        if sum in k:
            return False
        else:
            k.add(sum)
            n = sum
            sum = 0
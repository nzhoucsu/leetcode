if x == 0:
    return 0.0
if n == 0:
    return 1.0
if n < 0:
    return 1.0/self.myPow(x, -n)
half = self.myPow(x, n//2)
if n%2:
    return half*half*x
else:
    return half*half
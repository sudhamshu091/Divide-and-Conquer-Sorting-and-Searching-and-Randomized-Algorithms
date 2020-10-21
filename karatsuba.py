def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        n = m // 2

        a = x // 10**(n)
        b = x % 10**(n)
        c = y // 10**(n)
        d = y % 10**(n)

        z0 = karatsuba(b,d)
        z1 = karatsuba((a+b),(c+d))
        z2 = karatsuba(a,c)

        return (z2 * 10**(2*n)) + ((z1 - z2 - z0) * 10**(n)) + (z0)
print(karatsuba(7,3))

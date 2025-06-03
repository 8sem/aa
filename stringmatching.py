def rk(text, pattern):
    d, q = 256, 101
    n, m = len(text), len(pattern)
    h = pow(d, m-1, q)
    p = t = 0
    res = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t and text[i:i+m] == pattern:
            res.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0: t += q

    return res

# Example
p = input("enter the patren :")
m = input("enter matching patren :")
print(rk(p,m))


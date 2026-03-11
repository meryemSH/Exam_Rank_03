def atoi_base(s, base):
    digits = "0123456789ABCDEF"
    res = 0

    for c in s.upper():
        value = digits.index(c)
        res = res * base + value

    return (res)


print(atoi_base("FF", 16))

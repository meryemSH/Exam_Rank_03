def atoi_base(s, base):
    digits = "0123456789ABCDEF"
    res = 0

    for c in s.upper():
        value = digits.index(c)
        res = res * base + value

    return res


def revarese_base(n, base):
    digits = "0123456789ABCDEF"
    results = ""

    if n == 0:
        return "0"

    while n > 0:
        results = results + digits[n % base]
        n //= base

    return results[::-1]


def conver_base(n, base_from, base_to):
    num = atoi_base(n, base_from)
    return revarese_base(num, base_to)
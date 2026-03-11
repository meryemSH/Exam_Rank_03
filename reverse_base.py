def reverse_base(n, base):
    digits = "0123456789ABCDEF"
    res = ""

    if n == 0:
        return "0"

    while n > 0:
        res = res + digits[n % base]
        n //= base

    return res

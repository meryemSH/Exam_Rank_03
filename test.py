def test(stri):
    while stri:
        res = min(stri)
        i = 1
        stri = stri.replace(res, "")
        print(f"{i}: {stri}: {res}")


def main():
    test("zakaria")


main()

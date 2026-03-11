from sys import argv

text = argv[1]
og_len = len(text)
minChar = 'a'
i = 0
while len(text) != 0:
    if minChar in text:
        text = text.replace(minChar, "")
        print(i, text, minChar, sep=":")
        i += 1
    if minChar not in ["z", "Z"]:
        minChar = chr(ord(minChar) + 1)
        continue
    break
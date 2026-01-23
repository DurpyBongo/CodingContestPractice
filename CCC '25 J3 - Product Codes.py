n = int(input())

for _ in range(n):
    s = input()

    letters = ""
    total = 0
    i = 0

    while i < len(s):
        if s[i].isupper():
            letters += s[i]
            i += 1

        elif s[i] == '-' or s[i].isdigit():
            sign = 1
            if s[i] == '-':
                sign = -1
                i += 1

            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            total += sign * num

        else:
            i += 1

    print(letters + str(total))

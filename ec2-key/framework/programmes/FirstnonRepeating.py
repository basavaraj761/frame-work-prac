s = input("enter the string:")


def nonrepeat(s):
    f = {}
    for x in s:
        f[x] = f.get(x, 0) + 1

    for i in s:
        if f[i] == 1:
            return i

    return -1


print(nonrepeat(s))

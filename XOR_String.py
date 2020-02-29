def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] != t[i]:
            res =res+ '1';
        else:
            res = res+'0';

    return res

s = input()
t = input()
print(strings_xor(s, t))




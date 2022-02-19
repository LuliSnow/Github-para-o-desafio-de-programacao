def contandoanagramas(s):

    n = len(s)
    mp = dict()


    for i in range(n):
        sb = ''
        for j in range(i, n):
            sb = ''.join(sorted(sb + s[j]))
            mp[sb] = mp.get(sb, 0)

            mp[sb] += 1

    anas = 0

    for k, v in mp.items():
        anas += (v * (v - 1)) // 2
    return anas

s = str(input('Digite uma palavra: ')).strip()
print(contandoanagramas(s))

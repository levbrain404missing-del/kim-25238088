from itertools import product

k = 0
for p in product('0123456', repeat=5):
    if p[0] == '0':
        continue
    slovo = ''.join(p)
    pary = 0
    tri_podryad = False
    for i in range(4):
        if int(slovo[i]) % 2 == 0 and int(slovo[i + 1]) % 2 == 0:
            pary += 1
    for i in range(3):
        if (int(slovo[i]) % 2 == 0 and
            int(slovo[i + 1]) % 2 == 0 and
            int(slovo[i + 2]) % 2 == 0):
            tri_podryad = True
    if pary >= 2 and not tri_podryad:
        k += 1
print(k)

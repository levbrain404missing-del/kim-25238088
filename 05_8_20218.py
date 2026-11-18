from itertools import product

nomer = 0
otvet = 0
for p in product('ГЕИНРСЯ', repeat=6):
    nomer += 1
    slovo = ''.join(p)
    if 'ГИРЯ' in slovo:
        otvet = nomer
print(otvet)

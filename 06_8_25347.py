from itertools import product

nomer = 0
for p in product('АГИНРТ', repeat=6):
    nomer += 1
    slovo = ''.join(p)
    if nomer % 2 == 1 and slovo[0] not in 'АИГ' and slovo.count('А') == 1:
        print(nomer)
        break

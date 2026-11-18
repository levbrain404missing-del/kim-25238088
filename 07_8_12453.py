from itertools import permutations

k = 0
for p in set(permutations('СОВЕСТЬ')):
    slovo = ''.join(p)
    para_glasnyh = False
    para_soglasnyh = False
    for i in range(6):
        if slovo[i] in 'ОЕЬ' and slovo[i + 1] in 'ОЕЬ':
            para_glasnyh = True
        if slovo[i] not in 'ОЕЬ' and slovo[i + 1] not in 'ОЕЬ':
            para_soglasnyh = True
    if not (para_glasnyh and para_soglasnyh):
        k += 1
print(k)

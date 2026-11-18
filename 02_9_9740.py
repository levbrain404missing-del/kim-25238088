k = 0
with open('9.txt') as f:
    for line in f:
        a = list(map(int, line.split()))
        povt = [x for x in set(a) if a.count(x) == 3]
        nepovt = [x for x in a if a.count(x) == 1]
        if len(povt) == 1 and len(nepovt) == 4:
            if sum(nepovt) <= 4 * povt[0]:
                k += 1
print(k)

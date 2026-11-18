k = 0
with open('9.txt') as f:
    for line in f:
        a = list(map(int, line.split()))
        povt = [x for x in set(a) if a.count(x) > 1]
        nepovt = [x for x in a if a.count(x) == 1]
        if sorted(a.count(x) for x in set(a)) == [1, 1, 1, 2, 4]:
            if sum(nepovt) >= 3 * max(povt):
                k += 1
print(k)

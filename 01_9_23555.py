k = 0
with open('9.txt') as f:
    for line in f:
        a = list(map(int, line.split()))
        povt = [x for x in set(a) if a.count(x) > 1]
        nepovt = [x for x in a if a.count(x) == 1]
        if sorted(a.count(x) for x in set(a)) == [1, 1, 2, 3]:
            if max(povt) > max(nepovt):
                k += 1
print(k)

k = 0
with open('9.txt') as f:
    for line in f:
        a = sorted(map(int, line.split()))
        nepovt = [x for x in a if a.count(x) == 1]
        povt = [x for x in a if a.count(x) > 1]
        usl1 = a[0] * a[-1] < 3 * sum(a[1:-1])
        usl2 = sum(nepovt) <= sum(povt)
        if usl1 != usl2:
            k += 1
print(k)

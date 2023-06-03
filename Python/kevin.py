a = []
for n in range(1, 31):
    for m in range(2, 31):
        for o in range(3, 31):
            if n!=m and m!=o and n!=o and (n+m+o) % 3 == 0:
                check = [n, m, o]
                check.sort()
                check = tuple(check)
                if check not in a:
                    a.append(check)

print(len(a))
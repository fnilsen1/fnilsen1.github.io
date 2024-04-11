start = 1
end = 30
sum = 0
for i in range(start,end-1):
    for n in range(i+1,end):
        for m in range(n+1, end+1):
            if (i+n+m)%3 == 0:
                sum += 1
print(sum)


[]
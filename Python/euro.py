arr = [0, 0, 0, 0, 0]
target = [200, 100, 40, 10, 2]
count = 0

while arr != target:
    arr[0] += 1
    
    if arr[0] > 200:
        arr[0] = 0
        arr[1] += 1
    
    if arr[1] > 100:
        arr[1] = 0
        arr[2] += 1
    
    if arr[2] > 40:
        arr[2] = 0
        arr[3] += 1

    if arr[3] > 10:
        arr[2] = 0
        arr[4] += 1
    
    if (arr[0] + arr[1]*2 + arr[2]*5 + arr[3]*20+arr[4]*100) == 200:
        count += 1
    
    print(arr)

print(count)
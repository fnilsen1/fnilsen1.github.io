import random
# iterations = 10000000
# liste = [10, 20, 40, 80, 160]
# amount = []
# for i in range(iterations):
#     sum = 0
#     for j in range(len(liste)):
#         random_int = random.randint(1,2)
#         if random_int == 1:
#             sum += liste[j]
#     amount.append(sum)
# count = 0
# for i in range(len(amount)):
#     if amount[i]>=200:
#         count+=1
# print(count/iterations)
    

#100 lvl 3
#56 lvl 2, 22 lvl 4, 22 lvl 6
#51 lvl 1, 49 lvl 5
valg = []

one = [3]
two = []
three = []


for i in range(56):
    two.append(2)

for i in range(22):
    two.append(4)
    two.append(6)

for i in range(51):
    three.append(1)

for i in range(49):
    three.append(5)

valg.append(one)
valg.append(two)
valg.append(three)


results = []
def simulation():
    valg_copy = valg.copy()  # Make a copy of valg to avoid modifying the original list
    tilfeldig = random.randint(0, 2)
    tall1 = random.randint(0, len(valg_copy[tilfeldig]) - 1)
    first = valg_copy[tilfeldig][tall1]
    valg_copy.pop(tilfeldig)

    tilfeldig1 = random.randint(0, 1)
    tall2 = random.randint(0, len(valg_copy[tilfeldig1]) - 1)
    second = valg_copy[tilfeldig1][tall2]

    if first > second:
        results.append(tilfeldig)

    else:
        results.append(valg.index(valg_copy[tilfeldig1]))



for i in range(1000000):
    simulation()

print(results)
print(results.count(0)/10000)
print(results.count(1)/10000)
print(results.count(2)/10000)


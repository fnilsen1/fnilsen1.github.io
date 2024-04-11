import math
# dt = 0.001
# x = 0
# best_area = 0
# best_x = 0

# while x < 2:
#     A = x*math.sqrt(16-x**2)+x*math.sqrt(4-x**2)
#     if(A > best_area):
#         best_area=A
#         best_x = x

#     x+=dt
# print(best_area, best_x)

dx = 0.00001
start = 0
slutt = math.pi
intervall_lengde = 2
arc_lengde = 0

def func(x):
    return math.sin(x)

for i in range (int(math.pi/dx)-1):
    arc_lengde+=math.sqrt(dx**2+(func(start+dx)-func(start))**2)
    start+=dx


print(arc_lengde)
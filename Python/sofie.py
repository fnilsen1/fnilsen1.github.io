# import random
# liste = []
# count = 0
# c = 299


# a = [0 for i in range(294)]
# for j in range(3):
#     a.append(1)
# for k in range(3):
#     a.append(2)

# for l in range(100000): 
#     liste = []
#     c=299
#     a = [0 for i in range(294)]
#     for j in range(3):
#         a.append(1)
#     for k in range(3):
#         a.append(2)

#     for i in range(5):
#         b = random.randint(0,c)
#         liste.append(a[b])
#         a.pop(b)
#         c-=1


#     if liste[0]==1 or liste[1]==1 or liste[2]==1 or liste[3]==1 or liste[4]==1:
#         count+=1
        
# print(count/100000)

# #0.048'

#0.4165913
# import random 

#UTLEVERT KODE (ingenting her skal endres)
# import numpy as np
# import matplotlib.pyplot as plt
# #utfallsrom
# x=np.arange(6)
# #punktsannsynlighet
# f_x = np.array([0.05,0.10,0.25,0.40,0.15,0.05])
# #stolpediagram
# plt.bar(x, f_x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("Stolpediagram for f(x)")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# def f_X(x, alpha):
#     return (2*x/alpha)*np.exp((-x**2)/alpha)

# def f_Z(z, alpha):
#     return 2*(1-np.exp((-z**2)/alpha))*((2*z/alpha)*np.exp((-z**2)/alpha))

# x = np.linspace(0,5,100)

# alpha = 1

# plt.plot(x, f_X(x, alpha), color="red") 
# plt.plot(x, f_Z(x, alpha), color="blue") 
# plt.show()





# UTLEVERT KODE (ingenting her skal endres)
# punktsannsynlighet
# import numpy as np
# import matplotlib.pyplot as plt

# f_x = np.array([0.05,0.10,0.25,0.40,0.15,0.05])
# # kumulativ fordelingsfunksjon
# F_x = [np.sum(f_x[:i]) for i in range(1,7)]
# print(F_x)
# def simX(n):
#     # verdimengde
#     x = np.arange(6)
#     # for lagring av realisasjoner
#     x_sim = np.zeros(n)
#     for i in range(n): # vi simulerer hver og en x for seg
#         u = np.random.uniform() # en realisasjon fra U(0,1)
#         if(u < F_x[0]): # hvis u er mindre enn den laveste
#         # verdien i F_x vil
#         # vi at realisasjonen skal være 0
#             x_sim[i] = x[0]
#         elif(u <= F_x[1]): # hvis u er mindre enn den nest
#         # laveste verdien (men større enn laveste)
#         # vil vi at x skal bli 1
#             x_sim[i] = x[1]
#         elif(u <= F_x[2]):
#             x_sim[i] = x[2]
#         elif(u <= F_x[3]):
#             x_sim[i] = x[3]
#         elif(u <= F_x[4]):
#             x_sim[i] = x[4]
#         elif(u > F_x[4]):
#             x_sim[i] = x[5]
#     return x_sim

# def E(X):
#     return np.sum(X)/len(X)

# def SD(X):
#     varians = E(X**2)-E(X)**2
#     return np.sqrt(varians)

# # Antall realisasjoner man skal bruke
# n = 1000
# # Simuler realisasjoner av X ved å kalle på simX-funksjonen i cellen over
# simulerte_X = simX(n)
# standardavvik = SD(simulerte_X)
# print(standardavvik)


# forventningsverdi = (sum(simulerte_X))/n
# # Skriv ut resultatet
# print("Approksimert forventningsverdi: ", forventningsverdi)

# import numpy as np
# import matplotlib.pyplot as plt

# def generateX(n,alpha):
#     u = np.random.uniform(size=n) #array med n elementer.
#     x = np.sqrt(-alpha*np.log(1-u))
#     return x

# def Y(n):
#     a = generateX(n, 1)
#     b = generateX(n, 1)
#     c = generateX(n, 1.2)
#     d = generateX(n, 1.2)
#     e = generateX(n, 1.2)
#     liste = np.zeros(n)
    
#     for i in range(n):
#         tmp_liste = np.zeros(5)
#         tmp_liste[0]=a[i]
#         tmp_liste[1]=b[i]
#         tmp_liste[2]=c[i]
#         tmp_liste[3]=d[i]
#         tmp_liste[4]=e[i]
#         tmp_liste.sort()

#         liste[i]=tmp_liste[2]
#     return liste

# n = 10000
# simulerte_Y = Y(n)

# count = 0
# for i in range(n):
#     if simulerte_Y[i]>=1:
#         count+=1

# count1 = 0
# for j in range(n):
#     if simulerte_Y[j]>=0.75:
#         count1+=1

# print("P(Y>=1 | Y>=0.75) = ", count/count1)
# import numpy as np

# array_2d = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])

# median_values_along_columns = np.median(array_2d, axis=1)

# print(median_values_along_columns)


# plt.hist(simulerte_Y, density=True,bins=100)
# plt.show()



# x = np.linspace(0, 4, 1000)
# y = 2*x/alpha*np.e**((-x**2)/alpha)

# plt.plot(x, y)

# import numpy as np
# import matplotlib.pyplot as plt

# #Enkel destillasjon
# x = np.array([5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
# y = np.array([73, 73, 75.5, 75, 76, 78, 81, 81, 84, 94, 104, 106, 107, 108, 108, 108, 108, 108, 108, 107, 107, 106, 105])

# #Fraksjonert destillasjon
# a = np.array([5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
# b = np.array([77, 75.5, 76, 78, 78, 77.5, 77, 77, 77, 87, 111, 112, 112, 112, 113, 113, 113, 113, 113])


# print(len(x), len(y))
# # plt.plot(x, y, marker='o', linestyle='-', color='orange', label='Enkel destillasjon')
# # plt.plot(a, b, marker='o', linestyle='-', color='blue', label='Fraksjonert destillasjon')
# # plt.xlabel('Volum destillat [mL]')
# # plt.ylabel('Temperatur [°C]')
# # plt.title('Sammenligning av destillasjon og observert kokepunkt')

# # # Legg til en legend
# # plt.legend()

# # # Vis plottet
# # plt.show()


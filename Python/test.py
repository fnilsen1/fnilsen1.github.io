import math
import matplotlib.pyplot as plt
import numpy as np
import random



# import openpyxl
 

# dataframe = openpyxl.load_workbook("Python/antall_sokere_vgs.xlsx")
 
# dataframe1 = dataframe.active
 
# cell_obj = dataframe1.cell(row = 5, column = 1)

# print(cell_obj.value)



data = np.random.normal(60, 5, 100) 
# x = np.linspace(-50,50, 101)
# print(data)
# # print(x)
# plt.plot(x,data)

# # plt.xlabel("x")
# # plt.ylabel("y")
plt.hist(data, bins=10)
plt.show()

# import matplotlib.pyplot as plt

# partiforkortelser = ["Jenter", "Gutter"]
# representanter = [10, 20]

# plt.pie(representanter, labels=partiforkortelser)

# plt.show()


# def f(x):
#     return math.sin(x)

# x_verdier = np.linspace(-5,5,500)
# print(x_verdier)
# y_verdier = []

# for i in range(len(x_verdier)):

#     y_verdier.append(f(x_verdier[i]))

# plt.plot(x_verdier, y_verdier)
# plt.show()


# x = np.linspace(-5,5,500)


# a = (3*x**4)+2*x-2
# b=(x**2)+x
# c = -x**2-3*x

# plt.plot(x,a, color='r', linestyle='dashed')
# plt.plot(x,b, linestyle='dotted')
# plt.plot(x,c)

# plt.xlabel("x")
# plt.ylabel("y")

# plt.show()



# list = []
# checked_list = []
# checking = []

# count = 0
# for i in range (1,31,1):
#     list.append(i)

# # print(list)

# for i in range(len(list)):
#     for j in range(len(list)):
#         for k in range(len(list)):
#             checking = [list[i],list[j],list[k]]
#             checking.sort()
#             if(checking in checked_list):
#                 pass
            
#             elif(checking not in checked_list and list[i]!=list[j] and list[j]!=list[k] and  list[i]!=list[k]):    
#                 checked_list.append(checking)  
#                 if((list[i]+list[j]+list[k])%3==0):   
#                     count+=1

            
# print(count)

sum = 0
for i in range(1000000000):
    sum+=i
print(sum)
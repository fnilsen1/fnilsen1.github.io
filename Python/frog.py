import random
jump_list = []
for i in range(10000):
    current_pad = 0
    jumps = 0
    while current_pad!=10:
        jumps+=1
        current_pad+=random.randint(1, 10-current_pad)
    jump_list.append(jumps)
print(sum(jump_list)/len(jump_list))
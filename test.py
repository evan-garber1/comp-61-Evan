#line = ""
#for i in range(3):
    #for j in range(3):
    #    line += str(i) + str(j) + " "
    #print(line)
    #line = ""


# a_list = [0, 1, 2, 3, 4]
#print(a_list)
#a_list[2] = 10
#print(a_list[2])



#a_list = [0, 1, 2, 3, 4]
#two_d_list = [ [0, 1, 2, 3, 4],
              #[5, 6, 7, 8, 9],
              #[10, 11, 12, 13, 14]
 #             ]
#print(two_d_list)
#print(two_d_list[1])
#print(two_d_list[1][1])


import random
two_d_visual_list = []
visual_line = []
for i in range(3):
    for j in range(3):
        visual_line.append(random.randint(0,1))
    two_d_visual_list.append(line)
    visual_line = []

print(two_d_visual_list)

two_d_mine_list = []
mine_line = []
for i in range(3):
    for j in range(3):
        mine_line.append(random.randint(0,1))
    two_d_mine_list.append(line)
    mine_line = []

print(two_d_mine_list)

input_x = int(input("Input x position: "))
input_y = int(input("Input y position: "))

if(two_d_mine_list[input_x] [input_y] == 1):
    print("You lose")
else:
    print("Keep going")


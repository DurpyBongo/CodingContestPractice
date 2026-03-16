num_of_parkinglots = int(input())
num_of_lights = int(input())
which_parking_lots = int(input())

which_one_is_lit = [] # final list of all lights which are lit up

answerkey = []
for i in range(num_of_lights):
    single_light = input().split()
    base_parking = int(single_light[0]) # the parkinglot underneath
    length = int(single_light[1]) # parkinglots to the sidemnmm
    which_one_is_lit.append(base_parking)

    for i in range(base_parking-length,base_parking+length+1):
        which_one_is_lit.append(i)

for x in range(which_parking_lots):
    ask = int(input())
    if which_one_is_lit.__contains__(ask):
        print('Y')
    else:
        print('N')

        


num_of_parkinglots = int(input())
num_of_lights = int(input())
which_parking_lots = int(input())

which_one_is_lit = [] # final list of all lights which are lit up

answerkey = []

for i in range(num_of_lights):
    single_light = input().split()
    base_parking = int(single_light[0]) # the parkinglot underneath
    length = int(single_light[1]) # parkinglots to the sidemnmm

    which_one_is_lit.append([base_parking-length,base_parking+length])

for x in range(which_parking_lots):
    ask = int(input())
    for i in which_one_is_lit:
        if ask>=i[0] and ask<=i[1]:
            print('Y')
        
            print('N')

        


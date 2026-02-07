import sys

rounds = int(input())

# if rounds>5:
#     sys.exit()
big_list = []
temporary_group_three = []
for i in range(rounds):
    for u in range(3):
        ligma = input()
        temporary_group_three.append(ligma)
    big_list.append(temporary_group_three)
    temporary_group_three = []

def checkFIX(list_of_three):
    for u in range(len(list_of_three)):
        base = list_of_three[u]
        for i in range(len(list_of_three)):
            if i!=u:
                if list_of_three[i].startswith(base) or list_of_three[i].endswith(base):# and list_of_three[i]!=base:
                    return "No"
            # elif list_of_three[i].endswith(base) and list_of_three[i]!= base:
            #     yes_or_no = False
            #     break
    return "Yes"

for l in range(rounds):
    print(checkFIX(big_list[l]))

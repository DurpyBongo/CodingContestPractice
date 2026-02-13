days = int(input())
one = 0
two = 0
three = 0
four = 0
five = 0

all_num = []
for i in range(days):
    available = input()
    for i in range(len(available)):
        if available[i] == 'Y':
            if i == 0:
                one+=1
            elif i ==1:
                two +=1
            elif i ==2:
                three +=1
            elif i ==3:
                four +=1
            elif i ==4:
                five +=1

all_num.append(one)
all_num.append(two)
all_num.append(three)
all_num.append(four)
all_num.append(five)

x = all_num.count(max(all_num))

if x ==1:
    print(all_num.index(max(all_num))+1)
else:
    empty = []
    for i in range(5):
        if all_num[i] == max(all_num):
            if i == 0:
                empty.append('1')
            elif i ==1:
                empty.append('2')
            elif i ==2:
                empty.append('3')
            elif i ==3:
                empty.append('4')
            elif i ==4:
                empty.append('5')
    print(','.join(empty))
A = input()
B = input()

first_list = list(A)
second_list = list(B)

first_count = 0
second_count = 0
while len(first_list)>0 and len(second_list)>0:
    if first_list[0]==second_list[0]:
        first_list.pop(0)
        second_list.pop(0)
        first_count +=1
        second_count +=1
    elif first_list[0] == 'R' and second_list[0] == 'G':
        second_list.pop(0)
        first_count +=1
    elif second_list[0] == 'R' and first_list[0] == 'G':
        first_list.pop(0)
        second_count +=1
    elif first_list[0] == 'G' and second_list[0] == 'B':
        second_list.pop(0)
        first_count +=1 
    elif second_list[0] == 'G' and first_list[0] == 'B':
        first_list.pop(0)
        second_count +=1
    elif first_list[0] == 'B' and second_list[0] == 'R':
        second_list.pop(0)
        first_count +=1 
    elif second_list[0] == 'B' and first_list[0] == 'R':
        first_list.pop(0)
        second_count +=1

boi = len(first_list)
gurl = len(second_list)
if boi>0:
    first_count+=boi
elif gurl>0:
    second_count+=gurl

print(first_count)
print(second_count)
    

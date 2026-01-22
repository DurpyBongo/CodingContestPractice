import math
first = int(input())
second = int(input())
final = 0
for i in range(first, second + 1):
    count=0
    for u in range(1,i+1):
        if i % u ==0:
            count+=1
    if count==4:
        final+=1
print(f'The number of RSA numbers between {first} and {second} is {final}')



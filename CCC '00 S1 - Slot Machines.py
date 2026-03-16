import sys

money = int(input())
first = int(input())
second= int(input())
third = int(input())

count = 0
for i in range(first):
    money-=1
    count+=1
    if i % 35 == 0:
        money+=30
    if money<=0:
        print(f'Martha plays {count} times before going broke.')
        sys.exit()
if money>0:
    for i in range(second):
        money-=1
        count+=1
        if i % 100 == 0:
            money+=60
        if money<=0:
            print(f'Martha plays {count} times before going broke.')
            sys.exit()
if money>0:
    for i in range(third):
        money-=1
        count+=1
        if i % 10 == 0:
            money+=9
        if money<=0:
            print(f'Martha plays {count} times before going broke.')
            sys.exit()
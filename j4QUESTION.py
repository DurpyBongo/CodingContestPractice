rounds = int(input())
x = 0
y=0
starting_position = [x,y]
slimy_squares = []
slimy_squares.append(starting_position)
position = starting_position.copy()
count = 0

empty = []
for i in range(rounds):
    direction = input()
    empty = []
    NSEW = direction[0]
    for cashew in range(len(direction)):
        if cashew != 0:
            empty.append(direction[cashew])
    kebab = int(''.join(empty))
    
    if NSEW == 'S':
        for u in range(kebab):
            y-=1
            slimy_squares.append([x,y])
            hi = [x,y]
            if slimy_squares.count(hi)>1:
                slimy_squares.pop(-1)
                count+=1
        # if slimy_squares.count(hi)>1:
        #     count+=1
        #     slimy_squares.pop(-1)

    elif NSEW == 'N':
        for u in range(kebab):
            y+=1
            slimy_squares.append([x,y])
            hi = [x,y]
            if slimy_squares.count(hi)>1:
                slimy_squares.pop(-1)
                count+=1
        # if slimy_squares.count(hi)>1:
        #     count+=1
        #     slimy_squares.pop(-1)

    elif NSEW == 'E':
        for u in range(kebab):
            x+=1
            slimy_squares.append([x,y])
            hi = [x,y]
            if slimy_squares.count(hi)>1:
                slimy_squares.pop(-1)
                count+=1
        # if slimy_squares.count(hi)>1:
        #     count+=1
        #     slimy_squares.pop(-1)

    elif NSEW == 'W':
        for u in range(kebab):
            x-=1
            slimy_squares.append([x,y])
            hi = [x,y]
            if slimy_squares.count(hi)>1:
                slimy_squares.pop(-1)
                count+=1
        # if slimy_squares.count(hi)>1:
        #     count+=1
        #     slimy_squares.pop(-1)
print(count)
    


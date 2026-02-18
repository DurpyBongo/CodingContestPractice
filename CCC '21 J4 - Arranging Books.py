code = input()
base = list(code)
count = 0

mwah = base.copy()
mwah.sort()
while True:
    for i in range(len(base)):
        character = base[i]
        if character =='M':
            if 'L' in base[i+1:len(base)]:
                for y in range(i+1,len(base)):
                    if base[y]=='L':
                        base[i]='L'
                        base[y]=character
                        count+=1
        if character =='S':
            if 'L' in base[i+1:len(base)]:
                for y in range(i+1,len(base)):
                    if base[y]=='L':
                        base[i]='L'
                        base[y]=character
                        count+=1
            if 'M' in base[i+1:len(base)]:
                for y in range(i+1,len(base)):
                    if base[y] =='M':
                        base[i]='M'
                        base[y]=character
                        count+=1
    if mwah == base:
        break   
print(count) 
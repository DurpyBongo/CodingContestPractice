follow = input()
group = {"C": [], "D": [], "S": [], "H": []}
Clist = []
Dlist = []
Slist =[]
Hlist=[]

Cpoints =0
Dpoints =0
Spoints =0
Hpoints =0

for i in follow:
    if i == 'C' or i == 'D' or i == 'S' or i == 'H':
        current = i
    else:
        group[current].append(i)
for x in range(len(group['C'])):
    if group['C'][x] in ['A', 'K', 'Q', 'J']:
        Clist.append(group['C'][x])
for x in range(len(group['D'])):
    if group['D'][x] in ['A', 'K', 'Q', 'J']:
        Dlist.append(group['D'][x])
for x in range(len(group['S'])):
    if group['S'][x] in ['A', 'K', 'Q', 'J']:
        Slist.append(group['S'][x])
for x in range(len(group['H'])):
    if group['H'][x] in ['A', 'K', 'Q', 'J']:
        Hlist.append(group['H'][x])



for hello in range(len(Clist)):
    if Clist[hello] == 'A':
        Cpoints += 4
    if Clist[hello] == 'K':
        Cpoints += 3
    if Clist[hello] == 'Q':
        Cpoints +=2
    if Clist[hello] == 'J':
        Cpoints += 1
if len(group['C']) == 0:
    Cpoints += 3
elif len(group['C']) == 1:
    Cpoints += 2
elif len(group['C']) == 2:
    Cpoints +=1



for hello in range(len(Dlist)):
    if Dlist[hello] == 'A':
        Dpoints += 4
    if Dlist[hello] == 'K':
        Dpoints += 3
    if Dlist[hello] == 'Q':
        Dpoints +=2
    if Dlist[hello] == 'J':
        Dpoints += 1
if len(group['D']) == 0:
    Dpoints += 3
elif len(group['D']) == 1:
    Dpoints += 2
elif len(group['D']) == 2:
    Dpoints +=1

for hello in range(len(Slist)):
    if Slist[hello] == 'A':
        Spoints += 4
    if Slist[hello] == 'K':
        Spoints += 3
    if Slist[hello] == 'Q':
        Spoints +=2
    if Slist[hello] == 'J':
        Spoints += 1
if len(group['S']) == 0:
    Spoints += 3
elif len(group['S']) == 1:
    Spoints += 2
elif len(group['S']) == 2:
    Spoints +=1

for hello in range(len(Hlist)):
    if Hlist[hello] == 'A':
        Hpoints += 4
    if Hlist[hello] == 'K':
        Hpoints += 3
    if Hlist[hello] == 'Q':
        Hpoints +=2
    if Hlist[hello] == 'J':
        Hpoints += 1
if len(group['H']) == 0:
    Hpoints += 3
elif len(group['H']) == 1:
    Hpoints += 2
elif len(group['H']) == 2:
    Hpoints +=1

C_boi = ' '.join(group['C'])
D_boi = ' '.join(group['D'])
S_boi = ' '.join(group['S'])
H_boi = ' '.join(group['H'])


print(f'Cards Dealt              Points')
print(f'Clubs {C_boi}            {Cpoints}')
print(f'Diamonds {D_boi}              {Dpoints}')
print(f'Hearts {H_boi}              {Hpoints}')
print(f'Spades {S_boi}                  {Spoints}')
print(f'                       Total {Cpoints+Dpoints+Hpoints+Spoints}')

        
        


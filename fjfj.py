for hello in range(len(Hlist)):
    if Hlist[hello] == 'A':
        Cpoints += 4
    if Hlist[hello] == 'K':
        Cpoints += 3
    if Hlist[hello] == 'Q':
        Cpoints +=2
    if Hlist[hello] == 'J':
        Cpoints += 1
if len(Hlist) == 0:
    Cpoints += 3
elif len(Hlist) == 1:
    Cpoints += 2
elif len(Hlist) == 2:
    Cpoints +=1
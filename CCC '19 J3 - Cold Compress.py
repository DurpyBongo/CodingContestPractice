rounds = int(input()) # this is the input
messages = [] # this has all of the lines as seperate values ['adf', 'asdffwe]
what_to_print_final = [] #last thing to print
empty = []
for i in range(rounds): 
    message = input()
    messages.append(message)
    #entire thing to get the messages in the list
for x in range(rounds):
    thing = messages[x] # take line
    what_to_print = []
    base = thing[0] #first character
    count = 1
    for y in range(1, len(thing)+1):
        if y==len(thing):
            what_to_print.append(str(count))
            what_to_print.append(base) #number and character
        elif base == thing[y]:
            count+=1
            base = thing[y]
        else:
            what_to_print.append(str(count))
            what_to_print.append(base) #number and character
            base = thing[y] # base is new character start over checking again 
            count = 1
    finished_line = ' '.join(what_to_print)
    what_to_print_final.append(finished_line)
for WHOOOO_ITHINKIDIDIT in what_to_print_final:
    print(WHOOOO_ITHINKIDIDIT)






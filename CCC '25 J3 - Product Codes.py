rounds = int(input())
all_raw_codes = [] # all of the inputs, did not change any of it
one_line = []
final_answer = []

temporary = [] # just use temporary and then make it back into empty list
negative_temporary = [] # for temporary that are negative


help_the_count_when_multi_digit = []
for i in range(rounds):
    poop = input()
    all_raw_codes.append(poop)
for y in range(len(all_raw_codes)): # this is ONE raw code
        count=0 #integer value for ONE raw code
        one_line = []
        for x in range(len(all_raw_codes[y])): # specific character in ONE craw code
            if all_raw_codes[y][x].isupper() == True:
                one_line.append(all_raw_codes[y][x])
            elif all_raw_codes[y][x].isdigit() == True: # check to see if digit
                if all_raw_codes[y][x-1] == '-' and x+1<=len(all_raw_codes)-1 and all_raw_codes[y][x+1].isdigit() != True:
                    count-=int(all_raw_codes[y][x]) # if its a digit and the previous is negative, than minus                        #fix this cuz what if multi digit? just use the elif below when finished and paste it here
                elif x+1<=len(all_raw_codes)-1 and all_raw_codes[y][x+1].isdigit() == True:
                    if all_raw_codes[y][x-1] =='-':
                        negative_temporary.append(all_raw_codes[y][x])
                        negative_temporary.append(all_raw_codes[y][x+1])
                        nigga = ''.join(negative_temporary)
                        negative_temporary = []
                        negative_temporary.append(nigga) # bigger number
                    else:
                        temporary.append(all_raw_codes[y][x])
                        temporary.append(all_raw_codes[y][x+1])
                        rawr = ''.join(temporary)
                        temporary = []
                        temporary.append(rawr) # bigger number
                else:
                    count+=int(all_raw_codes[y][x]) # else its positivie just add
                    if temporary != []:
                        count+=int(temporary[0]) # only if multi digit number is positive
                    if negative_temporary != []:
                        count-=int(negative_temporary[0])
                    negative_temporary = []
                    temporary=[]
        one_line.append(str(count))
        obamam = ''.join(one_line)
        final_answer.append(obamam)
for twotwosMycrodie in range(len(final_answer)):
    print(final_answer[twotwosMycrodie])

        
            

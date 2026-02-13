string = input()
temporary_string = []
temporary_all_string = [] # has everything for on command
temporary_digit = [] # temporary for digits to check how long it is
all_commands = []
for i in range(len(string)):
    if string[i] in "QWERTYUIOPASDFGHJKLZXCVBNM":
        temporary_string.append(string[i]) # ['A','b']
    elif string[i] in '+-':
        x = ''.join(temporary_string)
        temporary_all_string.append(x) # appended the actual string now like ABC
        temporary_string=[]
        if string[i] == '+':
            temporary_all_string.append('tighten')
        elif string[i] == '-':
            temporary_all_string.append('loosen')
        temporary_string = []
    elif string[i].isdigit():
        temporary_digit.append(string[i]) # ['1','2']
        if i+1 == len(string) or not string[i+1].isdigit():
            y = ''.join(temporary_digit)
            temporary_all_string.append(y)
            temporary_digit = []
            all_commands.append(temporary_all_string)
            temporary_all_string=[]

for i in range(len(all_commands)):
    print(f'{' '.join(all_commands[i])}')


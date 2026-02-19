rounds = int(input())
answer = []

for i in range(rounds):
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for u in range(4):
        line = input().strip()
        single_line = line.split(' ')
        word = single_line[-1].lower()

        syllable = word  # default if no vowel found

        # scan backwards
        for x in range(len(word) - 1, -1, -1):
            if word[x] in ['a', 'e', 'i', 'o', 'u']:
                syllable = word[x:]
                break

        if u == 0:
            first_line = syllable
        elif u == 1:
            second_line = syllable
        elif u == 2:
            third_line = syllable
        elif u == 3:
            fourth_line = syllable

    # classify AFTER reading 4 lines
    if first_line == second_line == third_line == fourth_line:
        answer.append('perfect')
    elif first_line == second_line and third_line == fourth_line:
        answer.append('even')
    elif first_line == third_line and second_line == fourth_line:
        answer.append('cross')
    elif first_line == fourth_line and second_line == third_line:
        answer.append('shell')
    else:
        answer.append('free')

for result in answer:
    print(result)

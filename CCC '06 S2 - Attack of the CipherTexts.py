first = list(input())
second = list(input())
answer = ''
dic = {}
for i in range(len(second)):
    dic[second[i]] = first[i]

code = list(input())

for u in range(len(code)):
    if code[u] not in dic:
        answer = answer + '.'
    else:
        answer = answer + dic[code[u]]
print(answer)



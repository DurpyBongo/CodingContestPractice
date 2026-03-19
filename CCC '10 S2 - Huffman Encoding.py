rounds = int(input())
dic = {}
queue = ''
answer = ''
for i in range(rounds):
    text = input().split()
    dic[text[1]] = text[0]

code = input()
for u in range(len(code)):
    queue+= code[u]
    
    if queue in dic:
        answer = answer + dic[queue]
        queue = ''
        
print(answer)


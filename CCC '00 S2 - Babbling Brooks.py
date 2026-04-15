number_of_streams = int(input())
streams = []
for i in range(number_of_streams):
    power = int(input())
    streams.append(power)
while True:
    inputed = int(input())
    if inputed == 99:
        index_num = int(input())-1
        percentage = int(input())
        queue = streams[index_num]
        left = queue*percentage/100
        right = queue-left
        streams.insert(index_num+1, right)
        streams.insert(index_num+2, left)
        del streams[index_num]
        
    elif inputed == 88:
        index_num = int(input())-1
        queue_value = streams[index_num]+streams[index_num+1]
        streams.insert(index_num,queue_value)
        del streams[index_num+1:index_num+2]
    elif inputed == 77:
        break
print(" ".join(map(str, streams)))




starting_point = input()
end_point = input()

st = starting_point.split()
end = end_point.split()

start_x = int(st[0])-1
start_y = int(st[1])-1
end_x = int(end[0])-1
end_y = int(end[1])-1

directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

visited = [[False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False]]

queu = [[start_x, start_y, 0]]

for i in directions:
    new_x = start_x + i[0]
    new_y = start_y + i[1]
    queu.pop(0)
    
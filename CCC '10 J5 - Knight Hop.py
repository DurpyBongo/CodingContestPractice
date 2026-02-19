starting_point = input()
end_point = input()

st = starting_point.split()
end = end_point.split()

start_x = int(st[0])-1
start_y = int(st[1])-1
end_x = int(end[0])-1
end_y = int(end[1])-1

directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

visited = [[False for _ in range(8)] for _ in range(8)]
visited[start_x][start_y] = True
queue = [(start_x, start_y, 0)]  # (x, y, moves)

while queue:
    x, y, moves = queue.pop(0)

    if x == end_x and y == end_y:
        print(moves)
        break

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < 8 and 0 <= new_y < 8 and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            queue.append((new_x, new_y, moves + 1))


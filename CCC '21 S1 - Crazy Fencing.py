trapezoids = int(input())
count = 0
# for i in range(trapezoids+1):
#     base = int(input())
#     bases.append(base)
# for i in range(trapezoids):
#     height = int(input())
#     heights.append(height)

base = input()
bases = base.split(' ')
height = input()
heights = height.split(' ')

for u in range(trapezoids):
    grah = int(bases[u]) + int(bases[u+1])
    hello = grah*int(heights[u])/2
    count +=hello
print(count)

with open('2021/Day 2/input.txt') as f:
    contents = f.readlines()
    #open file and make it a list

depth = 0
dist = 0
aim = 0


for line in contents:
#beginning of loop

    forw = line.find('forward')
    down = line.find('down')
    up = line.find('up')

    amount = int(line[-2])

    if forw == 0:
        dist = dist + amount
        depth = depth + (amount * aim)

    if down == 0:
        aim = aim + amount

    if up == 0:
        aim = aim - amount

print('Depth: ',depth)
print('Distance: ',dist)

answer = depth * dist

print('Answer: ',answer)
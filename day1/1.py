f = open('./input.txt')

sum = 0

for line in f:
    sum += int(line)

print(sum)
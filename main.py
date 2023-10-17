k = 0
min = 9081
max = 0

for i in range(3466, 9081 + 1):
    a = i
    s = 0
    while a > 0:
        s += 1
        a = a // 8
    if ((i % 7 == 1 or i % 7 == 5) and s != 4):
        k += 1
        max = i

print(k, max)
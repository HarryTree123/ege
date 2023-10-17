n = 9**5 + 3**25 - 20
s = 0
s1 = 0
s2 = 0
while n > 0:
    s = s + n % 3
    n = n // 3
print(s)
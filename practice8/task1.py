# Препдоположим что a и b != 0
c = 5
koren = c ** (1/2) + 1


for a in range(1, c):
    for b in range(1, c):
        if a*a + b*b == c:
            print(True)
            exit(0)

print(False)

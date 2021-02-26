import random
print('Δώσε την πλευρά του τετραγώνου:')
side = int(input('> '))
while side < 0:
    print('Δώσε θετικό αριθμό')
    side = int(input('> '))
total100 = 0
repetition = 100
for k in range(repetition):
    numbers = []
    for i in range(side):
        numbers.append([0] * side)
    half = int((side ** 2) / 2) + ((side ** 2) % 2 > 0)
    y = 0
    while y < half:
        r1 = random.randrange(0, side)
        r2 = random.randrange(0, side)
        if numbers[r1][r2] != 1:
            numbers[r1][r2] = 1
            y += 1
    print('_________________________________________________________________')
    for i in range(side):
        print(numbers[i])
    print('_________________________________________________________________')
    vertical = 0
    horizontal = 0
    diagonal = 0

    for i in range(side):
        c = 0
        for j in range(side):
            if numbers[i][j] == 1:
                c = c + 1
                if c == 4:
                    horizontal += 1
                    c = 0
            else:
                c = 0
    print('Οριζόντιες τετράδες:', horizontal)
    for i in range(side):
        c = 0
        for j in range(side):
            if numbers[j][i] == 1:
                c = c + 1
                if c == 4:
                    vertical += 1
                    c = 0
            else:
                c = 0
    print('Κάθετες τετράδες:', vertical)
    for i in range(side - 3):
        for j in range(side - 3):
            if i == 0 or j == 0:
                if numbers[i][j] == numbers[i + 1][j + 1]:
                    if numbers[i][j] == numbers[i + 2][j + 2]:
                        if numbers[i][j] == numbers[i + 3][j + 3]:
                            if numbers[i][j] == 1:
                                diagonal += 1
            else:
                if numbers[i][j] == 1:
                    if numbers[i - 1][j - 1] != 1:
                        if numbers[i][j] == numbers[i + 1][j + 1]:
                            if numbers[i][j] == numbers[i + 2][j + 2]:
                                if numbers[i][j] == numbers[i + 3][j + 3]:
                                    diagonal += 1
    for i in reversed(range(side - 3)):
        for j in reversed(range(3, side)):
            if i == 0 or j == side - 1:
                if numbers[i][j] == 1:
                    if numbers[i][j] == numbers[i + 1][j - 1]:
                        if numbers[i][j] == numbers[i + 2][j - 2]:
                            if numbers[i][j] == numbers[i + 3][j - 3]:
                                diagonal += 1
            else:
                if numbers[i][j] == 1:
                    if numbers[i - 1][j + 1] != 1:
                        if numbers[i][j] == numbers[i + 1][j - 1]:
                            if numbers[i][j] == numbers[i + 2][j - 2]:
                                if numbers[i][j] == numbers[i + 3][j - 3]:
                                    diagonal += 1
    print('Διαγώνιες τετράδες:', diagonal)
    total = vertical + horizontal + diagonal
    total100 += total
print('_________________________________________________________________')
print('Συνολικές τετράδες απο όλες τις επαναλήψεις:', total100)
print('Μέσος όρος:', total100 / repetition)

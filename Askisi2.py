import random
print('Δώσε τον όρο της ακολουθίας Fibonacci:')
n = int(input('> '))
y = 0
n1 = 0
n2 = 1
while n < 0:
    print('Δώσε θετικό αριθμό')
    n = int(input('> '))
if n <= 2:
    print('ο', n, 'ος όρος δεν είναι πρώτος')
else:
    for i in range(n-1):
        nt = n1 + n2
        n1 = n2
        n2 = nt
    for i in range(20):
        a = random.randint(0, 100000)
        if (a ** nt) % nt == (a % nt):
            y += 1
        else:
            print('ο', n, 'ος όρος δεν είναι πρώτος')
            break
    if y == 20:
        print('ο', n, 'ος όρος είναι πρώτος')

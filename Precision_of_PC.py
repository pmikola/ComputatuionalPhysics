eps = 1.0
N = 20000
for i in range(N):
    eps = eps / 2
    one = 1. + eps
    sol = one - 1
    if sol <= 0.225E-15:
        print('precision =', sol )
        break
    print('eps =', eps, 'one = ', one)


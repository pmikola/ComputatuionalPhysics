under = 1.
over = 1.
loop_number = 1
while True:
    if abs(under) == float('inf'):
        break
    if abs(over) == float('inf'):
        break
    under = under / 2
    over = over * 2
    print(under,over)
    loop_number += 1
print(under,over,loop_number)
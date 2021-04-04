z = 1
while z < 3:
    for x in range(4):
        y = 3 * x - z
        print(y)
        if y >= 4:
            break
    z += 1

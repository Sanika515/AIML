def water_jug():
    x, y = 4, 3
    jug1, jug2 = 0, 0

    while jug1 != 2:
        if jug1 == 0:
            jug1 = x
        elif jug2 == y:
            jug2 = 0
        else:
            transfer = min(jug1, y-jug2)
            jug1 -= transfer
            jug2 += transfer
        print(jug1, jug2)

water_jug()
weight = float(input("Your Earth Weight: "))
planet = int(input("Your Planet Target: "))

if planet == 1:
    weight = weight * 0.38
    print('destination weight = ' + str(weight))
elif planet == 2:
    weight = weight * 0.91
    print('destination weight = ' + str(weight))
elif planet == 3:
    weight = weight * 0.38
    print('destination weight = ' + str(weight))
elif planet == 4:
    weight = weight * 2.53
    print('destination weight = ' + str(weight))
elif planet == 5:
    weight = weight * 1.07
    print('destination weight = ' + str(weight))
elif planet == 6:
    weight = weight * 0.89
    print('destination weight = ' + str(weight))
elif planet == 7:
    weight = weight * 1.14
    print('destination weight = ' + str(weight))
else:
    print('Invalid planet number')

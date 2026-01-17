month = int(input("Enter Month: "))

if month >= 1 and month <= 3:
    print('Winter 🌨️')
elif month > 3 and month <= 6:
    print('Spring 🌱')
elif month > 6 and month <= 9:
    print('Summer 🌻')
elif month > 9 and month <= 12:
    print('Autumn 🍂')
else:
    print('Invalid')
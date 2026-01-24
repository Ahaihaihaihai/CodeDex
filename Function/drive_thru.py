menu = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']

def get_item(x):
    return menu[x-1]

def welcome(x):
    print('What would you like to eat today?')
    x = int(input('1. 🍔 Cheeseburger\n2. 🍟 Fries\n3. 🥤 Soda\n4. 🍦 Ice Cream\n5. 🍪 Cookie\n'))
    return x

def main():
    number = 0
    order = welcome(number)
    order = get_item(order)
    print(f"Here is your {order}, Have a nice day!")


if __name__ == "__main__":
    main()

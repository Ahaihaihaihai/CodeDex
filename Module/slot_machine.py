# import random
# symbols = ['🍒',' 🍇', '🍉','7️⃣']

# results = random.choices(symbols, [3,3,3,1], k=3)

# print(f'{results[0]}|{results[1]}|{results[2]}')

# if results[0] == results[1] == results[2] == '7️⃣':
#     print('Jackpot! 💰')
# else:
#     print('Thanks for playing!')

import random
symbols = ['🍒',' 🍇', '🍉','7️⃣']

def play(symbols):
    results = random.choices(symbols, k=3)
    return results

keep = True
while keep:
    results = play(symbols)
    print(f'{results[0]}|{results[1]}|{results[2]}')
    if results[0] == results[1] == results[2] == '7️⃣':
        print('Jackpot! 💰')
        keep = False
    else:
        keep = input('Want to keep playing? Y or N\n')
        if keep == 'y' or keep == 'Y':
            keep = True
        else:
            keep = False

    

        


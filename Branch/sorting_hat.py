ans = int(input("Q1) Do you like Dawn or Dusk?\n  1) Dawn\n  2) Dusk\n"))
Gryffindor = Ravenclaw = Hufflepuff = Slytherin = 0
if ans == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif ans == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

ans = int(input("Q2) When I'm dead, I want people to remember me as:\n  1) The Good\n  2) The Great\n  3) The Wise\n  4) The Bold\n"))
if ans == 1:
    Hufflepuff += 2
elif ans == 2:
    Slytherin += 2
elif ans == 3:
    Ravenclaw += 2
elif ans == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

ans = int(input("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))
if ans == 1:
    Slytherin += 4
elif ans == 2:
    Hufflepuff += 4
elif ans == 3:
    Ravenclaw += 4
elif ans == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

print("🦁 Gryffindor: " + str(Gryffindor) + "\n🦅 Ravenclaw: " + str(Ravenclaw) + "\n🦡 Hufflepuff: " + str(Hufflepuff) + "\n🐍 Slytherin: " + str(Slytherin))
print("Most point: ",end=" ")
# if Gryffindor > Slytherin and Gryffindor > Ravenclaw and Gryffindor > Hufflepuff:
#     print("🦁 Gryffindor")
# elif Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
#     print("🦅 Ravenclaw")
# elif Hufflepuff > Slytherin:
#     print("🦡 Hufflepuff")
# else:
#     print("🐍 Slytherin")
max_point = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if max_point == Gryffindor:
    print("🦁 Gryffindor")
elif max_point == Ravenclaw:
    print("🦅 Ravenclaw")
elif max_point == Hufflepuff:
    print("🦡 Hufflepuff")
else:
    print("🐍 Slytherin")

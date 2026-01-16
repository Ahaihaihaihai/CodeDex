height = int(input("Your Height (cm): "))
credits = int(input("Your Credits: "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
    print("You don't have enough credits.")
else:
    print("You are not tall enough to ride and don't have enough credits.")
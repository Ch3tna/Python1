print("Which meal do you want?")
meal = input("Lunch(L) Breakfast(B) Dinner(D): ")

if meal == "L":
    food = input("North Indian (NI) or South Indian (SI): ")
    if food == "NI":
        choice = input("Chole Puri or rajma chawal enter full name case sensitive): ")
        if choice == "Chole puri" or choice == "Rajma chawal":
            print("You got", choice)
        else:
            print("Eat dirt")
    elif food == "SI":
        choice = input("Rasam rice or Chicken curry (enter full name case sensitive): ")
        if choice == "Rasam rice" or choice == "Chicken curry":
            print("You got", choice)
        else:
            print("Eat dirt")
    else:
        print("Invalid cuisine choice")
elif meal == "B":
    food = input("American(A) or Italian (I): ")
    if food == "A":
        choice = input("Hot dog or Burger (enter full name case sensitive): ")
        if choice == "Hotdog" or Burger == "Waffles":
            print("You got", choice)
        else:
            print("Eat dirt")
    elif food == "I":
        choice = input("Pizza or Pasta(enter full name case sensitive): ")
        if choice == "Pizza" or choice == "Pasta":
            print("You got", choice)
        else:
            print("Eat dirt")
    else:
        print("Invalid cuisine choice")
elif meal == "D":
    food = input("Korean (K) or Japanese (J): ")
    if food == "K":
        choice = input(" Soft Tofu Stew or Kimbap (enter full name case sensitive): ")
        if choice == "Soft Tofu Stew" or choice == "Kimbap":
            print("You got", choice)
        else:
            print("Eat dirt")
    elif food == "J":
        choice = input("Ramen or Shushi (enter full name case sensitive): ")
        if choice == "Ramen" or choice == "Shushi":
            print("You got", choice)
        else:
            print("Eat dirt")
    else:
        print("Invalid cuisine choice")
else:
    print("Sorry!")

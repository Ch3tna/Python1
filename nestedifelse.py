print("Which meal do you want?")
meal = input("Lunch(L) Breakfast(B) Dinner(D): ")

if meal == "L":
    food = input("German(G) or Arabian(A): ")
    if food == "G":
        choice = input("Döner or Brot (enter full name case sensitive): ")
        if choice == "Döner" or choice == "Brot":
            print("You got", choice)
        else:
            print("Eat dirt")
    elif food == "A":
        choice = input("Shawarma or Mandi (enter full name case sensitive): ")
        if choice == "Shawarma" or choice == "Mandi":
            print("You got", choice)
        else:
            print("Eat dirt")
    else:
        print("Invalid cuisine choice")
elif meal == "B":
    food = input("American(A) or Indian(I): ")
    if food == "A":
        choice = input("Pancakes or Waffles (enter full name case sensitive): ")
        if choice == "Pancakes" or choice == "Waffles":
            print("You got", choice)
        else:
            print("Eat dirt")
    elif food == "I":
        choice = input("Paratha or Idli (enter full name case sensitive): ")
        if choice == "Paratha" or choice == "Idli":
            print("You got", choice)
        else:
            print("Eat dirt")
    else:
        print("Invalid cuisine choice")
elif meal == "D":
    food = input("Italian(I) or Chinese(C): ")
    if food == "I":
        choice = input("Pizza or Pasta (enter full name case sensitive): ")
        if choice == "Pizza" or choice == "Pasta":
            print("You got", choice)
        else:
            print("Eat dirt")
    elif food == "C":
        choice = input("Noodles or Dumplings (enter full name case sensitive): ")
        if choice == "Noodles" or choice == "Dumplings":
            print("You got", choice)
        else:
            print("Eat dirt")
    else:
        print("Invalid cuisine choice")
else:
    print("Get out")

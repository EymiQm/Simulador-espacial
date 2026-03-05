f oxygen == 0 or health == 0:
        print("\nGAME OVER ❌")
        break

    next_day = ""

    while next_day != "1":
        next_day = input("Press 1 to go to the next day: ")
        if next_day != "1":
            print("Invalid option. Press 1 to continue.\n")

    day += 1

# =========================
    # GAME OVER
    # =========================

    if oxygen == 0 or health == 0:

        print("\nGAME OVER ❌")

        print("\n===== MISSION SUMMARY =====")
        print("Difficulty:", difficulty_name)
        print("Days survived:", day)
        print("Population:", population)

        print("\nFinal Resources:")
        print("Health:", health)
        print("Oxygen:", oxygen)
        print("Batteries:", batteries)
        print("Spare Parts:", spare_parts)

        print("\nThe colony could not survive the harsh conditions of Mars.")
        print("============================")

        break

    # =========================
    # SIGUIENTE DÍA
    # =========================

    next_day = ""

    while next_day != "1":
        next_day = input("Press 1 to go to the next day: ")
        if next_day != "1":
            print("Invalid option. Press 1 to continue.\n")

    day += 1

    current_day_index += 1
    if current_day_index > 6:
        current_day_index = 0

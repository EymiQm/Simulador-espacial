# EVITAR NEGATIVOS 

    if oxygen < 0:
        oxygen = 0
    if batteries < 0:
        batteries = 0
    if spare_parts < 0:
        spare_parts = 0
    if health < 0:
        health = 0

______________________________________

# FINAL DEL JUEGO

if day > 10 and oxygen > 0 and health > 0:

    print("\nMISSION SUCCESS 🚀")

    print("\n===== MISSION SUMMARY =====")
    print("Difficulty:", difficulty_name)
    print("Days survived: 10")
    print("Population:", population)

    print("\nFinal Resources:")
    print("Health:", health)
    print("Oxygen:", oxygen)
    print("Batteries:", batteries)
    print("Spare Parts:", spare_parts)

    print("\nThe Mars colony survived the mission successfully!")
    print("============================")

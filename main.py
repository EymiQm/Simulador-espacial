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
    print("\nMISSION SUCCESS 🚀 You survived 10 days on Mars!")

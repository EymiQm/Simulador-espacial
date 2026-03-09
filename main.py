# =========================
# CONFIGURATION ACCORDING TO LEVEL
# =========================

if difficulty == "1":
    oxygen = 100
    batteries = 100
    spare_parts = 100
    health = 100

elif difficulty == "2":
    oxygen = 75
    batteries = 75
    spare_parts = 75
    health = 75

else:
    oxygen = 50
    batteries = 50
    spare_parts = 50
    health = 50


# =========================
# INFORMACIÓN DE PARTIDA
# =========================

if difficulty == "1":
    difficulty_name = "Easy"
    event_probability = "5% - 15%"

elif difficulty == "2":
    difficulty_name = "Medium"
    event_probability = "20% - 40%"

else:
    difficulty_name = "Hard"
    event_probability = "45% - 60%"

print("\n===== GAME SETTINGS =====")
print("Difficulty:", difficulty_name)
print("Critical Event Probability:", event_probability)
print("=========================\n")

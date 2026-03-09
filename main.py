# =========================
# BUCLE PRINCIPAL 
# =========================

day = 1

while day <= 10:

    current_day = days_of_week[current_day_index]

    print("\n======================================")
    print("DAY", day, "-", current_day)
    print("======================================")
    
    print("GAME SETTINGS")
    print("Difficulty:", difficulty_name)
    print("Critical Event Probability:", event_probability)

    print("\nCOLONY STATUS")
    print("Population:", population)

    print("\nRESOURCES (Previous Day)")
    print("Health:      ", health)
    print("Oxygen:      ", oxygen)
    print("Batteries:   ", batteries)
    print("Spare Parts: ", spare_parts)

    print("======================================")

    # =========================
    # CONSUMO AUTOMÁTICO 
    # =========================

    consumption_message = "Normal resource consumption"

    if current_day == "Monday" or current_day == "Tuesday":
        consumption_message = "0.8% LESS resource consumption"

    elif current_day == "Saturday" or current_day == "Sunday":
        consumption_message = "1.4% MORE resource consumption"

    # Consumo base
    oxygen -= float(population * 2)
    health -= float(5)
    batteries -= float(5)

# Ajuste por día
    if current_day == "Monday" or current_day == "Tuesday":

        oxygen += oxygen * 0.008
        health += health * 0.008
        batteries += batteries * 0.008

    elif current_day == "Saturday" or current_day == "Sunday":

        oxygen -= oxygen * 0.014
        health -= health * 0.014
        batteries -= batteries * 0.014

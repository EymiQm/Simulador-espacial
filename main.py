import random # VERSION FINAL

# =========================
# VALIDACIÓN DE DIFICULTAD Joyner
# =========================

difficulty = ""

while difficulty != "1" and difficulty != "2" and difficulty != "3":
    print("=== MARS SURVIVAL SIMULATOR ===")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    difficulty = input("Enter option (1-3): ")
    
    if difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("Invalid option. Try again.\n")

# =========================
# CONFIGURACIÓN SEGÚN NIVEL = joel
# =========================

if difficulty == "1":
    oxygen = 100
    batteries = 100
    spare_parts = 100
    health = 100

elif difficulty == "2":
    oxygen = 95
    batteries = 90
    spare_parts = 90
    health = 90

else:
    oxygen = 90
    batteries = 60
    spare_parts = 60
    health = 70

# =========================
# INFORMACIÓN DE PARTIDA = andres
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
print("=========================")

# =========================
# POBLACIÓN ALEATORIA = emanuel
# =========================

population = random.randint(4, 6)

print("\nSurvivors assigned to the station:", population)

# =========================
# DÍA DE LA SEMANA ALEATORIO = emanuel
# =========================

days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

current_day_index = random.randint(0,6)

# =========================
# BUCLE PRINCIPAL = miguel
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
    # CONSUMO AUTOMÁTICO = miguel
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

    # =========================
    # EVENTO DEL DÍA = jhonatan
    # =========================

    event_chance = random.randint(1, 100)

    if difficulty == "1":
        critical_limit = random.randint(5, 15)

    elif difficulty == "2":
        critical_limit = random.randint(20, 40)

    else:
        critical_limit = random.randint(45, 65)

    # =========================
    # EVENTO CRÍTICO = jhonatan
    # =========================

    if event_chance <= critical_limit:

        event_type = random.randint(1, 10)

        if event_type == 1:
            print("CRITICAL EVENT: Sandstorm reduces solar charge.")
            loss = 15
            batteries -= loss
            print("Batteries -", loss)

        elif event_type == 2:
            print("CRITICAL EVENT: Oxygen leak detected.")
            loss = 10
            oxygen -= loss
            print("Oxygen -", loss)

        elif event_type == 3:
            print("CRITICAL EVENT: Crew illness spreads.")
            loss = 15
            health -= loss
            print("Health -", loss)

        elif event_type == 4:
            print("CRITICAL EVENT: Storage damage.")
            loss = 15
            spare_parts -= loss
            print("Spare Parts -", loss)

        elif event_type == 5:
            print("CRITICAL EVENT: Radiation spike.")
            loss = 20
            health -= loss
            print("Health -", loss)

        elif event_type == 6:
            print("CRITICAL EVENT: Water recycler failure.")
            loss = 10
            health -= loss
            print("Health -", loss)

        elif event_type == 7:
            print("CRITICAL EVENT: Power system malfunction.")
            loss = 20
            batteries -= loss
            print("Batteries -", loss)

        elif event_type == 8:
            print("CRITICAL EVENT: Structural crack in habitat.")
            loss = 20
            spare_parts -= loss
            print("Spare Parts -", loss)

        elif event_type == 9:
            print("CRITICAL EVENT: Food contamination.")
            loss = 10
            health -= loss
            print("Health -", loss)

        elif event_type == 10:
            print("CRITICAL EVENT: Major system overload.")

            loss_battery = 10
            batteries -= loss_battery
            print("Batteries -", loss_battery)

            loss_oxygen = 10
            oxygen -= loss_oxygen
            print("Oxygen -", loss_oxygen)

    # =========================
    # EVENTO NORMAL = camilo
    # =========================

    else:

        normal_event = random.randint(1, 10)

        if normal_event == 1:
            print("Normal Event: Beautiful Mars sunrise.")

        elif normal_event == 2:
            print("Normal Event: Crew plays board games.")

        elif normal_event == 3:
            print("Normal Event: Communication with Earth successful.")

        elif normal_event == 4:
            print("Normal Event: Routine system check completed.")

        elif normal_event == 5:
            print("Normal Event: Crew watches a movie.")

        elif normal_event == 6:
            print("Normal Event: Minor dust outside the station.")

        elif normal_event == 7:
            print("Normal Event: Exercise session completed.")

        elif normal_event == 8:
            print("Normal Event: Crew shares stories.")

        elif normal_event == 9:
            print("Normal Event: Calm and stable day.")

        elif normal_event == 10:
            print("Normal Event: Earth sends encouraging message.")

    # =========================
    # EVITAR NEGATIVOS = emy
    # =========================

    if oxygen < 0:
        oxygen = 0
    if batteries < 0:
        batteries = 0
    if spare_parts < 0:
        spare_parts = 0
    if health < 0:
        health = 0

    # =========================
    # MOSTRAR STATUS ACTUAL = andres
    # =========================

    print("\n----- STATUS AFTER EVENT -----")
    print("Population:  ", population)
    print("Consumption Modifier:", consumption_message)

    print("\nResources:")
    print("Health:      ", health)
    print("Oxygen:      ", oxygen)
    print("Batteries:   ", batteries)
    print("Spare Parts: ", spare_parts)

    print("--------------------------------")

    if oxygen <= 20:
        print("⚠ Oxygen below 20%! Lights and research shut down.")

    # =========================
    # GAME OVER = stiward 
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
    # SIGUIENTE DÍA = stiward
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

# =========================
# FINAL DEL JUEGO = 
# =========================

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

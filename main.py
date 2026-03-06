    # =========================
    # EVENTO CRÍTICO 
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


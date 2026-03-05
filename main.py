#BUCLE PRINCIPAL

while day <= 10:

    print("\n==============================")
    print("DAY:", day)
    print("==============================")

    print("Population:", population)
    print("Previous Day Status:")
    print("Health:", health)
    print("Oxygen:", oxygen)
    print("Batteries:", batteries)
    print("Spare Parts:", spare_parts)

    # CONSUMO AUTOMÁTICO

    print("\nCalculating daily consumption...")

    # consumo de oxigeno por persona
    oxygen_consumption = population * 3

    # aplicar consumo
    oxygen = oxygen - oxygen_consumption

    # consumo de salud
    health = health - 5

    # consumo de baterias
    batteries = batteries - 5

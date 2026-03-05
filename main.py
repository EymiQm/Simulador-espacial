#=========================
#Bucle Principal
#==========================

while day <= 10:

    print("\n==============================")
    print("DAY", day)
    print("==============================")
    print("Population:", population)
    print("Previous Day Status:")
    print("Health:", health)
    print("Oxygen:", oxygen)
    print("Batteries:", batteries)
    print("Spare Parts:", spare_parts)

    # =========================
    # CONSUMO AUTOMÁTICO
    # =========================

# El consumo del oxigeno se vera afectado por la poblacion
    oxygen -= population * 3
    health -= 5
    batteries -= 5

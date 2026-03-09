import random # ESTE VERSION TIENE EL PORCENTAJE DE EVENTOS CRITICOS DEPENDIENDO DEL MODO DE JUEGO

# =========================
# VALIDACIÓN DE DIFICULTAD = Joyner
# =========================

difficulty = ""

while difficulty != "1" and difficulty != "2" and difficulty != "3":
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    difficulty = input("Enter option (1, 2 o 3): ")
    
    if difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("option failed, please enter again.")

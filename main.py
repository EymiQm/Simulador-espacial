#=======================
#MOSTRAR STATUS ACTUAL 
#=======================
   
 print("\n---- CURRENT STATUS AFTER EVENT ----")
    print("Population:  ", population)
    print("Health:      ", health)
    print("Oxygen:      ", oxygen)
    print("Batteries:   ", batteries)
    print("Spare Parts: ", spare_parts)

print("----------------------------")
   
 if oxygen < 20:
     print("⚠️ Oxygen below 20%! Lights and research shut down.")

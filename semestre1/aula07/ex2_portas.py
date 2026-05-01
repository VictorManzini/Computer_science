presenca = 1
luz_amb = 1
manual = 0
if presenca and not luz_amb or manual:
    print("Luz ligada")
else:
    print("Luz desligada")
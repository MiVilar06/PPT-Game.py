Nombre1 = input("Inserte el nombre del Jugador 1: ")
Nombre2 = input("Inserte el nombre del Jugador 2: ")

Jugador1 = input("Bienvenidxs! Elige, Piedra? Papel? o Tijera? : ")
Jugador2 = input("Bienvenidxs! Elige, Piedra? Papel? o Tijera? : ")

Condicion1 = Jugador1 == "Piedra" and Jugador2 == "Tijera"
Condicion2 = Jugador1 == "Papel" and Jugador2 == "Piedra"
Condicion3 = Jugador1 == "Tijera" and Jugador2 == "Papel"

if Jugador1 == Jugador2:
    print("Ha sido un empate n.n")
elif Condicion1 or Condicion2 or Condicion3:
    print("You Win!" , Nombre1)
else:
    print("You Win!" , Nombre2)


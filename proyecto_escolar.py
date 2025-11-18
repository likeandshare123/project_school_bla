import curses
import random
import time
import os
from curses import wrapper
def limpiar():
    os.system("cls")
AHORCADO = [
    """
     ------
     |    |
          |
          |
          |
          |
     =======
    """,
        """
     ------
     |    |
     O    |
          |
          |
          |
     =======
    """,
        """
     ------
     |    |
     O    |
     |    |
          |
          |
     =======
    """,
        """
     ------
     |    |
     O    |
    /|    |
          |
          |
     =======
    """,
        """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
     =======
    """,
        """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
     =======
    """,
        """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
     =======
    """
    ]
PALABRAS = ["python","escuela","computadora","programa","ahorcado","internet","juego","teclado"]
def ahorcado():
    limpiar()
    palabra = random.choice(PALABRAS)
    letras_correctas = []
    letras_falladas = []
    intentos = 0
    while True:
        limpiar()
        print("<======> Juego del ahorcado <======>")
        print(AHORCADO[intentos])
        progreso = ""
        for letra in palabra:
            if letra in letras_correctas:
                progreso += letra + " "
            else:
                progreso += "- "
        print("Palabra : ", progreso, "\n")
        print("Letras incorrectas : ","".join(letras_falladas))
        print(f"Intentos restantes : {6 - intentos}\n")
        letra = input("Elige una letra : ").lower()
        if not letra.isalpha or len(letra) != 1:
            print("! Solo una letra.")
            time.sleep(1)
            continue
        if letra in letras_correctas or letra in letras_falladas:
            print("! Ya intentaste esa letra.")
            time.sleep(1)
            continue
        if letra in palabra:
            letras_correctas.append(letra)
        else:
            letras_falladas.append(letra)
            intentos += 1
        if all(l in letras_correctas for l in palabra):
            limpiar()
            print("¡ Ganaste !")
            print(f"la palabra era {palabra}.")
            input()
            break
        if intentos == 6:
            limpiar()
            print(AHORCADO[6])
            print("¡ Perdiste !")
            print(f"la palabra era {palabra}")
            input()
            break
def juego_vibora(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    ventana = curses.newwin(20,60,0,0) #aqui se crea la ventana y el tamaño
    ventana.keypad(True)#detecta las flechas arriba abajo y a los lados
    curses.noecho()# evita que se muestren las teclas en la pantalla
    ventana.timeout(100) #actualiza cada 100ms
    ventana.border() # pone los bordes

    vibora = [(10,30),(10,29),(10,28)]
    direccion = curses.KEY_RIGHT
    comida = (random.randint(1,18),random.randint(1,58)) #la posicion aleatoria donde se pondra la comids
    ventana.addch(comida[0],comida[1],"O")#añadir la comida con sus parametros
    while True:
        tecla = ventana.getch()
        if tecla != -1:
            if tecla in [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT]:
                direccion = tecla
        cabeza = vibora[0]
        if direccion == curses.KEY_UP:
            nueva = (cabeza[0] - 1,cabeza[1])
        elif direccion == curses.KEY_DOWN:
            nueva = (cabeza[0] + 1,cabeza[1])
        elif direccion == curses.KEY_LEFT:
            nueva = (cabeza[0], cabeza[1] - 1)
        else:
            nueva = (cabeza[0], cabeza[1] + 1)

        if (nueva[0] == 0 or nueva[0] == 19 or nueva[1] == 0 or nueva[1] == 59):
            break
        
        if nueva in vibora:
            break

        vibora.insert(0,nueva)

        if nueva == comida:
            comida = (random.randint(1,18),random.randint(1,58))
            ventana.addch(comida[0],comida[1],"O")
        else:
            cola = vibora.pop()
            ventana.addch(cola[0],cola[1]," ")

        ventana.addch(vibora[0][0],vibora[0][1],"#")

    curses.endwin()
    limpiar()
    print("GAME OVER.")
    input("Presiona Enter para continuar...")

def juego_ppt():
    limpiar()
    opciones = ["piedra","papel","tijera"]
    print("""
<========> Juego de piedra papel o tijera <========>
Elige una opcion :
(1) Piedra.
(2) Papel.
(3) Tijera.
<==================================================>
""")
    jugador = input("<=]==> ")
    if jugador not in ["1","2","3"]:
        print("[-] opcion no valida.")
        return
    jugador = opciones[int(jugador) - 1]
    computadora = random.choice(opciones)
    limpiar()
    print(f"Tu  elegiste : {jugador}")
    print(f"La computadora elegio : {computadora}")

    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel") :
        print("[+] Ganaste.")
        input()
    else:
        print("[-]perdiste")
        input()
        


    
def menu():
    while True :
        limpiar()
        print("""
+---------[ Menu de juegos ]---------+
|------------------------------------|
| (1) Juego del snake.               |
| (2) Juego del ahorcado.            |
| (3) Piedra papel o tijera.         |
| (4) Salir.                         |
|------------------------------------|
+------------------------------------+
""")
        opcion = input(" Eliga una opcion >> ")
        if opcion == "1" :
            wrapper(juego_vibora)
        elif opcion == "2" :
            ahorcado()
        elif opcion == "3" :
            juego_ppt()
        else:
            print("[*] Saliendo...")
            exit()
menu()

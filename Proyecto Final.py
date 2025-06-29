# Variables para estadísticas
estadisticas = {
    "computadora": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
    "multijugador": {"jugador1": 0, "jugador2": 0, "empatadas": 0}
}

ultima_partida = {"modo": None, "resultado": None}

def mostrar_menu_principal():
    print("\n¡Bienvenido a Piedra, Papel o Tijera!")
    print("1. Contra la computadora")
    print("2. Multijugador (2 jugadores)")
    print("3. Ver estadísticas de la última partida")
    print("4. Salir")

def mostrar_opciones_juego():
    print("\nElige:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

def obtener_opcion_jugador(jugador):
    while True:
        opcion = input(f"{jugador}, ingresa tu elección (1-3): ")
        if opcion in ["1", "2", "3"]:
            return int(opcion)
        print("Opción inválida. Intenta de nuevo.")

def jugar_contra_computadora():
    mostrar_opciones_juego()
    jugada_jugador = obtener_opcion_jugador("Jugador")
    
    import random
    jugada_pc = random.randint(1, 3)

    if jugada_jugador == jugada_pc:
        resultado = "Empate"
        estadisticas["computadora"]["empatadas"] += 1
    elif (jugada_jugador == 1 and jugada_pc == 3) or \
         (jugada_jugador == 2 and jugada_pc == 1) or \
         (jugada_jugador == 3 and jugada_pc == 2):
        resultado = "¡Ganaste!"
        estadisticas["computadora"]["perdidas"] += 1
    else:
        resultado = "¡Perdiste!"
        estadisticas["computadora"]["ganadas"] += 1

    print(f"\n{resultado}")
    print(f"La computadora eligió: {jugada_pc}")
    
    ultima_partida["modo"] = "computadora"
    ultima_partida["resultado"] = resultado

def jugar_multijugador():
    mostrar_opciones_juego()
    jugada1 = obtener_opcion_jugador("Jugador 1")
    jugada2 = obtener_opcion_jugador("Jugador 2")

    if jugada1 == jugada2:
        resultado = "¡Empate!"
        estadisticas["multijugador"]["empatadas"] += 1
    elif (jugada1 == 1 and jugada2 == 3) or \
         (jugada1 == 2 and jugada2 == 1) or \
         (jugada1 == 3 and jugada2 == 2):
        resultado = "¡Jugador 1 gana!"
        estadisticas["multijugador"]["jugador1"] += 1
    else:
        resultado = "¡Jugador 2 gana!"
        estadisticas["multijugador"]["jugador2"] += 1

    print(f"\n{resultado}")
    
    ultima_partida["modo"] = "multijugador"
    ultima_partida["resultado"] = resultado

def mostrar_estadisticas():
    if not ultima_partida["modo"]:
        print("\nNo hay datos de partidas anteriores.")
        return
    
    print("\nEstadísticas de la última partida:")
    print(f"Modo: {ultima_partida['modo']}")
    print(f"Resultado: {ultima_partida['resultado']}")
    
    if ultima_partida["modo"] == "computadora":
        print("\nEstadísticas contra computadora:")
        print(f"Ganadas: {estadisticas['computadora']['ganadas']}")
        print(f"Perdidas: {estadisticas['computadora']['perdidas']}")
        print(f"Empates: {estadisticas['computadora']['empatadas']}")
    else:
        print("\nEstadísticas multijugador:")
        print(f"Jugador 1: {estadisticas['multijugador']['jugador1']} victorias")
        print(f"Jugador 2: {estadisticas['multijugador']['jugador2']} victorias")
        print(f"Empates: {estadisticas['multijugador']['empatadas']}")

def main():
    jugando = True
    while jugando:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            jugar_contra_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            jugando = False
        else:
            print("Opción inválida. Intenta de nuevo.")
    
    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main()
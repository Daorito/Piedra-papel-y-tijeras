import random

def game():
    # Lista de opciones
    options = ['piedra', 'papel', 'tijeras']

    # Preguntar al usuario su elección
    user_choice = input("Elige piedra, papel o tijeras: ").lower()

    # Validar la elección del usuario
    if user_choice not in options:
        print("Esa opción no es válida.")
        return

    # Elección aleatoria de la computadora
    computer_choice = random.choice(options)
    print(f'El ordenador eligió {computer_choice}')

    # Comparar las elecciones y determinar el ganador
    if user_choice == computer_choice:
        print("Empate.")
    elif user_choice == 'piedra' and computer_choice == 'tijeras':
        print("Ganaste.")
    elif user_choice == 'papel' and computer_choice == 'piedra':
        print("Ganaste.")
    elif user_choice == 'tijeras' and computer_choice == 'papel':
        print("Ganaste.")
    else:
        print("Perdiste.")

# Ejecutar el juego
game()

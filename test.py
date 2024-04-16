import random

def get_user_choice():
    while True:
        user_choice = input("Wybierz kamień (k), papier (p) lub nożyce (n): ").lower()
        if user_choice in ['k', 'p', 'n']:
            return user_choice
        else:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")

def get_computer_choice():
    return random.choice(['k', 'p', 'n'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Remis!"
    elif (user_choice == 'k' and computer_choice == 'n') or \
         (user_choice == 'p' and computer_choice == 'k') or \
         (user_choice == 'n' and computer_choice == 'p'):
        return "Gratulacje! Wygrałeś!"
    else:
        return "Komputer wygrał!"

def main():
    print("Witaj w grze Kamień, papier, nożyce!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("Twój wybór:", user_choice)
        print("Wybór komputera:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
        if play_again != 't':
            print("Dziękujemy za grę!")
            break

if __name__ == "__main__":
    main()

    #Warunek if __name__ == "__main__": jest używany, aby upewnić się, że funkcja main() zostanie wykonana tylko wtedy, gdy plik zostanie uruchomiony bezpośrednio, a nie gdy zostanie zaimportowany jako moduł do innego skryptu.
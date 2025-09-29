import random

def guess_number_game():
    # Настройки игры
    min_number = 1
    max_number = 100
    max_attempts = 7
    
    # Загадываем число
    secret_number = random.randint(min_number, max_number)
    attempts = 0
    
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от {min_number} до {max_number}. У вас есть {max_attempts} попыток.")
    
    while attempts < max_attempts:
        try:
            # Получаем ввод от пользователя
            guess = int(input("Введите ваше число: "))
            
            # Проверяем корректность ввода
            if guess < min_number or guess > max_number:
                print(f"Пожалуйста, введите число в диапазоне от {min_number} до {max_number}.")
                continue
                
            attempts += 1
            
            # Проверяем угаданное число
            if guess < secret_number:
                print("Загаданное число больше!")
            elif guess > secret_number:
                print("Загаданное число меньше!")
            else:
                print(f"Поздравляем! Вы угадали число за {attempts} попыток!")
                return
                
            # Показываем оставшиеся попытки
            print(f"Осталось попыток: {max_attempts - attempts}")
            
        except ValueError:
            print("Ошибка! Введите, пожалуйста, целое число.")
            
    # Если попытки закончились
    print(f"Игра окончена! Вы не угадали число. Было загадано: {secret_number}")

if __name__ == "__main__":
    guess_number_game()
    while input("Хотите сыграть ещё раз? (да/нет): ").lower() == "да":
        guess_number_game()

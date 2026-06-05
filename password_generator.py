import random
import string

def generate_password(length=12):
    # Набір символів: великі, малі, цифри та спецсимволи
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерація випадкового пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Використання
print("Згенерований пароль:", generate_password(16))

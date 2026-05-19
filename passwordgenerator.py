import random

def generate_password(length):
    characters = "hgeyiau7ueah"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

password_length = 8
generated_password = generate_password(password_length)
print(generated_password)


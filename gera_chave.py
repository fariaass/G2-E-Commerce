import secrets

length = 50
chars = 'ABCDEFGHIJKLMNOPQRSTUVXWZabcdefghijklmnopqrstuvwxyz0123456789'

secret_key = ''.join(secrets.choice(chars) for i in range(length))

print(secret_key)


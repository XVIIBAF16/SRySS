import base64
from cryptography.fernet import Fernet

# The encrypted payload (from your provided code)
payload = b'gAAAAABkzWGWvEp8gLI9AcIn5o-ahDUwkTvM6EwF7YYMZlE-_Gf9rcNYjxIgX4b0ltY6bcxKarib2ds6POclRwCwhsRb1LOXVt4Q3ePtMY4BmHFFZlIHLk05CjwigT7hiI9p3sH9e7Cpk1uO90xbHbuy-mfi3nkmn411aBgwxyWpJvykpkuBIG_nty6zbox3UhbB85TOis0TgM0zG4ht0-GUW4wTq2_5-wkw3kV1ZAisLJHzF-Z9oLMmwFZU0UCAcHaBTGDF5BnVLmUeCGTgzVLSNn6BmB61Yg=='

# The key in base64 (it was provided in the script)
key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())

# Use Fernet to decrypt the payload
f = Fernet(key_base64)

# Decrypt the payload
plain = f.decrypt(payload)

# The decrypted content is executed by the original script
# Let's print the decrypted string to see what it contains
print(plain.decode())


# Fixed key: shuffled alphabet
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Get message from user
text = input("Enter message: ")
encrypted = ""

# Encrypt each character
for ch in text:
    if ch.isupper():
        encrypted += key[ord(ch) - ord('A')]
    elif ch.islower():
        encrypted += key[ord(ch.upper()) - ord('A')].lower()
    else:
        encrypted += ch

# Show result
print("Encrypted message:", encrypted)

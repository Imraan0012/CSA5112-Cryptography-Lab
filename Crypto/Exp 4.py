# Get input from user
text = input("Enter message: ").upper()
key = input("Enter key: ").upper()

encrypted = ""
key_index = 0

for char in text:
    if char.isalpha():
        shift = ord(key[key_index % len(key)]) - ord('A')
        encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        key_index += 1
    else:
        encrypted += char

print("Encrypted message:", encrypted)

text = input("Message: ").upper()
a = int(input("a (must be coprime with 26): "))
b = int(input("b (0–25): "))

if a in [1,3,5,7,9,11,15,17,19,21,23,25]:
    encrypted = ""
    for ch in text:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            encrypted += chr(c + ord('A'))
        else:
            encrypted += ch
    print("Encrypted:", encrypted)
else:
    print("Invalid 'a': must be coprime with 26")

text = input("Enter message: ")        # Ask the user to type a message
key = int(input("Enter shift (1-25): "))  # Ask how many letters to shift

encrypted = ""  # Start with an empty string to build the result

for c in text:  # Go through each character in the message
    if c.isupper():  # If it's an uppercase letter (A-Z)
        encrypted += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
    elif c.islower():  # If it's a lowercase letter (a-z)
        encrypted += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
    else:  # If it's not a letter (like space or punctuation)
        encrypted += c  # Just add it as it is

print("Encrypted message:", encrypted)  # Show the final encrypted message

text = input("Enter ciphertext: ").upper()

C1, C2 = ord('B') - 65, ord('U') - 65
P1, P2 = ord('E') - 65, ord('T') - 65

for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
    b = (C1 - a * P1) % 26
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    print(f"\na = {a}, b = {b}")
    for ch in text:
        if ch.isalpha():
            c = ord(ch) - 65
            p = (a_inv * (c - b)) % 26
            print(chr(p + 65), end="")
        else:
            print(ch, end="")

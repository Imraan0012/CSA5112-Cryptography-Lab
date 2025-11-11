import string

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J merged into I

def normalize_keyword(keyword: str) -> str:
    s, seen = [], set()
    for ch in keyword.upper():
        if ch.isalpha():
            ch = 'I' if ch == 'J' else ch
            if ch not in seen:
                s.append(ch)
                seen.add(ch)
    return "".join(s)

def build_key_square(keyword: str):
    key = normalize_keyword(keyword)
    for ch in ALPHABET:
        if ch not in key:
            key += ch
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    return matrix, pos

def print_square(matrix):
    print("\nKey Square (I/J combined):")
    for row in matrix:
        print(" ".join(row))
    print()

def prepare_text(text: str) -> str:
    out = []
    for ch in text.upper():
        if ch.isalpha():
            out.append('I' if ch == 'J' else ch)
    return "".join(out)

def make_digraphs_for_encryption(clean: str):
    pairs, i = [], 0
    while i < len(clean):
        a = clean[i]
        if i + 1 == len(clean):
            filler = 'X' if a != 'X' else 'Q'
            pairs.append((a, filler))
            i += 1
        else:
            b = clean[i+1]
            if a == b:
                filler = 'X' if a != 'X' else 'Q'
                pairs.append((a, filler))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
    return pairs

def chunk_pairs_for_decryption(text: str):
    clean = prepare_text(text)
    if len(clean) % 2 != 0:
        clean += 'X'
    return [(clean[i], clean[i+1]) for i in range(0, len(clean), 2)]

def enc_pair(a, b, pos, matrix):
    ra, ca = pos[a]
    rb, cb = pos[b]
    if ra == rb:
        return matrix[ra][(ca + 1) % 5], matrix[rb][(cb + 1) % 5]
    if ca == cb:
        return matrix[(ra + 1) % 5][ca], matrix[(rb + 1) % 5][cb]
    return matrix[ra][cb], matrix[rb][ca]

def dec_pair(a, b, pos, matrix):
    ra, ca = pos[a]
    rb, cb = pos[b]
    if ra == rb:
        return matrix[ra][(ca - 1) % 5], matrix[rb][(cb - 1) % 5]
    if ca == cb:
        return matrix[(ra - 1) % 5][ca], matrix[(rb - 1) % 5][cb]
    return matrix[ra][cb], matrix[rb][ca]

def playfair_encrypt(plaintext: str, keyword: str) -> str:
    matrix, pos = build_key_square(keyword)
    clean = prepare_text(plaintext)
    pairs = make_digraphs_for_encryption(clean)
    out = []
    for a, b in pairs:
        ea, eb = enc_pair(a, b, pos, matrix)
        out.append(ea + eb)
    return "".join(out)

def playfair_decrypt(ciphertext: str, keyword: str) -> str:
    matrix, pos = build_key_square(keyword)
    pairs = chunk_pairs_for_decryption(ciphertext)
    out = []
    for a, b in pairs:
        da, db = dec_pair(a, b, pos, matrix)
        out.append(da + db)
    return "".join(out)

# --- Interactive I/O ---
if __name__ == "__main__":
    print("Playfair Cipher (I/J combined)")
    mode = input("Mode (E=encrypt, D=decrypt): ").strip().upper()
    keyword = input("Keyword: ").strip()
    text = input("Text: ").strip()

    matrix, _ = build_key_square(keyword)
    print_square(matrix)

    if mode == 'E':
        result = playfair_encrypt(text, keyword)
        print("Ciphertext:", result)
    elif mode == 'D':
        result = playfair_decrypt(text, keyword)
        print("Decrypted (J→I):", result)
    else:
        print("Invalid mode. Use E or D.")

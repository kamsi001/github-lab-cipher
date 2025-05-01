import sys

def caesar_cipher(text, shift):
    result = ""
    text = text.upper()
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
    return result

if name == "main":
    shift = int(sys.argv(1))
    message = sys.stdin.read()
    encrypted = caesar_cipher(message, shift)

    # print in blocks of 5, 10 per line
    for i in range(0, len(encrypted), 5):
        print(encrypted(i:i+5), end=' ')
        if (i // 5 + 1) % 10 == 0:
            print()
def caesar_cipher(text, shift=13):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

def main():
    text = input("Enter the text to encrypt/decrypt: ")
    encrypted_text = caesar_cipher(text)
    print("Result:", encrypted_text)

if __name__ == "__main__":
    main()

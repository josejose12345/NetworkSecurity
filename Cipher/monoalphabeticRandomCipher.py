import random

def generate_cipher_map():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)
    return {chr(65+i): cipher for i, cipher in enumerate(alphabet)}

def permutation_cipher(text, cipher_map):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += cipher_map[char.upper()].lower()
            else:
                result += cipher_map[char]
        else:
            result += char
    return result

def main():
    text = input("Enter the text to encrypt: ")
    
    # Generate the cipher map
    cipher_map = generate_cipher_map()
    print("Cipher Map:")
    for key, value in cipher_map.items():
        print(f"{key} -> {value}")

    # Encrypt the text using the generated cipher map
    encrypted_text = permutation_cipher(text, cipher_map)
    print("\nEncrypted Text:")
    print(encrypted_text)

if __name__ == "__main__":
    main()

# cesar.py

def cesar(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # mantiene espacios y otros caracteres
    return result

if __name__ == "__main__":
    print("=== Cifrado César ===")
    texto = input("Ingresa el texto a cifrar: ")
    desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))

    texto_cifrado = cesar(texto, desplazamiento)
    print(f"\n🔐 Texto cifrado: {texto_cifrado}")

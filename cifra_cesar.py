def cifra_cesar(texto, deslocamento):
    """Implementa a cifra de César para criptografar texto."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_base = 65 if char.isupper() else 97
            resultado += chr((ord(char) - ascii_base + deslocamento) % 26 + ascii_base)
        else:
            resultado += char
    return resultado

# Exemplo de uso
if __name__ == "__main__":
    texto = "Hello World"
    deslocamento = 3
    cifrado = cifra_cesar(texto, deslocamento)
    print(f"Texto original: {texto}")
    print(f"Texto cifrado: {cifrado}")

import unicodedata

def remove_acento(s):
    nfkd = unicodedata.normalize('NFD', s)
    return ''.join(ch for ch in nfkd if not unicodedata.combining(ch))

def shift_char(c, k):
    if 'A' <= c <= 'Z':
        base = ord('A')
        return chr((ord(c) - base + k) % 26 + base)
    if 'a' <= c <= 'z':
        base = ord('a')
        return chr((ord(c) - base + k) % 26 + base)
    return c

def caesar(text, k):
    k = k % 26
    return ''.join(shift_char(c, k) for c in text)

def main():
    modo = input("Modo (e = cifrar / d = decifrar): ").strip().lower()
    texto = input("Texto: ")
    try:
        k = int(input("Chave k (número inteiro): ").strip())
    except ValueError:
        print("Chave inválida. Use um número inteiro.")
        return

    opt = input("Remover acentos antes (s/n)? ").strip().lower()
    if opt == 's':
        texto_proc = remove_acento(texto)
    else:
        texto_proc = texto

    if modo == 'd':
        k = -k

    resultado = caesar(texto_proc, k)
    print("\nResultado:")
    print(resultado)

if __name__ == "__main__":
    main()

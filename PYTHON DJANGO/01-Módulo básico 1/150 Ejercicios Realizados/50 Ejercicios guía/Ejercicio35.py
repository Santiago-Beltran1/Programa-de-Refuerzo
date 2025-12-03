from collections import Counter
import heapq

class NodoHuffman:
    """Nodo para el árbol de codificación Huffman"""
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def comprimir_repeticion_simple(texto):
    """
    Compresión simple: reemplaza secuencias repetidas
    Ejemplo: "aaaa" -> "4a"
    """
    if not texto:
        return ""

    resultado = []
    contador = 1
    anterior = texto[0]

    for char in texto[1:]:
        if char == anterior:
            contador += 1
        else:
            if contador > 1:
                resultado.append(str(contador) + anterior)
            else:
                resultado.append(anterior)
            anterior = char
            contador = 1
    # Añadir la última secuencia
    if contador > 1:
        resultado.append(str(contador) + anterior)
    else:
        resultado.append(anterior)

    comprimido = ''.join(resultado)
    print(f"Texto original: {texto}")
    print(f"Texto comprimido (repetición simple): {comprimido}")
    return comprimido

# Ejemplo de uso
if __name__ == "__main__":
    texto = "aaabbcddddde"
    comprimir_repeticion_simple(texto)

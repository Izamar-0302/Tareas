import heapq
from collections import defaultdict, Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def create_huffman_codes(root, code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code

    create_huffman_codes(root.left, code + "0", codes)
    create_huffman_codes(root.right, code + "1", codes)

    return codes


def encode(text, codes):
    return ''.join(codes[char] for char in text)


def decode(binary, root):
    decoded_text = []
    current = root

    for bit in binary:
        current = current.left if bit == "0" else current.right

        if current.char is not None:
            decoded_text.append(current.char)
            current = root

    return ''.join(decoded_text)


def print_huffman_tree(node, indent=0):
    if node is None:
        return
    print("  " * indent + (node.char if node.char else "*") + f" ({node.freq})")
    print_huffman_tree(node.left, indent + 1)
    print_huffman_tree(node.right, indent + 1)


# Función principal
def main():
    text = input("Ingrese el mensaje de texto: ")
    if not text:
        print("El mensaje no puede estar vacío.")
        return

    print("\nConstruyendo el árbol de Huffman...")
    root = build_huffman_tree(text)
    
    print("\nÁrbol de Huffman:")
    print_huffman_tree(root)

    print("\nCreando tabla de códigos...")
    codes = create_huffman_codes(root)
    print("Tabla de códigos:")
    for char, code in codes.items():
        print(f"'{char}': {code}")

    print("\nCodificando el mensaje...")
    binary_message = encode(text, codes)
    print(f"Mensaje codificado: {binary_message}")
    print(f"Número de bits en el mensaje codificado: {len(binary_message)}")
    print(f"Número de caracteres en el mensaje original: {len(text)}")

    print("\nDecodificando el mensaje...")
    decoded_message = decode(binary_message, root)
    print(f"Mensaje decodificado: {decoded_message}")

    assert decoded_message == text, "El mensaje decodificado no coincide con el original."


if __name__ == "__main__":
    main()

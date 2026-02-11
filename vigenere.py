import matplotlib.pyplot as plt
from collections import Counter

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
MODULE = len(ALPHABET)

#Funciones para graficar frecuencias en histograma (librerías Matplotlib y Collections)

def get_frequency(text):
   """Genera el histograma de frecuencias de un texto"""
   print("Hola")
   text = "".join(filter(str.isalpha, text.upper()))
   count = Counter(text)
   total = sum(count.values())
   return {k: v/total for k, v in count.items()}

def plot_distribution(text, title):
   """Grafica la distribución de letras"""
   freqs = get_frequency(text)
   letters = sorted(list(ALPHABET))
   values = [freqs.get(l, 0) for l in letters]
   
   plt.figure(figsize=(10, 5))
   plt.bar(letters, values)
   plt.title(title)
   plt.ylabel('Frecuencia')
   plt.show()
   

#Funciones para desencriptar César y Vigenère

def caesar_brute_force(ciphertext, shift):
   """Imprime todos los posibles desplazamientos César"""
   ciphertext = ciphertext.upper()
   decrypted = ""
   for char in ciphertext:
       if char in ALPHABET:
           idx = ALPHABET.index(char)
           nidx = (idx-shift) if (idx-shift)>=0 else (idx-shift-1)
           decrypted += ALPHABET[nidx % MODULE]
       else:
           decrypted += char
       # Muestra solo los primeros 50 caracteres para revisión rápida
   print(f"Corrimiento {shift}: {decrypted[:50]}...")

def Vigenère_decrypt(ciphertext, key):
   """Descifra Vigenère dada una clave"""
   decrypted = []
   key = key.upper()
   key_idx = 0
   ciphertext = ciphertext.upper()
   
   for char in ciphertext:
       if char in ALPHABET:
           shift = ALPHABET.index(key[key_idx % len(key)])
           idx = ALPHABET.index(char)
           nidx = (idx-shift) if (idx-shift)>=0 else (idx-shift-1)
           decrypted_char = ALPHABET[nidx % MODULE]
           decrypted.append(decrypted_char)
           key_idx += 1
       else:
           decrypted.append(char)
   return "".join(decrypted)

if __name__ == "__main__":
    # Ejemplo 1: Análisis de frecuencias
    #texto_prueba = "Hola mundo, este es un texto de prueba para ver la distribución de frecuencias"
    #plot_distribution(texto_prueba, "Distribución de Frecuencias - Texto de Prueba")

    mensaje_cifrado = "RHZJHAHYHAHZKLONBHGBZLLTJBLTAYHTLTHYNLTAOTH"
    for shift in range(1, MODULE):
        caesar_brute_force(mensaje_cifrado, shift)
        if shift >= 29:  # Limitar para prueba
            break

    mensaje_vigenere = "LHÑDOKGARJRSHFMNRTIOLNMVNJQGTWMWLHGLR"
    clave = "HTML"
    descifrado = Vigenère_decrypt(mensaje_vigenere, clave)
    print(f"\nMensaje descifrado con Vigenère: {descifrado}")
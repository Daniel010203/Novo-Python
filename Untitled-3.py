texto = input("Informe o texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper()in VOGAIS:
        print(letra,end="")
else:
    print("Favor digite vogais.")

for numero in range(0,51,5):
    print(numero,end="")

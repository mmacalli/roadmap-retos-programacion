"""
operaciones
"""
from sqlalchemy import values

s1 = "aqui estamos"
s2 = "comandante programador "

#concatenacion
print(s1 + "," + s2 + "!")

#repeticion
print(s1 * 3)

#indexacio
print(s1[0] + s1[1] + s1[2] + s1[3])



#longitud
print(len(s2))

#slicing (porcion)
print(s2 [2:5])

#Busqueda
print("o" in s1)
print("3" in s2)

#reemplazo
print(s2.replace("c", "a"))

#division
print(s2.split("a"))

#mayusculas y minusculas

print(s2.upper())
print(s2.lower())
print("hola gury".title())
print("hola gury".capitalize())

#eliminacion de espacios al principio y al final

print(" hola gury".strip() + "loquito")

#busqueda al principio y al final
print(s2.startswith("co"))
print(s2.startswith("de"))
print(s2.endswith("co"))
print(s2.endswith("lll"))

s3 = "Martin el perro salvaje"

#busqueda de posicion
print(s3.find("perro"))
print(s3.find("Martin"))
print(s3.find("a"))
print(s3.lower().find("j"))

#busqueda de ocurrencias
print(s3.lower().count("r"))

#formateo
print("saludo {}, lenguaje {}!".format(s1,s2))
#interpolacion
print(f"saludo {s1}, lenguaje {s3}!")
#transformacio
print(list (s3))
#tranformacion de lista en cadena
l1 = [ s1 ," Pedro ", s3, "eee"]
print("".join(l1))

#tranformancionas numericas
s4= "12345"
s4 = int(s4)
print(s4)

s5 = "12345"
s5 = float(s5)
print(s5)

#comprobacion
s4= "12345"
print(s4.isalnum())
print(s2.isalpha())
print(s1.isalpha())
print(s4.isalpha())

"""
extras
"""

def check(word1: str, word2: str):

    #palindromos
    print(f"¿{word1}es un palindromo ?: {word1 == word1[::-1]}")
    print(f"¿{word2}es un palindromo ?: {word2 == word2[::-1]}")
    #anagrama
    print(f"¿{word1}es un anagrama de {word2}?: {sorted(word1) == sorted((word2))}")
    #isograma
    print(f"¿{word1}es un isograma? {len(word1) == len(set(word1))}?")
    print(f"¿{word2}es un isograma? {len(word2) == len(set(word2))}?")

    word_dict = dict()
    for word in word1:
        word_dict[word] = word_dict.get(word,0) + 1

    isogram = True
    values = list(word_dict.values())
    for word in values:
        if word_count != isogram_len:
            isogram = False
            break

    print(word_dict)


check("radar" ,"pipiri")
check("mijo","jomi")
check("radar" ,"pythonpython")

def inverter_string(s):
    lista_chars = list(s)
    inicio = 0
    fim = len(lista_chars) - 1
    
    while inicio < fim:
        lista_chars[inicio], lista_chars[fim] = lista_chars[fim], lista_chars[inicio]
        inicio += 1
        fim -= 1  

    return (lista_chars)

entrada_usuario = input("Digite a string para inverter: ")

resultado = inverter_string(entrada_usuario)
print("String invertida:", resultado)

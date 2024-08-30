texto_minusculo = input("Digite uma string: ").lower()

if 'a' in texto_minusculo:
    quantidade_a = texto_minusculo.count('a')
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
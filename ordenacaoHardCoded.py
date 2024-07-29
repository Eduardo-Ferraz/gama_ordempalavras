
def ordenar_por_frequencia(palavras, caracter):
    caracter_lower = caracter.lower()
    palavras_ordenadas = sorted(palavras, key=lambda palavra: palavra.lower().count(caracter_lower), reverse=True)
    return palavras_ordenadas

# Exemplo de uso
caracter = 'a'

palavras1 = ["Gama", "Matematica", "Vestibular", "IA"]
resultado1 = ordenar_por_frequencia(palavras1, caracter)
print(resultado1)

# Exemplo de uso 2 com o mesmo caracter
palavras2 = ["Teste", "Testando", "123", "Palavras", "Girafa", "Gato", "Galinha"]
resultado2 = ordenar_por_frequencia(palavras2, caracter)
print(resultado2)
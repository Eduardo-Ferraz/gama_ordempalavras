def ordenar_por_frequencia(palavras, caracter):
    caracter_lower = caracter.lower()
    palavras_ordenadas = sorted(palavras, key=lambda palavra: palavra.lower().count(caracter_lower), reverse=True)
    return palavras_ordenadas

def receber_dados():
    caracter = input("Digite o caractere para ordenar as palavras pela frequência do caractere! (ou pressione Enter para sair): ").strip()
    if not caracter:
        return None, None
    palavras = input("Digite as palavras separadas por espaço (ou pressione Enter para sair): ").strip().split()
    if not palavras:
        return None, None
    return palavras, caracter

while True:
    palavras, caracter = receber_dados()
    if palavras is None or caracter is None:
        break
    resultado = ordenar_por_frequencia(palavras, caracter)
    print("Palavras ordenadas:", resultado)

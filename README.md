# Ordenação de Palavras por Frequência de Caracteres
Ordenação de lista de palavras com base na frequência do caractere fornecido de forma otimizada e eficiente.

```
def ordenar_por_frequencia(palavras, caracter):
    caracter_lower = caracter.lower()
    palavras_ordenadas = sorted(palavras, key=lambda palavra: palavra.lower().count(caracter_lower), reverse=True)
    return palavras_ordenadas
```

## Descrição do Código

A função _ordenar_por_frequencia_ recebe como parâmetros um array de palavras e o caracter em questão a ser avaliado para a ordenação.

A função sorted() é usada para ordenar a lista de palavras:
- key=lambda palavra: palavra.lower().count(caracter_lower): Este é o critério de ordenação.
  - palavra.lower(): Cada palavra é convertida para minúsculas para que a contagem do caractere não leve isso em consideração.
  - count(caracter_lower): O método count é chamado na palavra convertida para minúsculas contando quantas vezes o caracter_lower aparece.
- reverse=True: Ordenação deve ser em ordem decrescente para que as palavras com maior frequência do caractere apareçam primeiro na lista.

Dessa forma, o código retorna as palavras na ordem correta cumprindo os requisitos. É possível observar exemplos de uso executando os arquivos ordenacaoHardCoded.py ou ordenacaoComInputs.py
Ao executar o primeiro, são utilizados dados de amostra padrão os 2 seguintes casos de uso:

```
caracter = 'a'

palavras1 = ["Gama", "Matematica", "Vestibular", "IA"]
resultado1 = ordenar_por_frequencia(palavras1, caracter)
print(resultado1)

# Exemplo de uso 2 com o mesmo caracter
palavras2 = ["Teste", "Testando", "123", "Palavras", "Girafa", "Gato", "Galinha"]
resultado2 = ordenar_por_frequencia(palavras2, caracter)
print(resultado2)
```
Resposta:
['Matematica', 'Gama', 'Vestibular', 'IA']
['Palavras', 'Girafa', 'Galinha', 'Testando', 'Gato', 'Teste', '123']

No segundo caso, ordenacaoComInputs.py roda pedindo novos conjuntos de dados ao usuário até que ele deseje sair da aplicação, apertando Enter sem enviar os dados pedidos.

print("Bem-vindo ao programa de análise das temperaturas de julho")
print()

#entrada de dados
arquivo = open("banco-temperaturas-julho.txt", "r")

registros = []

for linha in arquivo:
    partes = linha.strip().split("\t")
    registro = (partes[0], float(partes[1]))
    registros.append(registro)

arquivo.close()

#processamento e saída de dados
total_linhas = len(registros)
soma = 0
minima = registros[0][1]
maxima = registros[0][1]
data_minima = registros[0][0]

for data, temperatura in registros:
    soma += temperatura

    if temperatura < minima:
        minima = temperatura
        data_minima = data

    if temperatura > maxima:
        maxima = temperatura

media = soma / total_linhas

print(f"O arquivo possui {total_linhas} linhas")
print(f"A média das temperaturas é {media:.2f}")
print(f"A temperatura minima é {minima} e a máxima é {maxima}")
print(f"A temperatura mínima foi registrada pela primeira vez em {data_minima}")
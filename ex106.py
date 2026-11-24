#apresentação
print("Bem-vindo ao programa de temperaturas de um dia de julho")
print()

#entrada de dados
dia = input("Informe a data (aaaa-mm-dd): ")

arquivo = open("banco-temperaturas-julho.txt", "r")

dias = {}

for linha in arquivo:
    partes = linha.strip().split("\t")
    data = partes[0].split(" ")[0]
    temperatura = float(partes[1])

    if data in dias:
        minima, maxima = dias[data]

        if temperatura < minima:
            minima = temperatura

        if temperatura > maxima:
            maxima = temperatura

        dias[data] = (minima, maxima)

    else:
        dias[data] = (temperatura, temperatura)

arquivo.close()

#processamento e saída de dados
if dia in dias:
    minima, maxima = dias[dia]
    amplitude = maxima - minima

    print(f"Temperatura mínima do dia {dia}: {minima}")
    print(f"Temperatura máxima do dia {dia}: {maxima}")
    print(f"Amplitude térmica: {amplitude:.2f}")

else:
    print(f"O dia {dia} não está presente no arquivo")
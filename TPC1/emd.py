import os

# abrir o ficheiro csv
with open("emd.csv", "r", encoding="utf-8") as file:
    dataset = file.read()

# criar ficheiro de texto para resultados
if not os.path.exists("resultados.txt"):
    resultados = open("resultados.txt", "w", encoding="utf-8")
else:
    resultados = open("resultados.txt", "w", encoding="utf-8")

# dataset processado - cada lista corresponde a uma linha
data = []

# ler dataset
for line in dataset.split("\n")[1:]:
    row = line.strip().split(",")
    data.append(row)

# lista de modalidades
modalidades = []
for line in data[1:]:
    if len(line) == 13:
        modalidade = line[8]
        if modalidade not in modalidades:
            modalidades.append(modalidade)
modalidades.sort()
resultados.write("Modalidades por orndem alfabetica: " + str(modalidades) + "\n\n")

# Percentagens de atletas aptos e inaptos para a prática desportiva
n_atletas = len(data) - 1
aptos = 0
inaptos = 0
for line in data[1:]:
    if len(line) == 13:
        if line[12] == "true":
            aptos += 1
        else:
            inaptos += 1
percentagem_aptos = (aptos / n_atletas) * 100
percentagem_inaptos = (inaptos / n_atletas) * 100
resultados.write("Percentagem de atletas aptos: " + str(percentagem_aptos) + "%\n")
resultados.write("Percentagem de atletas inaptos: " + str(percentagem_inaptos) + "%\n\n")

# Distribuição de atletas por escalão etário
resultados.write("Distribuição de atletas por escalão etário:\n")
escaloes = {}
max_idade = 0

for line in data[1:]:
    if len(line) == 13:
        idade = int(line[5])
        if idade > max_idade:
            max_idade = idade

# criar escaloes           
i = 1
while i <= max_idade:
    escalao = str(i) + "-" + str(i + 3)
    escaloes[escalao] = None
    i = i + 4

# distribuir atletas pelos escaloes
for line in data[1:]:
    if len(line) == 13:
        idade = int(line[5])
        nome = line[3] + " " + line[4]       
        for escalao, _ in escaloes.items():
            min_idade, max_idade = map(int, escalao.split("-"))
            if min_idade <= idade <= max_idade:
                if escaloes[escalao] is None:
                    escaloes[escalao] = [nome]
                else:
                    escaloes[escalao].append(nome)
                
for escalao, atletas in escaloes.items():
    resultados.write("Escalão " + escalao + ": " + str(atletas) + "\n")

resultados.close()
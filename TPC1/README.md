# TPC1: Análise de um dataset

## Autor
- Duarte Machado Leitão
- A100550

## Resumo

Sem recorrer à biblioteca csv, é necessário fazer a leitura e parsing do dataset. Com os dados recolhidos, deverão ser realizadas as seguintes tarefas:

- **Tarefa 1:** criar uma lista ordenada alfabeticamente das modalidades desportivas

- **Tarefa 2:** determinar as percentagens de atletas aptos e inaptos para a prática desportiva

- **Tarefa 3:** determinar a distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

## Resolução

Este TPC é resolvido com recurso a um script python. Os resultados de cada tarefa são guardados no ficheiro "resultados.txt", que é criado no inicio do script (caso este não exista). De seguida, passa-se à leitura e parsing do csv. Cada linha corresponde a uma lista de strings. Esta lista será posteriormente adicionada a outra lista que guarda todas as linhas. 

- **Tarefa 1:** em primeiro lugar é criada uma lista para guardar as modalidades. Depois é usado um ciclo para percorrer a lista de linhas. Se a modalidade encontrada em cada linha não se encontrar na lista de modalidades, será adicionada. Por fim a lista de modalidades é ordenada alfabeticamente com o método sort.

- **Tarefa 2:** em primeiro lugar é calculado o numero de atletas no dataset, juntamente com duas variáveis - uma para contar atletas aptos e ou para não aptos. Recorre-se a um ciclo para percorrer a lista de linhas e atualizar o valor das variáveis. No fim são calculadas as percentagens.

- **Tarefa 3:** em primeiro lugar é criado um dicionário para associar um escalão a uma lista de atletas. De seguida é calculada a idade máxima do dataset para criar um número adequado de escalões. Com recuroso a um ciclo, são criados os ciclos que irão servir de chaves para o dicionário. É usado outro ciclo para inserir cada atleta no respetivo escalão. Se o escalão ainda não tiver atletas, o valor inserido é uma lista com o primeiro e último nome do atleta em questão. Caso contrário, estes são adicionados à lista existente.
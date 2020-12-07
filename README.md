# Boas vindas ao repositório do projeto de Relatório de Estoque!

Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo e, se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

---

## Instruções para entregar seu projeto:

### ANTES DE COMEÇAR A DESENVOLVER:

1. Clone o repositório

- `git clone git@github.com:tryber/sd-0x-inventory-report.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-0x-inventory-report`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

Nota: após terminar o trabalho, para desativar o ambiente virtual digite `deactivate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

4. Crie uma branch a partir da branch `master`

- Verifique que você está na branch `master`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `master`
  - Exemplo: `git checkout master`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-inventory-report`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto inventory-report'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-inventory-report/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-inventory-report/pulls) e confira que o seu _Pull Request_ está criado

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter, para aprovação em todos os requisitos, os arquivos `main.py`, `inventory.py`, `inventory_iterator.py`, `importer.py`, `csv_importer.py`, `json_importer.py`, `xml_importer.py`, `simple_report.py`, `complete_report.py`, que conterão seu código `Python` e testes. Atente que os requisitos te orientarão a povoar estes arquivos aos poucos.

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a gente no Slack!.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

No projeto passado você implementou algumas funções que faziam leitura e escrita de arquivos JSON e CSV, correto? Neste projeto nós vamos fazer algo parecido, mas orientados pela Programação Orientada a Objeto! Você implementará um gerador de relatórios que recebe arquivos com dados de um estoque e gera, de saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas formas, sendo elas:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- Através da importação de um arquivo `XML`;

Além disso, o relatório final deverá poder ser gerado em duas versões: simples e completa.

### Como o projeto deve ser executável

Seu programa deverá ser executável **via linha de comando** com o comando `inventory_report argumento1 argumento2`:

- O **argumento 1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

- O **argumento 2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.

---

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
.
├── dev-requirements.txt
├── inventory_report
│   ├── data
│   │   ├── inventory.csv
│   │   ├── inventory.json
│   │   └── inventory.xml
│   ├── importer
│   │   ├── csv_importer.py
│   │   ├── importer.py
│   │   ├── json_importer.py
│   │   └── xml_importer.py
│   ├── inventory
│   │   ├── inventory_iterator.py
│   │   └── inventory.py
│   ├── main.py
│   └── reports
│       ├── complete_report.py
│       └── simple_report.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    ├── test_complete_report.py
    ├── test_csv_importer.py
    ├── test_importer.py
    ├── test_inventory.py
    ├── test_json_importer.py
    ├── test_main.py
    ├── test_simple_report.py
    └── test_xml_importer.py
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar tanto as classes quanto os testes. Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r dev-requirements.txt
```

O arquivo `dev-requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, você pode executá-lo com o seguinte comando:

```bash
$ python3 -m flake8
```

---

## Dados

Arquivos de exemplo nos três formatos de importação estão disponíveis no diretório `data` deste repositório.

### Importação de arquivos CSV

Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```csv
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,Nicotine Polacrilex,Target Corporation,2020-02-18,2022-09-17,CR25 1551 4467 2549 4402 1,morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit
2,fentanyl citrate,"Galena Biopharma, Inc.",2019-12-06,2022-12-25,FR29 5951 7573 74OY XKGX 6CSG D20,bibendum morbi non quam nec dui luctus rutrum nulla tellus in
3,NITROUS OXIDE,Keen Compressed Gas Co. Inc.,2019-12-22,2023-11-07,CZ09 8588 0858 8435 9140 2695,ipsum dolor sit amet consectetuer adipiscing elit proin risus praesent
```

### Importação de arquivos JSON

Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa":"Forces of Nature",
    "data_de_fabricacao":"2020-07-04",
    "data_de_validade":"2023-02-09",
    "numero_de_serie":"FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento":"in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus"
  }
]
```

### Importação de arquivos XML

Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>valsartan and hydrochlorothiazide</nome_do_produto>
    <nome_da_empresa>Lake Erie Medical &amp; Surgical Supply DBA Quality Care Products LLC</nome_da_empresa>
    <data_de_fabricacao>2019-10-27</data_de_fabricacao>
    <data_de_validade>2022-08-31</data_de_validade>
    <numero_de_serie>MT08 VVDN 2131 9NFL C1JG KTDV RS1L LOZ</numero_de_serie>
    <instrucoes_de_armazenamento>at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat</instrucoes_de_armazenamento>
  </record>
</dataset>
```

---

## Requisitos obrigatórios:

#### 1 -Criar um método `generate` numa classe `SimpleReport` do módulo `simple-report`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá gerar uma saída para a linha de comando.

- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

- O método deverá gerar, na linha de comando, uma saída com o seguinte formato:

   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
   ```

**Dica**: O módulo [datetime](https://docs.python.org/3/library/datetime.html) vai te ajudar.

##### As seguintes verificações serão feitas:

**[Será validado que é possível que a classe `SimpleReport` liste a data de fabricação mais antiga]**

**[Será validado que é possível que a classe `SimpleReport` liste a validade de fabricação mais próxima]**

**[Será validado que é possível que a classe `SimpleReport` liste a empresa com maior estoque]**

**[Será validado que é possível que a classe `SimpleReport` liste o formato correto]**

#### 2 - Criar um método `generate` numa classe `CompleteReport` do módulo `complete-report`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá gerar uma saída para a linha de comando.

- A classe `CompleteReport` deve herdar o método (`generate`) da classe `SimpleReport`, de modo a especializar seu comportamento.

- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

- O método deverá gerar, na linha de comando, uma saída com o seguinte formato:

   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
   Produtos estocados por empresa:
   - Physicians Total Care, Inc.: QUANTIDADE
   - Newton Laboratories, Inc.: QUANTIDADE
   - Forces of Nature: QUANTIDADE
   ```

##### As seguintes verificações serão feitas:

**[Será validado que é possível que a classe `CompleteReport` liste a data de fabricação mais antiga]**

**[Será validado que é possível que a classe `CompleteReport` liste a validade de fabricação mais próxima]**

**[Será validado que é possível que a classe `CompleteReport` liste a empresa com maior estoque]**

**[Será validado que é possível que a classe `CompleteReport` liste a quantidade de estoque correto]**

**[Será validado que é possível que a classe `CompleteReport` liste o formato correto]**

#### 3 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory`, capaz de ler um arquivo CSV passado como parâmetro de linha de comando

- O método, quando receber um arquivo CSV, deve chamar o método de gerar relatório correspondente à entrada passada, `simples` ou `completo`. Ou seja, o método da classe `Inventory` deve chamar o método da classe que vai gerar o relatório.

##### As seguintes verificações serão feitas:

**[Será validado que ao importar um arquivo csv simples será retornado com sucesso]**

**[Será validado que ao importar um arquivo csv completo será retornado com sucesso]**

#### 4 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory`, capaz de ler um arquivo JSON passado como parâmetro de linha de comando

- O método, quando receber um arquivo JSON, deve chamar o método de gerar relatório correspondente à entrada passada, `simples` ou `completo`. Ou seja, o método da classe `Inventory` deve chamar o método da classe que vai gerar o relatório.

##### As seguintes verificações serão feitas:

**[Será validado que ao importar um arquivo json simples será retornado com sucesso]**

**[Será validado que ao importar um arquivo json completo será retornado com sucesso]**

#### 5 - Deve haver um método `import_data` dentro de uma classe `Inventory` do módulo `inventory`, capaz de ler um arquivo XML passado como parâmetro  de linha de comando

- O método, quando receber um arquivo XML, deve chamar o método de gerar relatório correspondente à entrada passada, `simples` ou `completo`. Ou seja, o método da classe `Inventory` deve chamar o método da classe que vai gerar o relatório.

##### As seguintes verificações serão feitas:

**[Será validado que ao importar um arquivo xml simples será retornado com sucesso]**

**[Será validado que ao importar um arquivo xml completo será retornado com sucesso]**

#### 6 - Criar uma classe abstrata `Importer` no módulo import. Deve haver três classes herdeiras desta: `CsvImporter`, `JsonImporter` e `XmlImporter`, cada uma definida em seu respectivo módulo.

- A classe abstrata deve definir a assinatura do método `import_data` a ser implementado por cada classe herdeira. Ela deve receber como parâmetro o nome do arquivo a ser importado.

- O método `import_data` definida por cada classe herdeira deve lançar uma exceção caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um CSV para o `JsonImporter`.

- O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

##### As seguintes verificações serão feitas:

**[Será validado que a casse CsvImporter está herdando a classe Importer]**

**[Será validado que a casse JsonImporter está herdando a classe Importer]**

**[Será validado que a casse XmlImporter está herdando a classe Importer]**

**[Será validado que a classe CsvImporter esta importando os dados para uma lista]**

**[Será validado que a classe JsonImporter esta importando os dados para uma lista]**

**[Será validado que a classe XmlImporter esta importando os dados para uma lista]**

**[Será validado que ao enviar um arquivo com extensão incorreta para o CsvImporter irá gerar um erro]**

**[Será validado que ao enviar um arquivo com extensão incorreta para o JsonImporter irá gerar um erro]**

**[Será validado que ao enviar um arquivo com extensão incorreta para o XmlImporter irá gerar um erro]**

#### 7 - Criar uma classe `InventoryIterator` no módulo `inventory-iterator`, que implementa a interface de um iterator. A classe `Inventory` deve implementar o método `__iter__` associado a essa classe.

- A classe `Inventory` deverá ser refatorada em outro arquivo chamado `inventory_report/inventory/inventory_refactor.py`. Nesse arquivo você irá refatorar a classe Inventory e passar chamar essa classe de `InventoryRefactor`

- A classe `InventoryRefactor` deve utilizar as classes definidas no requisito 6 para lidar com a lógica de importação, via **composição**.

- As classes `InventoryIterator` e `InventoryRefactor` devem implementar corretamente a interface de um iterator, de modo que o código abaixo nos dê o primeiro item da lista de dicionários com os dados importados:

- É necessário gravar na instância quando importar os dados e tambem ao gravar novos dados expandir esses mesmos dados.

- As variáveis e os método devem ser públicos.

   ```python
   # ... Acima, um código que instância e importa um arquivo para a variável `inventory` e importações do módulo Iterator e Iterable

   iterator = iter(inventory)
   first_item = next(iterator)
   ```

##### As seguintes verificações serão feitas:

**[Será validado que inter é instanciado por iterator]**

**[Será validado que é possivel interar o primeiro item da lista usando csv]**

**[Será validado que é possivel interar o primeiro item da lista usando json]**

**[Será validado que é possivel interar o primeiro item da lista usando xml]**

**[Será validado que é possivel expandir duas listas de dados]**

**[Será validado que não é possivel enviar arquivo inválido]**


## Requisitos bônus:

#### 8 - Criar um menu no arquivo `inventory_report/main.py` que ao inserir as informações necessárias, as ações adequadas devem ser disparadas.

- Onde o comando no menu executado será:

`inventory_report inventory_report/data/inventory.json simples`

- O menu terá duas entradas
  - O arquivo com sua extenção .csv, .json ou .xml.
  - Se o relatório e "simples" ou "completo"

- Deverá ser usado o metódo `import_data` do arquivo `inventory_report/inventory_refactor.py` para verificar o tipo de arquivo e o formato do relatório.

- Onde o resultado printado no console deverá ser esses:
  - Para o simples:

  ```json
  Data de fabricação mais antiga: 2019-09-06
  Data de validade mais próxima: 2022-09-17
  Empresa com maior quantidade de produtos estocados: Target Corporation
  ```
  
  - Para o completo:
  
  ```json
  Data de fabricação mais antiga: 2019-09-06
  Data de validade mais próxima: 2022-09-17
  Empresa com maior quantidade de produtos estocados: Target Corporation
  
  Produtos Estocados por empresa: 
  - Target Corporation: 2
  - Galena Biopharma: 3
  - Cantrell Drug Company: 3
  - Moore Medical LLC: 1
  - REMEDYREPACK: 1
  ```

- Caso a tenha menos de três argumentos, exiba a mensagem de erro "Verifique os argumentos" na `stderr`.

📌 A função `sys.argv` deve ser utilizada para receber a entrada de dados da pessoa usuária.

✍️  Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `inventory_report parametro_1 parametro_2`, assim você conseguirá interagir com o menu.

##### As seguintes verificações serão feitas:

**[Será validado se o menu importa um arquivo csv simples]**

**[Será validado se o menu importa um arquivo csv completo]**

**[Será validado se o menu importa um arquivo json simples]**

**[Será validado se o menu importa um arquivo json completo]**

**[Será validado se o menu importa um arquivo xml simples]**

**[Será validado se o menu importa um arquivo xml completo]**

**[Será validado se passar opcões a menos no menu irá retornar um erro]**

---

### DURANTE O DESENVOLVIMENTO

- Faça `commits` das alterações que você fizer no código regularmente

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

- Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
  5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

---

### DEPOIS DE TERMINAR O DESENVOLVIMENTO (OPCIONAL)

Para sinalizar que o seu projeto está pronto para o _"Code Review"_ dos seus colegas, faça o seguinte:

- Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

  - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

  - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

  - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-0x`.

Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

---

### REVISANDO UM PULL REQUEST

Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.

#VQV 🚀

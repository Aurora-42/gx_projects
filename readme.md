# Estudos Great Expectations
Este projeto utiliza a biblioteca `great_expectations` para validar dados de um DataFrame pandas. Abaixo estão os principais conceitos e passos utilizados no código.

## Conceitos 

### Contexto do Great Expectations
O contexto do Great Expectations é o ambiente principal onde todas as operações de validação de dados ocorrem. Ele gerencia as configurações, fontes de dados, expectativas e resultados de validação. Inicializar o contexto é o primeiro passo para começar a usar a biblioteca.

### Fonte de Dados
Uma fonte de dados no Great Expectations representa a origem dos dados que você deseja validar. Pode ser um banco de dados, um arquivo CSV, um DataFrame pandas, entre outros. Adicionar uma fonte de dados ao contexto permite que o Great Expectations saiba de onde os dados estão vindo.

### Asset de DataFrame
Um asset de DataFrame é uma representação específica de um conjunto de dados dentro de uma fonte de dados. No caso de um DataFrame pandas, o asset representa o DataFrame que você deseja validar. Ele é adicionado à fonte de dados para que o Great Expectations possa trabalhar com ele.

### Definição de Batch
Um batch é uma porção específica de dados que você deseja validar. No contexto de um DataFrame, um batch pode ser o DataFrame inteiro ou uma parte dele. A definição de batch especifica como os dados são agrupados para validação.

### Expectativa
Uma expectativa é uma regra ou condição que você define para os dados. Por exemplo, você pode definir uma expectativa de que os valores de uma coluna estejam dentro de um certo intervalo. As expectativas são usadas para validar se os dados atendem aos critérios definidos.

### Validação
A validação é o processo de verificar se os dados atendem às expectativas definidas. O resultado da validação indica se os dados passaram ou falharam nas expectativas, ajudando a garantir a qualidade e a confiabilidade dos dados.
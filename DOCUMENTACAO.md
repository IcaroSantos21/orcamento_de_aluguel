# Documentação Técnica - Sistema de Orçamento de Imóveis

## 📖 Visão Geral

Este documento fornece informações técnicas detalhadas sobre o Sistema de Orçamento de Imóveis, incluindo arquitetura, classes, métodos e fluxos de funcionamento.

## 🏗️ Arquitetura do Sistema

O sistema segue o paradigma de Programação Orientada a Objetos (POO) com separação clara de responsabilidades:

- **main.py**: Interface do usuário e controle de fluxo
- **classe_orcamentos.py**: Lógica de negócio e cálculos

## 📋 Classe Orcamento

### Constantes da Classe

```python
VALOR_APARTAMENTO = 700.00          # Valor base apartamento
VALOR_CASA = 900.00                 # Valor base casa  
VALOR_ESTUDIO = 1200.00             # Valor base estúdio
VALOR_CONTRATO = 2000.00            # Valor fixo do contrato
VALOR_QUARTO_CASA = 250.00          # Adicional por quarto (casa)
VALOR_QUARTO_APARTAMENTO = 200.00   # Adicional por quarto (apartamento)
VALOR_GARAGEM = 300.00              # Adicional garagem
VALOR_ESTACIONAMENTO = 250.00       # Adicional estacionamento (até 2 vagas)
```

### Construtor

```python
def __init__(self, tipo_imovel, numero_quartos=1, criancas=0, 
             garagem=0, vagas_estacionamento=0, numero_parcela=1)
```

**Parâmetros:**
- `tipo_imovel` (str): "casa", "apartamento" ou "estudio"
- `numero_quartos` (int): Quantidade de quartos (padrão: 1)
- `criancas` (int): Número de crianças (padrão: 0)
- `garagem` (int): Possui garagem (0=não, 1=sim)
- `vagas_estacionamento` (int): Vagas de estacionamento para estúdio
- `numero_parcela` (int): Parcelas do contrato (1-5)

### Métodos Principais

#### calcular_valor_aluguel()

Calcula o valor do aluguel baseado no tipo de imóvel e características.

**Lógica de Cálculo:**

**Apartamento:**
```python
valor_base = VALOR_APARTAMENTO
+ (quartos_extras * VALOR_QUARTO_APARTAMENTO)
+ (garagem * VALOR_GARAGEM)
* (0.95 se sem_criancas else 1.0)
```

**Casa:**
```python
valor_base = VALOR_CASA
+ (quartos_extras * VALOR_QUARTO_CASA)
+ (garagem * VALOR_GARAGEM)
```

**Estúdio:**
```python
valor_base = VALOR_ESTUDIO
+ VALOR_ESTACIONAMENTO (se vagas <= 2)
+ (60.00 * vagas_extras) (se vagas > 2)
```

#### calcular_parcelas()

Calcula o valor das parcelas do contrato.

```python
parcela = VALOR_CONTRATO / numero_parcelas
```

**Validações:**
- Número de parcelas entre 1 e 5
- Retorna ValueError se inválido

## 🔄 Fluxo do Sistema (main.py)

### Função main()

Loop principal do sistema que gerencia o menu e as operações.

```
┌─────────────────┐
│   Mostrar Menu  │
└─────────┬───────┘
          │
    ┌─────▼─────┐
    │ Opção = ? │
    └─────┬─────┘
          │
    ┌─────▼─────┐    ┌──────────────┐    ┌─────────────┐
    │     1     │───▶│ Criar        │───▶│ Salvar CSV  │
    │ Orçamento │    │ Orçamento    │    │             │
    └───────────┘    └──────────────┘    └─────────────┘
          │
    ┌─────▼─────┐    ┌──────────────┐
    │     2     │───▶│ Mostrar      │
    │ Listar    │    │ Orçamentos   │
    └───────────┘    └──────────────┘
          │
    ┌─────▼─────┐
    │     3     │
    │   Sair    │
    └───────────┘
```

### Função criar_orçamento()

Coleta dados do usuário e cria um novo orçamento.

**Fluxo de Entrada:**
1. Solicita tipo de imóvel
2. **Se estúdio**: pergunta sobre estacionamento
3. **Se casa/apartamento**: 
   - Quantidade de quartos
   - Presença de crianças
   - Garagem
4. Número de parcelas do contrato
5. Cria objeto Orcamento
6. Adiciona à lista global

### Função mostrar_orcamento()

Exibe lista de orçamentos e permite visualizar detalhes.

**Validações:**
- Verifica se lista não está vazia
- Valida índice selecionado pelo usuário

### Exportação CSV

Gera arquivo `orcamento.csv` com:
- Cabeçalho do orçamento
- Projeção mensal (12 meses)
- Valor fixo do aluguel por mês

**Formato do CSV:**
```
Orcamento
Mês;Aluguel
1;1700.0
2;1700.0
...
12;1700.0
```

## 🔍 Validações e Tratamento de Erros

### Validações Implementadas

1. **Tipo de Imóvel**: Aceita apenas "casa", "apartamento", "estudio"
2. **Parcelas**: Entre 1 e 5 parcelas
3. **Índice de Orçamento**: Valida seleção na lista
4. **Entrada Numérica**: Conversão de strings para int

### Tratamento de Erros

- **ValueError**: Para tipos de imóvel inválidos
- **ValueError**: Para número de parcelas inválido
- **Validação de Lista**: Verifica se há orçamentos antes de listar

## 📊 Estrutura de Dados

### Lista Global
```python
lista_orcamentos = []  # Armazena objetos Orcamento
```

### Objeto Orcamento
```python
{
    'tipo_imovel': str,
    'quantidade_quartos': int,
    'quantidade_criancas': int,
    'garagem': int,
    'vagas_estacionamento': int,
    'numero_parcelas': int
}
```

## 🚀 Possíveis Melhorias

### Funcionalidades
- [ ] Persistência em banco de dados
- [ ] Interface gráfica (GUI)
- [ ] Relatórios em PDF
- [ ] Histórico de alterações de preços
- [ ] Cálculo de reajustes anuais

### Técnicas
- [ ] Testes unitários
- [ ] Logging de operações
- [ ] Configuração externa de preços
- [ ] Validação de entrada mais robusta
- [ ] Padrão MVC completo

### Performance
- [ ] Cache de cálculos
- [ ] Otimização de I/O
- [ ] Processamento assíncrono

## 🔧 Dependências

### Bibliotecas Padrão
- `csv`: Manipulação de arquivos CSV
- `os`: Operações do sistema (implícito)

### Requisitos de Sistema
- Python 3.6+
- Sistema operacional: Windows/Linux/macOS
- Memória: Mínimo 64MB RAM
- Espaço em disco: 10MB

## 📝 Convenções de Código

### Nomenclatura
- **Classes**: PascalCase (`Orcamento`)
- **Funções**: snake_case (`criar_orçamento`)
- **Constantes**: UPPER_CASE (`VALOR_APARTAMENTO`)
- **Variáveis**: snake_case (`lista_orcamentos`)

### Estrutura
- Imports no topo do arquivo
- Constantes após imports
- Funções em ordem lógica de uso
- Função main() no final

## 🧪 Casos de Teste

### Cenários de Teste Sugeridos

1. **Apartamento Básico**: 1 quarto, sem garagem, sem crianças
2. **Casa Completa**: 3 quartos, com garagem, com crianças
3. **Estúdio Premium**: Com 3 vagas de estacionamento
4. **Parcelamento Máximo**: Contrato em 5 parcelas
5. **Validações**: Entradas inválidas e casos extremos
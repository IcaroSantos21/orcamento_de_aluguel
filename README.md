# Sistema de Orçamento de Imóveis

Sistema simples para calcular orçamentos de aluguel de imóveis (casas, apartamentos e estúdios) com diferentes configurações e opções de pagamento.

## 📋 Funcionalidades

- **Cálculo de Aluguel**: Calcula valores baseados no tipo de imóvel e características
- **Tipos de Imóvel**: Casa, Apartamento e Estúdio
- **Configurações Personalizáveis**:
  - Número de quartos (casa/apartamento)
  - Garagem (casa/apartamento)
  - Vagas de estacionamento (estúdio)
  - Desconto para imóveis sem crianças
- **Parcelamento**: Contrato divisível em até 5 parcelas
- **Exportação**: Gera arquivo CSV com detalhes do orçamento
- **Histórico**: Lista todos os orçamentos criados

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6 ou superior


### Menu Principal
1. **Fazer Orçamento**: Cria um novo orçamento
2. **Listar Orçamentos**: Visualiza orçamentos salvos
3. **Sair do Programa**: Encerra o sistema

## 💰 Tabela de Preços

| Tipo de Imóvel | Valor Base | Quarto Adicional | Observações |
|----------------|------------|------------------|-------------|
| Apartamento    | R$ 700,00  | R$ 200,00       | Desconto 5% sem crianças |
| Casa           | R$ 900,00  | R$ 250,00       | - |
| Estúdio        | R$ 1.200,00| -               | - |

### Adicionais
- **Garagem**: R$ 300,00
- **Estacionamento** (até 2 vagas): R$ 250,00
- **Vaga Extra** (acima de 2): R$ 60,00 por vaga
- **Contrato**: R$ 2.000,00 (parcelável em até 5x)

## 📁 Estrutura do Projeto

```
orcamento/
├── main.py                 # Arquivo principal com interface do usuário
├── classe_orcamentos.py    # Classe Orcamento com lógica de cálculo
├── README.md              # Este arquivo
├── DOCUMENTACAO.md        # Documentação técnica detalhada
└── orcamento.csv          # Arquivo gerado com orçamentos (criado automaticamente)
```

## 📊 Exemplo de Uso

```
Qual o imovel que você deseja alugar?
[Casa] | [Apartamento] | [Estudio]
Digite Aqui: casa

Digite a quantidade de quartos deseja: 3
Um dos moradores será uma criança? [S]Sim | [N]Não: N
Deseja uma casa com garagem? [S]Sim | [N]Não: S
Deseja pagar em quantas vezes? em até 5x: 2

Resultado:
- Tipo: Casa
- Quartos: 3
- Garagem: Sim
- Valor do Aluguel: R$ 1.700,00
- Contrato: R$ 1.000,00 (2x)
```

## 🔧 Tecnologias Utilizadas

- **Python 3**: Linguagem principal
- **CSV**: Para exportação de dados
- **POO**: Programação Orientada a Objetos

## 📝 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato através dos issues do projeto.
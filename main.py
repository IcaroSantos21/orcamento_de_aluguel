from classe_orcamentos import Orcamento
qtd_criancas = 0
qtd_quartos = 0
garagem = 0
qtd_vagas = 0
print('-------------------------------------------------------\n')
print('Olá vamos começar o Orçamento do seu mais novo IMÓVEL\n')
print('-------------------------------------------------------\n')

imovel = input('Qual o imovel que você deseja alugar?\n' \
                '[Casa] | [Apartamento] | [Estudio]\n' \
                'Digite Aqui: ').lower()

if imovel == 'estudio':
    estacionamento = input('Gostaria de ter vagas de estacionamento? [S]Sim | [N]Não:').upper()
    if estacionamento == 'S':
        qtd_vagas = int(input('Quantidade de Vagas: '))

else:
    qtd_quartos = int(input('Digite a quantidade de quartos deseja: '))
    possui_crianca = input('Um dos moradores será uma criança? [S]Sim | [N]Não: ').upper()
    if possui_crianca == 'S':
        qtd_criancas = int(input('Digite a quantidade de crianças: '))
        crianca = qtd_criancas
    possui_garagem = input('Deseja uma casa com garagem? [S]Sim | [N]Não:').upper()
    if possui_garagem == 'S':
        garagem = 1

print(Orcamento.VALOR_CONTRATO)
parcela_contrato = int(input('Deseja pagar em quantas vezes? em até 5x: '))

orcamento = Orcamento(
    tipo_imovel = imovel,
    numero_quartos = qtd_quartos,
    criancas = qtd_criancas,
    garagem = garagem,
    vagas_estacionamento = qtd_vagas,
    numero_parcela = parcela_contrato
)

lista_orcamentos = [orcamento]

for i, valor in enumerate(lista_orcamentos):
    print(valor)
from classe_orcamentos import Orcamento
import csv
lista_orcamentos = []
def criar_orçamento():  
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

    novo_orcamento = Orcamento(
        tipo_imovel = imovel,
        numero_quartos = qtd_quartos,
        criancas = qtd_criancas,
        garagem = garagem,
        vagas_estacionamento = qtd_vagas,
        numero_parcela = parcela_contrato
    )
    lista_orcamentos.append(novo_orcamento)
    return novo_orcamento
def mostrar_orçamento(lista):
    if not lista_orcamentos:
        return 'Não existe nenhum orçamento na lista ainda'
        
    print(f'Existem um total de {len(lista_orcamentos)} orçamentos criados')
    for i, o in enumerate(lista_orcamentos, start=1):
                print(f"{i} - {o.tipo_imovel.title()} ({o.quantidade_quartos} quartos)")
            
    escolha = int(input("Digite o número do orçamento que deseja ver: "))
    if 1 <= escolha <= len(lista_orcamentos):
        print(lista_orcamentos[escolha - 1])
    else:
        print("Número inválido!")
def criar_arquivo_csv():
     ...
# with open('orcamento.csv', 'w', newline='') as arquivo:
#     escritor = csv.writer(arquivo)
#     escritor.writerow(['MÊS ', ' VALOR'])
#     for mes in range(1, 13):
#         escritor.writerow([mes, orcamento.calcular_valor_aluguel()])


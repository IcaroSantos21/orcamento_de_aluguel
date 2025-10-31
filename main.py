from classe_orcamentos import Orcamento
import csv
lista_orcamentos = [] # Lista para armazenar os orçamentos

# Função para criar o orçamento
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

    # Solicita a quantidade de vagas do estacionamento somente para o estudio
    if imovel == 'estudio':
        estacionamento = input('Gostaria de ter vagas de estacionamento? [S]Sim | [N]Não:').upper()
        if estacionamento == 'S':
            qtd_vagas = int(input('Quantidade de Vagas: '))

    # Solicita dados para o orçamento de casa e/ou apartamento
    else:
        qtd_quartos = int(input('Digite a quantidade de quartos deseja: '))
        possui_crianca = input('Um dos moradores será uma criança? [S]Sim | [N]Não: ').upper()
        if possui_crianca == 'S':
            qtd_criancas = int(input('Digite a quantidade de crianças: '))
        possui_garagem = input('Deseja uma casa com garagem? [S]Sim | [N]Não:').upper()
        if possui_garagem == 'S':
            garagem = 1

    print(Orcamento.VALOR_CONTRATO)
    parcela_contrato = int(input('Deseja pagar em quantas vezes? em até 5x: '))

    # cria o orçamento
    novo_orcamento = Orcamento(
        tipo_imovel = imovel,
        numero_quartos = qtd_quartos,
        criancas = qtd_criancas,
        garagem = garagem,
        vagas_estacionamento = qtd_vagas,
        numero_parcela = parcela_contrato
    )
    lista_orcamentos.append(novo_orcamento) # adiciona o orçamento na lista
    print(novo_orcamento)
    return novo_orcamento # retorna o orçamento

# função para mostrar a lista de orçamentos criados
def mostrar_orcamento(lista):
    if not lista:
        print('Não existe nenhum orçamento na lista ainda')
        
    print(f'Existem um total de {len(lista_orcamentos)} orçamentos criados')
    for i, o in enumerate(lista_orcamentos, start=1):
                print(f"{i} - {o.tipo_imovel.title()} ({o.quantidade_quartos} quartos)")
            
    escolha = int(input("Digite o número do orçamento que deseja ver: "))
    if 1 <= escolha <= len(lista_orcamentos):
        print(lista_orcamentos[escolha - 1])
    else:
        print("Número inválido!")

# Função do menu de interação do usuário
def mostrar_menu():
    print('''
       -----------------------------   
        Selecione a Opção desejada:
        [1] Fazer Orçamento
        [2] Listar Orçamentos
        [3] Sair do Programa
       -----------------------------
    ''')
    return input('Digite o número aqui: ')

# Função principal do sistema
def main():
    while True:
        opcao = mostrar_menu()
        if opcao == '1':
            novo_orcamento = criar_orçamento()
            with open('orcamento.csv', mode='a', newline='\n', encoding='utf-8-sig') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                escritor.writerow(['Orcamento'])
                escritor.writerow([ 'Mês', 'Aluguel',])
                for mes in range(1, 13):
                    escritor.writerow([
                        mes,
                        novo_orcamento.calcular_valor_aluguel(),
                        ])

                        
            print('Orçamento Gerado com sucesso')
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '2':
            mostrar_orcamento(lista_orcamentos)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção Inválida, por valor selecione uma válida!')
            input("\nPressione ENTER para voltar ao menu...")

if __name__ == '__main__':
    main()
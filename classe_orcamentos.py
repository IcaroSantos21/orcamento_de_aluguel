# Criação da classe de orçamentos
class Orcamento():
    # Valor padrão por tipo de imóvel:
    VALOR_APARTAMENTO = 700.00 # Valor base para apartamentos
    VALOR_CASA = 900.00 # Valor base para casa
    VALOR_ESTUDIO = 1200.00 # Valor base para estudio
    # Valor padrão do contrato
    VALOR_CONTRATO = 2000.00 # Valor inteiro do contrato
    # Valor Padrão de adicionais
    VALOR_QUARTO_CASA = 250.00 # Valor caso adicione mais um quarto para casa
    VALOR_QUARTO_APARTAMENTO = 200.00 # Valor caso adicione mais um quarto para apartamento
    VALOR_GARAGEM = 300.00 # Valor padrão para adicionar garagem
    VALOR_ESTACIONAMENTO = 250.00 # Valor padrão para adicionar estacionamento de 2 vagas no estudio


    def __init__(self, tipo_imovel, numero_quartos=1, criancas=0, 
                 garagem=0, vagas_estacionamento=0, numero_parcela=1):
        # Atributos da classe  de orçamento
        self.tipo_imovel = tipo_imovel
        self.quantidade_quartos = numero_quartos
        self.quantidade_criancas = criancas
        self.garagem = garagem
        self.vagas_estacionamento = vagas_estacionamento
        self.numero_parcelas = numero_parcela

    def calcular_valor_aluguel(self):
        # Calcular o valor do imóvel com base no valor padrão e adicionais
        if self.tipo_imovel == 'apartamento':
            valor_base = self.VALOR_APARTAMENTO
            if self.quantidade_quartos > 1:
                # Acréscimo do quarto
                valor_base = self.VALOR_APARTAMENTO + (self.VALOR_QUARTO_APARTAMENTO * (self.quantidade_quartos - 1))
            if self.garagem >= 1:
                # Acréscimo da garagem
                valor_base += self.VALOR_GARAGEM
            if self.quantidade_criancas == 0:
                # Desconto caso não tenha criança
                valor_base *= 0.95
            return valor_base
        elif self.tipo_imovel == 'casa':
            valor_base = self.VALOR_CASA
            if self.quantidade_quartos > 1:
                # Acréscimo do quarto
                valor_base = self.VALOR_CASA + (self.VALOR_QUARTO_CASA * (self.quantidade_quartos - 1))
            if self.garagem >= 1:
                # Acréscimo da garagem
                valor_base += self.VALOR_GARAGEM
            return valor_base
        elif self.tipo_imovel == 'estudio':
            if self.vagas_estacionamento == 0:
                valor_base = self.VALOR_ESTUDIO 
            elif self.vagas_estacionamento <= 2:
                # Acréscimo do estacionamento até 2 vagas
                valor_base = self.VALOR_ESTUDIO + self.VALOR_ESTACIONAMENTO
            else:
                # Acréscimo do estacionamento acima de 2 vagas
                valor_base = self.VALOR_ESTUDIO + self.VALOR_ESTACIONAMENTO + (60.00 * (self.vagas_estacionamento - 2))
            return round(valor_base, 2)
        else:
            raise ValueError('Tipo de Imóvel inválido')
        
    def calcular_parcelas(self):
        # Calculando as parcelas do contrato
        if self.numero_parcelas <= 0 or self.numero_parcelas > 5:
            raise ValueError('O número de parcelas deve ser entre 1 e 5 vezes ')
        parcela = round(self.VALOR_CONTRATO / self.numero_parcelas, 2)
        return parcela 

    
    def __str__(self):
        # Saída da classe orçamento
        if self.tipo_imovel == 'estudio':
            return f"""
            |-----------------------|
            | DETALHES DO CONTRATO: |
            |-----------------------|
            Tipo de Imóvel: {self.tipo_imovel}
            Número de Vagas: {self.vagas_estacionamento}
            Valor Total do Aluguel: {self.calcular_valor_aluguel()}
            Valor Total Contrato:{self.VALOR_CONTRATO}
            Valor Parcelas do Contrato: {self.calcular_parcelas()}
            

        """
        return f"""
        |-----------------------|
        | DETALHES DO CONTRATO: |
        |-----------------------|
        Tipo de Imovel: {self.tipo_imovel}
        Numero de Quartos: {self.quantidade_quartos}
        Possui Garagem: {self.garagem}
        Valor Total do Aluguel: {self.calcular_valor_aluguel()}
        Valor Total Contrato:{self.VALOR_CONTRATO}
        Valor Parcelas Contrato: {self.calcular_parcelas()}
        """
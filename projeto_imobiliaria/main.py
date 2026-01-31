import csv

class imovel:
    def __init__(self, tipo, quartos=1, garagem=0, criancas=False):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.garagem = garagem
        self.criancas = criancas

    def calcular_aluguel(self):
        valor = 0

        # Valores base
        if self.tipo == "apartamento":
            valor = 700
            if self.quartos == 2:
                valor += 200
            if self.garagem > 0:
                valor += 300
            if not self.criancas:
                valor *= 0.95  # desconto de 5%

        elif self.tipo == "casa":
            valor = 900
            if self.quartos == 2:
                valor += 250
            if self.garagem > 0 :
                valor += 300

        elif self.tipo == "estudio":
            valor = 1200
            if self.garagem >= 2:
                valor += 250
                vagas_extras = self.garagem - 2
                if vagas_extras > 0:
                    valor += vagas_extras * 60

        return round(valor, 2)

class contrato:
    def __init__(self, valor_contrato=2000, parcelas=5):
        self.valor_contrato = valor_contrato
        self.parcelas = parcelas

    def valor_parcela(self):
        return round(self.valor_contrato / self.parcelas, 2)
    
class orcamento:
    def __init__(self, imovel, contrato):
        self.imovel = imovel
        self. contrato = contrato

    def gerar_resumo(self):
        aluguel = self.imovel.calcular_aluguel()
        return{
            "aluguel_mensal": aluguel,
            "valor_contrato": self.contrato.valor_contrato,
            "parcelas": self.contrato.parcelas,
            "valor_parcela": self.contrato.valor_parcela()
        }
    
    def gerar_csv(self, nome_arquivo="parcelas.csv"):
        aluguel = self.imovel.calcular_aluguel()
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Mês", "Valor do Aluguel"])
            for mes in range(1, 13):
                writer.writerow([mes, aluguel])


if __name__ == "__main__":
    print("=== GERADOR DE ORÇAMENTO - IMOBILIÁRIA R.M ===")

    tipo = input("Tipo do imovel (apartamento/casa/estudio): ")
    quartos = int(input("Quantidade de quartos (1 ou 2): "))
    garagem = int(input("Quantidade de vagas de garagem: "))

    criancas = False
    if tipo.lower()== "apartamento":
        resp = input("Possui crianças? (s/n): ")
        criancas = resp.lower() == 's'

    imovel = imovel(tipo, quartos, garagem, criancas)
    contrato = contrato()
    orcamento = orcamento(imovel, contrato)

    resumo = orcamento.gerar_resumo()

    print("\n--- RESUMO DO ORÇAMANTO ---")
    print(f"Aluguel mensal: R$ {resumo['aluguel_mensal']}")
    print(f"Contrato: R$ {resumo['valor_contrato']} em {resumo['parcelas']}x de R$ {resumo['valor_parcela']} ")

    gerar = input("deseja gerar arquivo CSV com 12 meses? (s/n): ")
    if gerar.lower() == 's':
        orcamento.gerar_csv()
        print("Arquivo parcelas.csv gerado com sucesso!")

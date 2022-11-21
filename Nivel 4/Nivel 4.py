import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


class Grafico:
    def __init__(self, data, item, cor, label):
        self.data = data
        self.item = item
        self.cor = str(cor)
        self.label = str(label)

    def gerarelementos(self):
        plt.plot(self.data, self.item, str(self.cor), marker='o', label=str(self.label))

    def geraregrecao(self):
        plt.plot(self.data, self.item, str(self.cor), label=str(self.label))

    @staticmethod
    def gerargrafico():
        plt.title('Gráfico de Despesas')
        plt.ylabel('Despesa em R$')
        plt.xlabel('Dia')
        plt.legend()
        plt.show()


dia = []
alimentacao = []
vestuario = []
transporte = []

while True:
    dia.append(int(input('Qual o dia? ')))
    alimentacao.append(float(input('Valor Gasto com Alimentação: R$')))
    vestuario.append(float(input('Valor Gasto com Vestuário: R$')))
    transporte.append(float(input('Valor Gasto com Transporte: R$')))
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break

sorted(dia)

x = np.array(dia).reshape((-1, 1))
model = LinearRegression()
model.fit(x, alimentacao)
alimentacao_pred = model.predict(x)


a = Grafico(dia, alimentacao, 'b', 'Alimentação')
v = Grafico(dia, vestuario, 'r', 'Vestuário')
t = Grafico(dia, transporte, 'g', 'Transporte')
ap = Grafico(dia, alimentacao_pred, 'k', 'Regr. Linear Alimentação')
a.gerarelementos()
v.gerarelementos()
t.gerarelementos()
ap.geraregrecao()
Grafico.gerargrafico()
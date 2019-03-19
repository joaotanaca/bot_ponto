# encoding: utf-8

from openpyxl import Workbook
from datetime import datetime
from datetime import date

book=Workbook()
sheet=book.active

lista_colunas=['A', 'B']
entrada_saida=['Entrada', 'Saida']
for i in range(18,40):
    for f in range(0, 2):
        coluna=lista_colunas[f]
        ponto=raw_input("""Aperte enter para bater o ponto;
wknd para fim de semana;
f para feriado.Observações(dia {}/ mês {}, {})""".format(date.today().day, date.today().month, entrada_saida[f]))
        colinha='{}{}'.format(coluna, i)
        if ponto=='wknd':
            dias_wknd=float(input('Quantos dias de feriado?'))
            sheet[colinha]='//////'
            continue
        sheet[colinha]=datetime.now().time()
book.save('folha_ponto_mes_{}.xls'.format(date.today().month))

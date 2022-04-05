import xlsxwriter
import config

def import_excel(monitoramento_item):

    workbook = xlsxwriter.Workbook(config.PATH_EXCEL+'excelExample3.xlsx')

    worksheet = workbook.add_worksheet("Notas Requisição")

    worksheet.write('A1', 'CNPJ Tomador')
    worksheet.write('B1', 'CNPJ Prestador')
    worksheet.write('C1', 'Número Nota')
    worksheet.write('D1', 'Data Emissão')
    worksheet.write('E1', 'Chave Nota')
    worksheet.write('F1', 'Codigo de serviço')
    worksheet.write('G1', 'Valor Nota')

    scores = (
        ['ankit', 1000],
        ['rahul', 100],
        ['priya', 300],
        ['harshita', 50],
    )

    row = 1
    col = 0

    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1

    workbook.close()
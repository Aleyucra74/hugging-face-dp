import xlsxwriter
import config
import os
import pandas as pd

def import_excel(requisicao_excel):

    workbook = xlsxwriter.Workbook('\\\\Brdcvmtaxanapd\\innovation\\operacao\\excel\\requisicaoRelatorio.xlsx')

    worksheet = workbook.add_worksheet("Notas Requisição")

    worksheet.write('A1', 'Numero Lote')
    worksheet.write('B1', 'Nome Arquivo')
    worksheet.write('C1', 'CNPJ Tomador')
    worksheet.write('D1', 'CNPJ Prestador')
    worksheet.write('E1', 'Número Nota')
    worksheet.write('F1', 'Data Emissão')
    worksheet.write('G1', 'Código de Verificação')
    worksheet.write('H1', 'Codigo de serviço')
    worksheet.write('I1', 'Valor Nota')
    worksheet.write('J1', 'Valor PIS')
    worksheet.write('K1', 'Endereço Tomador')
    worksheet.write('L1', 'Endereço Prestador')
    worksheet.write('M1', 'Score CNPJ Tomador')
    worksheet.write('N1', 'Score CNPJ Prestador')
    worksheet.write('O1', 'Score Número Nota')
    worksheet.write('P1', 'Score Data Emissão')
    worksheet.write('Q1', 'Score Chave Nota')
    worksheet.write('R1', 'Score Codigo de serviço')
    worksheet.write('S1', 'Score Valor Nota')
    worksheet.write('T1', 'Score Valor PIS')
    worksheet.write('U1', 'Score Endereço Tomador')
    worksheet.write('V1', 'Score Endereço Prestador')
    worksheet.write('V1', 'Municipio')

    row = 1
    col = 0

    for data in requisicao_excel:
        worksheet.write(row, col ,data['mliCodigo'])
        worksheet.write(row, col+1,data['mliNome'])
        worksheet.write(row, col+2 ,data['cnpjTomador'])
        worksheet.write(row, col+3 ,data['cnpjPrestador'])
        worksheet.write(row, col+4 ,data['numeroNota'])
        worksheet.write(row, col+5 ,data['dataEmissao'])
        worksheet.write(row, col+6 ,data['codigoVerificacao'])
        worksheet.write(row, col+7 ,data['codigoServico'])
        worksheet.write(row, col+8 ,data['valorTotal'])
        worksheet.write(row, col+9 ,data['pis'])
        worksheet.write(row, col+10 ,data['enderecoTomador'])
        worksheet.write(row, col+11 ,data['enderecoPrestador'])
        worksheet.write(row, col+12 ,data['scoreCnpjTomador'])
        worksheet.write(row, col+13 ,data['scoreCnpjPrestador'])
        worksheet.write(row, col+14 ,data['scoreNumeroNota'])
        worksheet.write(row, col+15 ,data['scoreDataEmissao'])
        worksheet.write(row, col+16 ,data['scoreCodigoVerificacao'])
        worksheet.write(row, col+17 ,data['scoreCodigoServico'])
        worksheet.write(row, col+18 ,data['scoreValorTotal'])
        worksheet.write(row, col+19 ,data['scorePis'])
        worksheet.write(row, col+20 ,data['scoreEnderecoTomador'])
        worksheet.write(row, col+21 ,data['scoreEnderecoPrestador'])
        row += 1

    workbook.close()

    return '\\\\Brdcvmtaxanapd\\innovation\\operacao\\excel\\requisicaoRelatorio.xlsx'


def import_excel_array(lista):
    df = pd.DataFrame(lista).T

    df.to_excel(excel_writer='\\\\Brdcvmtaxanapd\\innovation\\operacao\\excel\\test.xlsx')
    return '\\\\Brdcvmtaxanapd\\innovation\\operacao\\excel\\test.xlsx'
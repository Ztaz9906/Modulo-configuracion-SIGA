from io import BytesIO

from rest_framework.parsers import BaseParser
import openpyxl

class ExcelParser(BaseParser):
    media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    def parse(self, stream, media_type=None, parser_context=None):

        workbook = openpyxl.load_workbook(filename=BytesIO(stream.read()))
        sheet = workbook.active
        data_list = []
        for row in sheet.values:
            print(row)
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data = {
                'nombre_completo': row[0],
                'ci': row[1],
                'solapin': row[2],
                'codigo_solapin': row[3],
                'nombre_responsabilidad': row[4],
                'id_expediente': row[5],
            }
            data_list.append(data)
        return data_list

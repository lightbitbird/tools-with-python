import openpyxl
from datetime import date, datetime


class ExcelAccessor:
    xlsl_file = ''
    sheet = ''
    datetime_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self, xlsl_file='', sheet=''):
        self.xlsl_file = xlsl_file
        self.sheet = sheet

    def read_cells(self, range):
        wb = openpyxl.load_workbook(self.xlsl_file, data_only=True)
        ws = wb[self.sheet]
        cells = ws[range]
        row_cnt = 0
        data = ''
        for row in cells:
            if (row_cnt > 0):
                data += '\n'
            cell_cnt = 0
            for cell in row:
                if (cell_cnt > 0):
                    data += ','
                data += self.str_format(cell.value)
                # data += column_index_from_string(cell.column).value
                cell_cnt += 1
            row_cnt += 1

        print(data)

        return data

    def str_format(self, value):
        if type(value) is int:
            rtn = str(value)
        elif type(value) is bool:
            rtn = str(bool)
        else:
            if isinstance(value, date):
                rtn = value.strftime(self.datetime_format)
            elif isinstance(value, datetime):
                rtn = value.strftime(self.datetime_format)
            else:
                rtn = value
        if rtn.find(',') >= 0 or rtn.find("\n") >= 0 or rtn.find("\r\n") >= 0:
            rtn = '"' + rtn + '"'

        return rtn

    def create_csv_file(self, csv_data, output_file):
        with open(output_file, mode='w', encoding='utf-8') as f:
            f.write(csv_data)

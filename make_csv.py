import sys

from excel_accessor import ExcelAccessor

xlsl_file = ''
sheet = ''
range = ''
csv_file = ''
datetime_format = '%Y-%m-%d %H:%M:%S'

if __name__ == '__main__':
    args = sys.argv
    if 5 <= len(args):
        xlsl_file = args[1]
        sheet = args[2]
        range = args[3]
        csv_file = args[4]
    else:
        print('Arguments ar too short')
        print('Command line must be `python make_csv.py {xlsl_file} {sheet} {sheet range} {csv_file}`')
        sys.exit()


accessor = ExcelAccessor(xlsl_file, sheet)
accessor.create_csv_file(accessor.read_cells(range), csv_file)


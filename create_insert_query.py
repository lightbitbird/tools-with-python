import sys

from query_from_csv import QueryMaker, create_query_file

csv_file = ''
export_file = ''
table_name = ''

if __name__ == '__main__':
    args = sys.argv
    if 4 <= len(args):
        csv_file = args[1]
        table_name = args[2]
        export_file = args[3]
    else:
        print('Arguments ar too short')
        print('Command line must be `python insert_from_csv.py {csv_file} {table_name} {export_file}`')
        sys.exit()


qm = QueryMaker(csv_file)
create_query_file(qm.insert_query(table_name), export_file)

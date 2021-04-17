import csv
import chardet

def create_query_file(query, export_file):
    with open(export_file, mode='w', encoding='utf-8') as wf:
        wf.write(query)

        print(query)


class QueryMaker:
    csv_file = ''
    export_file = ''
    table_name = ''
    delimiter = ','
    newline = '\n'
    newline_cr = '\r\n'
    escape_char = '\''
    pre_parenthensis = '('
    suf_parenthensis = ')'
    end_char = ';'

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def insert_query(self, table_name):
        with open(self.csv_file, 'rb') as f:
            encoding = chardet.detect(f.read()).get('encoding')
            print(encoding)


        # with open(self.csv_file, encoding='utf-8') as f:
        with open(self.csv_file, encoding=encoding) as f:
            reader = csv.reader(f)

            query_prefix = 'INSERT INTO %s (%s) '
            q_values = self.newline + 'VALUES'

            q_body = ''
            header = next(reader)
            q_columns = ''

            col_cnt = 0
            for col in header:
                if (col_cnt > 0):
                    q_columns += self.delimiter + ' '
                q_columns += '`' + col + '`'
                col_cnt += 1

            cnt = 0
            for row in reader:
                if (cnt > 0):
                    q_body += self.suf_parenthensis + self.delimiter
                q_body += self.newline + '  ' + self.pre_parenthensis

                col_cnt = 0
                for col in row:
                    if (col_cnt > 0):
                        q_body += self.delimiter + ' '
                    q_body += self.escape_char + self.lineChar(col) + self.escape_char
                    col_cnt += 1
                cnt += 1

            q_head = query_prefix % (table_name, q_columns) + q_values
            q_body += self.suf_parenthensis
            query = q_head + q_body + self.end_char

        return query

    def lineChar(self, col):
        col = col.replace(self.newline_cr, "\\r\\n")
        return col.replace(self.newline, "\\n")

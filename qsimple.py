from sqlalchemy import create_engine
from os import getenv
import pandas as pd


# db configuration and connection
user = getenv('DBUSER')
pswd = getenv('DBPSWD')
host = getenv('DBHOST')
db = getenv('DBDB')
connect_str = 'mysql+pymysql://' + user + ':' + pswd + '@' + host + '/' + db
con = create_engine(connect_str)

c = 'cfpf'
file = open(c + '.sql', mode='r')
qc = file.read()
file.close()
print('processsing {}'.format(c))
qc = qc.replace('%', '%%')
print(qc)
print('executing query')
df = pd.read_sql_query(qc, con)
print('saving to spreadsheet')
df.to_excel(c + ".xlsx", sheet_name=c, engine='xlsxwriter')

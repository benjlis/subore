from sqlalchemy import create_engine
from os import getenv
import pandas as pd

# read query file
# with open('twihl.sql', 'r') as f:
#    qry = f.read()
# qry = "select id, authored, title, document_uri from marc_records " + \
#        "where rtrim(title) = '' or authored is null;"

prere = '(^| )'
bodyre = '(influenza|flu|cholera|yellow fever|typhus|smallpox|measles|' +\
         'malaria|encephalitis|polio|poliomyelitis|meningitis|dengue fever|' +\
         'hepatitis|ebola|HIV|AIDS|SARS|MERS|H1N1|Zika|COVID|coronavirus|' +\
         'epidemic|pandemic|plague)'
postre = '($| |,|;|\\\.|\\\?|!)'
re = prere + bodyre + postre

qry = "select date, 'Clinton' collection," +\
         " convert(classification, CHAR) classification, " + \
         " convert(title, CHAR) subject, " +\
         " convert(concat('http://history-lab.org/documents/', id), CHAR) " +\
         " id from declassification_clinton.docs " +\
         "  where subject regexp '{0}' or body regexp '{0}'".format(re) +\
         "  order by date"
#        "  where subject regexp '{0}'".format(re)


print(qry)
# db configuration and connection
user = getenv('DBUSER')
pswd = getenv('DBPSWD')
host = getenv('DBHOST')
db = getenv('DBDB')
connect_str = 'mysql+pymysql://' + user + ':' + pswd + '@' + host + '/' + db
con = create_engine(connect_str)

df = pd.read_sql_query(qry, con)
df.to_excel("see.xlsx", engine='xlsxwriter')

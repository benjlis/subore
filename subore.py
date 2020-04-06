from sqlalchemy import create_engine
from os import getenv
import pandas as pd

prere = '(^| )'
bodyre = '(influenza|asian flu|hong kong flu|spanish flu|1918 flu|' +\
         'cholera|yellow fever|typhus|smallpox|measles|' +\
         'malaria|encephalitis|polio|poliomyelitis|meningitis|dengue fever|' +\
         'hepatitis|ebola|HIV|AIDS|SARS|MERS|H1N1|Zika|COVID|coronavirus|' +\
         'bubonic plague|epidemic|pandemic)'
postre = '($| |,|;|\\\.|\\\?|!)'
re = prere + bodyre + postre

qry = "select date, 'Clinton' collection," +\
         " convert(classification, CHAR) classification, " + \
         " convert(title, CHAR) subject, " +\
         " convert(concat('http://history-lab.org/documents/', id), CHAR) " +\
         " id from declassification_clinton.docs " +\
         "  where subject regexp '{0}' or body regexp '{0}'".format(re) +\
         "  order by date"


def qry(corpus):
    return """
select date, classification, title,
       convert(concat('http://history-lab.org/documents/', id), CHAR) id
   from declassification_{1}.docs
   where subject regexp '{0}' or body regexp '{0}'
   order by date
""".format(re, corpus)


# db configuration and connection
user = getenv('DBUSER')
pswd = getenv('DBPSWD')
host = getenv('DBHOST')
db = getenv('DBDB')
connect_str = 'mysql+pymysql://' + user + ':' + pswd + '@' + host + '/' + db
con = create_engine(connect_str)

collections = ['frus', 'clinton', 'cables']
for c in collections:
    print('processsing {}'.format(c))
    print(qry(c))
#    df = pd.read_sql_query(qry(c), con)
#    df.to_excel("see.xlsx", sheet_name=c, engine='xlsxwriter')

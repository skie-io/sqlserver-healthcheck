import pandas as pd
from docxtpl import DocxTemplate
from rules.database_version import DatabaseVersionRule
from rules.instant_file import InstantFileRule
from server_name import ServerName
import rules
import datetime

xl = pd.ExcelFile('test_files/Navisite_SQL_Assesment__FULL_AGDATA-SQL_09_12_2021.xlsx')

db_version = DatabaseVersionRule(xl)
db_version.run()

rule2 = InstantFileRule(xl)
rule2.run()

topics = []
topics.append(db_version.result())
topics.append(rule2.result())

template = DocxTemplate('template.docx')

context = {
  'servername': ServerName().run(xl),
  'performer': 'Skie Report Tool',
  'day': datetime.datetime.now().strftime('%d'),
  'month': datetime.datetime.now().strftime('%m'),
  'year': datetime.datetime.now().strftime('%Y'),
  'topics': topics
}

template.render(context)

template.save('/Users/crivelaro/Downloads/generated_report.docx')

# for i in dir(rules):
#    print (i,"  ",type(getattr(rules,i)))
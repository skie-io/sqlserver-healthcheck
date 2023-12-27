import pandas as pd
from docxtpl import DocxTemplate
from rules.database_version import DatabaseVersionRule
import rules
import datetime

xl = pd.ExcelFile('test_files/Navisite_SQL_Assesment__FULL_AGDATA-SQL_09_12_2021.xlsx')

db_version = DatabaseVersionRule(xl)
db_version.run()

topics = [
  { "name": "Version and Edition", "description": "", "recommendation": "",
    "subtopics": [ 
      { "name": "Database Version", "description": db_version.attributes()["server_version"], "recommendation": ""},
      { "name": "Update Level", "description": db_version.attributes()["product_update_level"], "recommendation": ""}
    ]
  }
]

template = DocxTemplate('template.docx')

context = {
'servername': db_version.server_name,
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
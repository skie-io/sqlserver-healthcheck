import pandas as pd
from docxtpl import DocxTemplate
from rules.database_version import DatabaseVersionRule
from rules.instant_file import InstantFileRule
from rules.global_trace_flags import GlobalTraceFlags
#from rules.service_accounts import ServiceAccounts
from rules.instance_configurations import InstanceConfiguration
from server_name import ServerName
import datetime

xl = pd.ExcelFile('test_files/Navisite_SQL_Assesment__FULL_24-MWP-DBS1_01_28_2023.xlsx')

topics = []
rule_classes = [DatabaseVersionRule, InstantFileRule, GlobalTraceFlags, InstanceConfiguration]

for rule_class in rule_classes:
  rule = rule_class(xl)
  rule.run()
  if rule.generate_message():
    topics.append(rule.result())

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
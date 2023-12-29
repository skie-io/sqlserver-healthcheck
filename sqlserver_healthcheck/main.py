import pandas as pd
from docxtpl import DocxTemplate
from rules.database_version import DatabaseVersionRule
from rules.instant_file import InstantFileRule
from rules.global_trace_flags import GlobalTraceFlags
#from rules.service_accounts import ServiceAccounts
from rules.instance_configurations import InstanceConfiguration
from rules.memory import Memory
from rules.cpu import Cpu
from rules.wait_types import WaitTypes
from rules.sql_agent import SqlAgent
from rules.security import Security
from rules.database_io import DatabaseIo
from rules.database_configuration import DatabaseConfiguration
from rules.top_qureries import TopQueries
from rules.index_analysis import IndexAnalysis
from rules.maintenance import Maintanance
from server_name import ServerName
import datetime

xl = pd.ExcelFile('test_files/Navisite_SQL_Assesment__FULL_24-MWP-DBS1_01_28_2023.xlsx')

topics = []
rule_classes = [DatabaseVersionRule, InstantFileRule, GlobalTraceFlags, InstanceConfiguration, Memory, Cpu, WaitTypes, SqlAgent, Security, DatabaseIo, DatabaseConfiguration, TopQueries, IndexAnalysis, Maintanance]

for rule_class in rule_classes:
  rule = rule_class(xl)
  rule.run()
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
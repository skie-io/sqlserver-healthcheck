import pandas as pd
from rules.database_version import DatabaseVersionRule

xl = pd.ExcelFile('../test_files/Navisite_SQL_Assesment__FULL_AGDATA-SQL_09_12_2021.xlsx')

db_version = DatabaseVersionRule(xl)
db_version.run()

print(db_version.attributes())
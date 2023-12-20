import pandas as pd
from parser import parse

xl = pd.ExcelFile('../test_files/Navisite_SQL_Assesment__FULL_AGDATA-SQL_09_12_2021.xlsx')

df = parse(xl, "Sysadmin Server Role Members") 

print(df)

from lib.parser import parse
import re

class ServerName():
  def run(self, excel_file):
    df = parse(excel_file, "SQL Server and OS Version")
    first_line = df.iloc[0]
    return first_line['Server Name']
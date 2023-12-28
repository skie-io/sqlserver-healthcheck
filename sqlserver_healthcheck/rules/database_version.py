from rules.base_rule import BaseRule
from lib.parser import parse
import re

class DatabaseVersionRule(BaseRule):
  def run(self):
    self.df = parse(self.excel, "SQL Server and OS Version")
    self._get_os_version()
    self.df = parse(self.excel, "SQL Server Properties")
    self._get_product_update_level()

  def generate_message(self):
    True

  def topic_name(self):
    return "Version and Edition"
  
  def _get_os_version(self):
    first_line = self.df.iloc[0]
    sql_server_version = first_line['SQL Server and OS Version Info']
    sql_server_version = re.search("^Microsoft SQL Server \d{4} \([A-Z0-9\-]+\) \([A-Z0-9]+\)", sql_server_version)[0]
    self.add_subtopic("Database Version", sql_server_version)

  def _get_product_update_level(self):
    first_line = self.df.iloc[0]
    product_update_level = first_line['Product Update Level']
    self.add_subtopic("Product Update Level", product_update_level)
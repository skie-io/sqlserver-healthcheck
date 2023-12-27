from rules.base_rule import BaseRule
from lib.parser import parse
import re

class DatabaseVersionRule(BaseRule):
  def run(self):
    self.df = parse(self.excel, "SQL Server and OS Version")
    self._get_os_version()
    self._get_server_name()
    self.df = parse(self.excel, "SQL Server Properties")
    self._get_product_update_level()

  def generate_message(self):
    True

  def attributes(self):
    return {
      "server_version": self.sql_server_version,
      "product_update_level": self.product_update_level,
      "server_name": self.server_name
    }
  
  def recommendations(self):
    return "Update to the latest version of SQL Server."
  
  def _get_os_version(self):
    first_line = self.df.iloc[0]
    self.sql_server_version = first_line['SQL Server and OS Version Info']
    self.sql_server_version = re.search("^Microsoft SQL Server \d{4} \([A-Z0-9\-]+\) \([A-Z0-9]+\)", self.sql_server_version)[0]

  def _get_product_update_level(self):
    first_line = self.df.iloc[0]
    self.product_update_level = first_line['Product Update Level']

  def _get_server_name(self):
    first_line = self.df.iloc[0]
    self.server_name = first_line['Server Name']
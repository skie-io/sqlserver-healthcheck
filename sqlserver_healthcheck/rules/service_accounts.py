from rules.base_rule import BaseRule
from lib.parser import parse
import re

class ServiceAccountsRule(BaseRule):
  def run(self):
    self.df = parse(self.excel, "SQL Server and OS Version")
    self._get_os_version()
    self.df = parse(self.excel, "SQL Server Properties")
    self._get_product_update_level()

  def generate_message(self):
    True

  def attributes(self):
    return {
      "server_version": self.sql_server_version,
      "product_update_level": self.product_update_level
    }
  
  def recommendations(self):
    return ""
  
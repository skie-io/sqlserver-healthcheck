from rules.base_rule import BaseRule
from lib.parser import parse
import re

# I Don't know how to implement this rule
class ServiceAccountsRule(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Sysadmin Server Role Members")
    self._get_message()

  def topic_name(self):
    return "SQL Server Service Account"

from sqlserver_healthcheck.base_rule import BaseRule
from parser import parse

class OsVersionRule(BaseRule):
  def run(self):
    parse(self.excel, "Sysadmin Server Role Members") 

  def generate_message(self):
    False

  def __str__(self):
    return "OS Version Rule"
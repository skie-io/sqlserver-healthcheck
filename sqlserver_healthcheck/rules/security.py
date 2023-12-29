from rules.base_rule import BaseRule
from lib.parser import parse
import re

class Security(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._logins_with_blank_passwords()
    self._logins_with_equal_name()
    self._sysadmin_server_role_members()

  def topic_name(self):
    return "Security"
  
  def _logins_with_blank_passwords(self):
    pass

  def _logins_with_equal_name(self):
    pass

  def _sysadmin_server_role_members(self):
    pass
    
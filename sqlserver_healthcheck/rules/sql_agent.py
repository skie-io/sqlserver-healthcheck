from rules.base_rule import BaseRule
from lib.parser import parse
import re

class SqlAgent(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._alerts()
    self._jobs()

  def topic_name(self):
    return "SQL Agent"
  
  def _alerts(self):
    pass

  def _jobs(self):
    pass
    
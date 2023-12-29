from rules.base_rule import BaseRule
from lib.parser import parse
import re

class WaitTypes(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._analysis()

  def topic_name(self):
    return "Wait Types"
  
  def _analysis(self):
    pass

    
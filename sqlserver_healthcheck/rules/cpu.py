from rules.base_rule import BaseRule
from lib.parser import parse
import re

class Cpu(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._cpu_utitilization_history()
    self._cpu_utitilization_by_database()
    self._signal_waits()

  def topic_name(self):
    return "CPU"
  
  def _cpu_utitilization_history(self):
    pass

  def _cpu_utitilization_by_database(self):
    pass

  def _signal_waits(self):
    pass
    
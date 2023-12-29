from rules.base_rule import BaseRule
from lib.parser import parse
import re

class Maintanance(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._database_backups()
    self._statistics()
    self._integrity_checks()
    self._rebuild_indexes()

  def topic_name(self):
    return "Maintanance"
  
  def _database_backups(self):
    pass

  def _statistics(self):
    pass

  def _integrity_checks(self):
    pass

  def _rebuild_indexes(self):
    pass

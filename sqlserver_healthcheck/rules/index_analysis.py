from rules.base_rule import BaseRule
from lib.parser import parse
import re

class IndexAnalysis(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._hypothetical_indexex()
    self._most_costly_unused_indexes()
    self._missing_indexes()
    self._missing_indexes_warnings()
    self._statistics_health()
    self._active_heaps()
    self._duplicate_indexes()
    self._overlapping_indexes()

  def topic_name(self):
    return "Index Analysis"
  
  def _hypothetical_indexex(self):
    pass

  def _most_costly_unused_indexes(self):
    pass

  def _missing_indexes(self):
    pass

  def _missing_indexes_warnings(self):
    pass

  def _statistics_health(self):
    pass

  def _active_heaps(self):
    pass

  def _duplicate_indexes(self):
    pass

  def _overlapping_indexes(self):
    pass
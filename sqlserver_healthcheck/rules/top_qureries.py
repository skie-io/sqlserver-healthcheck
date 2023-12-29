from rules.base_rule import BaseRule
from lib.parser import parse
import re

class TopQueries(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._top_worker_time_queries()
    self._top_logical_reads_queries()
    self._top_elapsed_time_queries()

  def topic_name(self):
    return "Top Queries"
  
  def _top_worker_time_queries(self):
    pass

  def _top_logical_reads_queries(self):
    pass

  def _top_elapsed_time_queries(self):
    pass
from rules.base_rule import BaseRule
from lib.parser import parse
import re

class DatabaseIo(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._database_volume_information()
    self._io_utilization_by_database()
    self._database_latency()

  def topic_name(self):
    return "Database I/O"
  
  def _database_volume_information(self):
    pass

  def _io_utilization_by_database(self):
    pass

  def _database_latency(self):
    pass
    
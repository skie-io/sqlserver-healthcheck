from rules.base_rule import BaseRule
from lib.parser import parse
import re

class Memory(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._memory_dumps()
    self._system_memory()
    self._process_memory()
    self._ring_buffer()
    self._buffer_usage()
    self._page_cache_detail()

  def topic_name(self):
    return "Memory"
  
  def _memory_dumps(self):
    pass

  def _system_memory(self):
    pass

  def _process_memory(self):
    pass

  def _ring_buffer(self):
    pass

  def _buffer_usage(self):
    pass

  def _page_cache_detail(self):
    pass
    
from rules.base_rule import BaseRule
from lib.parser import parse
import re

class InstantFileRule(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._get_message()
    
  def generate_message(self):
    return True

  def topic_name(self):
    return "Instant File Initialization"
  
  def _get_message(self):
    first_line = self.df.iloc[0]
    self.priviledges_information = first_line['Privileges Information']
    m = re.search("^Error", self.priviledges_information)
    if m: 
      self.configured = False
      self.set_description("Instant File Initialization is not enabled")
      self.set_recommendation("Recommend enabling Instant File Initialization")
    else:
      self.configured = True
      self.set_description("Instant File Initialization is enabled")
    
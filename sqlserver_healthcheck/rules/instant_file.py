from rules.base_rule import BaseRule
from lib.parser import parse
import re

class ServiceAccountsRule(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._get_message()
    
  def generate_message(self):
    True

  def attributes(self):
    return {
      "configured": self.configured
    }
  
  def recommendations(self):
    return ""
  
  def __get_message(self):
    first_line = self.df.iloc[0]
    self.priviledges_information = first_line['Privileges Information']
    m = re.search("^Error", self.priviledges_information)
    if m: 
      self.configured = False 
    else:
      self.configured = True
    
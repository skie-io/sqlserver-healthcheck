from rules.base_rule import BaseRule
from lib.parser import parse
import re

class GlobalTraceFlags(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Global Trace Flags")
    self._get_message()
    
  def generate_message(self):
    return True

  def topic_name(self):
    return "Global Trace Flags"
  
  def _get_message(self):
    if (self.df.shape[0] == 0):
      self.set_description("No Global Trace Flags are configured")
      self.set_recommendation("Recommend enabling trace flags below:\n3226 - This is used to suppress writing successful backup events to error logs.\n1222 - This trace flag is used Writes deadlock info into SQL error log.\n2371 - The statistics of a table will only be automatically updated if the number of rows changed exceed a threshold.")
    else:
      msg = ""
      if self.df[self.df['TraceFlag'] == "3226"].shape[0] == 0:
        msg += "3226 - This is used to suppress writing successful backup events to error logs.\n"
      if self.df[self.df['TraceFlag'] == "1222"].shape[0] == 0:
        msg += "1222 - This trace flag is used Writes deadlock info into SQL error log.\n"
      if self.df[self.df['TraceFlag'] == "2371"].shape[0] == 0:
        msg += "2371 - The statistics of a table will only be automatically updated if the number of rows changed exceed a threshold."
      
      if msg == "":
        self.set_description("All Global Trace Flags are configured")
      else:
        self.set_description("Important Global Trace Flags are not configured")
        self.set_recommendation("Recommend enabling trace flags below:\n" + msg)
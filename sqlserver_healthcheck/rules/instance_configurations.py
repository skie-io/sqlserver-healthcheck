from rules.base_rule import BaseRule
from lib.parser import parse
import re

class InstanceConfiguration(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instance Configuration Values")
    self._cost_of_thresold_parallelism()
    self._max_degree_of_parallelism()
    self._optimize_for_adhoc_workloads()
    self._remote_admin_connections()
    self._max_server_memory()

  def topic_name(self):
    return "Instance Configuration"
  
  def _cost_of_thresold_parallelism(self):
    item = self.df[self.df['Name'] == "cost threshold for parallelism"]
    value = item["Value"].item()
    if value <= 5: # Magic number, I don't know what is the best value
      self.add_subtopic("Cost threshold for parallelism", value)
    else:
      self.add_subtopic("Cost threshold for parallelism", value, "Recommend to set to XXXX")

  def _max_degree_of_parallelism(self):
    item = self.df[self.df['Name'] == "max degree of parallelism"]
    value = item["Value"].item()
    if value <= 5: # Magic number, I don't know what is the best value
      self.add_subtopic("Max degree of parallelism", value)
    else:
      self.add_subtopic("Max degree of parallelism", value, "Recommend to set to XXXX")

  def _optimize_for_adhoc_workloads(self):
    item = self.df[self.df['Name'] == "optimize for ad hoc workloads"]
    value = item["Value"].item()
    if value <= 5: # Magic number, I don't know what is the best value
      self.add_subtopic("Optimize for adhoc workloads", value)
    else:
      self.add_subtopic("Optimize for ad hoc workloads", value, "Recommend to set to XXXX")

  def _remote_admin_connections(self):
    item = self.df[self.df['Name'] == "remote admin connections"]
    value = item["Value"].item()
    value = item["Value"].item()
    if item["Value"].item() == 1:
      self.add_subtopic("Remote admin connections", "Enabled")
    else:
      self.add_subtopic("Remote admin connections", "Disabled", "Recommend to enable")

  def _max_server_memory(self):
    server_memory = 10000 # Magic number, I don't know what is the best value
    threshold = int(0.8 * server_memory) # Magic number, I don't know what is the best value
    item = self.df[self.df['Name'] == "max server memory (MB)"]
    value = item["Value"].item()
    if item["Value"].item() >= threshold: 
      self.add_subtopic("Max server memory", f"Set to {value} out of {threshold} server memory")
    else:
      self.add_subtopic("Max server memory", f"Set to {value} out of {threshold} server memory", "Recommend to set to XXXX")

  def _priority_boost(self):
    item = self.df[self.df['Name'] == "priority boost"]
    value = item["Value"].item()
    if item["Value"].item() == 0:
      self.add_subtopic("Priority Boost", "Disabled")
    else:
      self.add_subtopic("Priority Boost", "Enabled", "Recommend to disable")
from rules.base_rule import BaseRule
from lib.parser import parse
import re

class DatabaseConfiguration(BaseRule):
  def run(self):
    self.df = parse(self.excel, "Instant File Initialization")
    self._db_file_location()
    self._db_file_size_space()
    self._temp_db()
    self._autogrowth()
    self._settings()
    self._dbs_without_log_backup()
    self._unstrusted_foreign_keys_and_constraints()
    self._db_corruption()

  def topic_name(self):
    return "Database Configuration"
  
  def _db_file_location(self):
    pass

  def _db_file_size_space(self):
    pass

  def _temp_db(self):
    pass

  def _autogrowth(self):
    pass

  def _settings(self):
    pass

  def _dbs_without_log_backup(self):
    pass

  def _unstrusted_foreign_keys_and_constraints(self):
    pass

  def _db_corruption(self):
    pass
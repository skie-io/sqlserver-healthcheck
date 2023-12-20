class BaseRule():
  def __init__(self, excel_file):
    self.excel = excel_file

  def run(self):
    NotImplementedError("Please implement this method")

  def generate_message(self):
    False

  def __str__(self):
    return ""
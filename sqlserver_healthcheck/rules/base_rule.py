class BaseRule():
  def __init__(self, excel_file):
    self.excel = excel_file
    self.subtopics = []
    self.description = ""
    self.recommendation = ""
    self.show_description = False

  def add_subtopic(self, name, description, recommendation = None):
    self.subtopics.append({ "name": name, "description": description, "recommendation": recommendation})

  def topic_name(self):
    NotImplementedError("Please implement this method")

  def run(self):
    NotImplementedError("Please implement this method")

  def generate_message(self):
    False

  def __str__(self):
    return ""
  
  def set_description(self, description):
    self.show_description = True
    self.description = description

  def set_recommendation(self, recommendation):
    self.recommendation = recommendation

  def result(self):
    return { "name": self.topic_name(), "show_description": self.show_description, "description": self.description, "recommendation": self.recommendation, "subtopics": self.subtopics }
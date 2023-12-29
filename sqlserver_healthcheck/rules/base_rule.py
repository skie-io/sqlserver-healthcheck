class BaseRule():
  def __init__(self, excel_file):
    self.excel = excel_file
    self.subtopics = []
    self.description = ""
    self.recommendation = ""
    self.show_description = False
    self.show_recommendation = False

  def add_subtopic(self, name, description, recommendation = ""):
    show_recommendation = (recommendation != "")
    self.subtopics.append({ "name": name, "description": description, "recommendation": recommendation, "show_recommendation": show_recommendation})

  def topic_name(self):
    NotImplementedError("Please implement this method")

  def run(self):
    NotImplementedError("Please implement this method")
  
  def set_description(self, description):
    self.show_description = True
    self.description = description

  def set_recommendation(self, recommendation):
    self.show_recommendation = True
    self.recommendation = recommendation

  def result(self):
    return { "name": self.topic_name(), "show_description": self.show_description, "description": self.description, "recommendation": self.recommendation, "show_recommendation": self.show_recommendation, "subtopics": self.subtopics }
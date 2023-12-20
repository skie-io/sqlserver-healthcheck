import pandas as pd

def parse(excel_file, tab_name):
  df = excel_file.parse(tab_name) 

  new_header = df.iloc[1] #grab the first row for the header
  df = df[2:] #take the data less the header row
  df.columns = new_header #set the header row as the df header
  df.reset_index()

  return df
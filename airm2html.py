def create_contextual_model_abbreviations_index_page():
  from bs4 import BeautifulSoup
  import os
  airm_cx_pages_directory = "docs/airm/viewer/1.0.0/contextual-model"
  path = airm_cx_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)
  
  import airm
  airm = airm.Airm()
  airm_abbreviations = airm.contextual_abbreviations.to_dict('records')
  html = open("docs/airm/templates/viewer/contextual-model-abbreviations-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+ filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(1,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(2,td_def)
     
      soup.find('tbody').insert(1,tr)
  
  f= open("docs/airm/viewer/1.0.0/contextual-model-abbreviations.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_contextual_model_abbreviations_with_supplements_index_page():
  pass
def create_contextual_model_abbreviations_item_pages():
  pass

def create_contextual_model_terms_index_page():
  pass
def create_contextual_model_terms_with_supplements_index_page():
  pass
def create_contextual_model_terms_item_pages():
  pass

def create_conceptual_model_index_page():
  pass
def create_conceptual_model_with_supplements_index_page():
  pass
def create_conceptual_model_item_pages():
  pass

def create_logical_model_index_page():
  pass
def create_logical_model_with_supplements_index_page():
  pass
def create_logical_model_item_pages():
  pass
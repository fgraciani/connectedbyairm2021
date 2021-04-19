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
  from bs4 import BeautifulSoup
  import airm
  airm = airm.Airm()
  airm_abbreviations = airm.contextual_abbreviations.to_dict('records')
  html = open("docs/airm/templates/viewer/contextual-model-abbreviations-with-supplements-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      tr.insert(1,td_supplement)

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(2,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(3,td_def)
     
      soup.find('tbody').insert(1,tr)
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      span_supplement = soup.new_tag("spam")
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
      td_supplement.insert(1,span_supplement)
      tr.insert(1,td_supplement)
      
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/european-supplement/"+filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(2,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(3,td_def)
     
      soup.find('tbody').insert(1,tr)

  f= open("docs/airm/viewer/1.0.0/contextual-model-abbreviations-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_contextual_model_abbreviations_item_pages():
  from bs4 import BeautifulSoup
  import airm
  airm = airm.Airm()
  airm_abbs = airm.contextual_abbreviations.to_dict('records')

  for record in airm_abbs:
    
    if record["supplement"] == "\t\t\t":
      html = open("docs/airm/templates/viewer/contextual-model/contextual-model-abbreviation-template.html").read()
      directory = "docs/airm/viewer/1.0.0/contextual-model/"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      html = open("docs/airm/templates/viewer/contextual-model/european-supplement/contextual-model-abbreviation-template.html").read()
      directory = "docs/airm/viewer/1.0.0/contextual-model/european-supplement/"
          
    print(record['class name'])
    soup = BeautifulSoup(html, "lxml") 

    soup.title.string = str(record['class name'])+" - Contextual Model | AIRM.aero"
    soup.find(text="CONCEPT_NAME_BC").replace_with(str(record['class name']))

    h2 = soup.new_tag("h2")
    h2.string = str(record['class name'])

    span_supplement = soup.new_tag("spam")
    if record["supplement"] == "\t\t\tEuropean Supplement":
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
    h2.insert(1,span_supplement)

    soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
    code = soup.new_tag("code")
    code.string = record['urn']
    code["class"] = "text-secondary"
    soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
    soup.find(text="CONCEPT_DEFINITION").replace_with(str(record['definition']))
    
    p = soup.new_tag("p")
    p.string = "Source: "
    span = soup.new_tag("span")
    span.string = record["source"]
    p.insert(2,span)
    soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,p)
    filename = str(record['class name'])+".html"
    filename = filename.replace("/", "-")
    filename = filename.replace("*", "-")
    filename = filename.replace(" ", "")
    filename = filename.replace("\t", "")
    filename = filename.replace("\n", "")
    f= open(directory + filename,"w+")
    f.write(soup.prettify())
    f.close()

def create_contextual_model_terms_index_page():
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
  airm_terms = airm.contextual_terms.to_dict('records')
  html = open("docs/airm/templates/viewer/contextual-model-terms-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_terms:
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
      url = "contextual-model/"+filename
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
  
  f= open("docs/airm/viewer/1.0.0/contextual-model-terms.html","w+")
  f.write(soup.prettify())
  f.close() 
  
def create_contextual_model_terms_with_supplements_index_page():
  from bs4 import BeautifulSoup
  import airm
  airm = airm.Airm()
  airm_terms = airm.contextual_terms.to_dict('records')
  html = open("docs/airm/templates/viewer/contextual-model-terms-with-supplements-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_terms:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      tr.insert(1,td_supplement)

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(2,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(3,td_def)
     
      soup.find('tbody').insert(1,tr)
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      span_supplement = soup.new_tag("spam")
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
      td_supplement.insert(1,span_supplement)
      tr.insert(1,td_supplement)
      
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/european-supplement/"+filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(2,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(3,td_def)
     
      soup.find('tbody').insert(1,tr)

  f= open("docs/airm/viewer/1.0.0/contextual-model-terms-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close()

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
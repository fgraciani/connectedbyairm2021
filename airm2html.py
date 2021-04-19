def create_contextual_model_abbreviations_index_page():
  import airm
  airm = airm.Airm()
  airm_abbreviations = airm.contextual_abbreviations.to_dict('records')
  template = open("docs/airm/templates/viewer/contextual-model-abbreviations-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "contextual-model/"

  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":     
      soup.find('tbody').insert(1,create_index_row(record,directory))
  
  f= open("docs/airm/viewer/1.0.0/contextual-model-abbreviations.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_contextual_model_abbreviations_with_supplements_index_page():
  import airm
  airm = airm.Airm()
  airm_abbreviations = airm.contextual_abbreviations.to_dict('records')
  template = open("docs/airm/templates/viewer/contextual-model-abbreviations-with-supplements-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "contextual-model/"
  
  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      directory=directory+"european-supplement/"
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))

  f= open("docs/airm/viewer/1.0.0/contextual-model-abbreviations-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_contextual_model_abbreviations_item_pages():
  import airm
  airm = airm.Airm()
  airm_abbs = airm.contextual_abbreviations.to_dict('records')

  for record in airm_abbs:
    
    if record["supplement"] == "\t\t\t":
      template = open("docs/airm/templates/viewer/contextual-model/contextual-model-abbreviation-template.html").read()
      directory = "docs/airm/viewer/1.0.0/contextual-model/"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      template = open("docs/airm/templates/viewer/contextual-model/european-supplement/contextual-model-abbreviation-template.html").read()
      directory = "docs/airm/viewer/1.0.0/contextual-model/european-supplement/"
          
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(template, "lxml") 

    print(record['class name'])
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
    filename = classname_to_filename(str(record['class name']))
    f= open(directory + filename,"w+")
    f.write(soup.prettify())
    f.close()

def create_contextual_model_terms_index_page():
  import airm
  airm = airm.Airm()
  airm_abbreviations = airm.contextual_abbreviations.to_dict('records')
  template = open("docs/airm/templates/viewer/contextual-model-terms-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "contextual-model/"

  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":     
      soup.find('tbody').insert(1,create_index_row(record,directory))
  
  f= open("docs/airm/viewer/1.0.0/contextual-model-terms.html","w+")
  f.write(soup.prettify())
  f.close() 
  
def create_contextual_model_terms_with_supplements_index_page():
  import airm
  airm = airm.Airm()
  airm_abbreviations = airm.contextual_abbreviations.to_dict('records')
  template = open("docs/airm/templates/viewer/contextual-model-terms-with-supplements-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "contextual-model/"
  
  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      directory=directory+"european-supplement/"
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))

  f= open("docs/airm/viewer/1.0.0/contextual-model-terms-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close()

def create_contextual_model_terms_item_pages():
  import airm
  airm = airm.Airm()
  airm_terms = airm.contextual_terms.to_dict('records')

  for record in airm_terms:
    
    if record["supplement"] == "\t\t\t":
      template = open("docs/airm/templates/viewer/contextual-model/contextual-model-term-template.html").read()
      directory = "docs/airm/viewer/1.0.0/contextual-model/"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      template = open("docs/airm/templates/viewer/contextual-model/european-supplement/contextual-model-term-template.html").read()
      directory = "docs/airm/viewer/1.0.0/contextual-model/european-supplement/"
          
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(template, "lxml") 

    print(record['class name'])
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
    insert_index = 1
    if record["source"] != "missing data":
      b = soup.new_tag("b")
      b.string = "Source: "
      p.insert(insert_index,b)
      insert_index = insert_index+1

      span = soup.new_tag("span")
      span.string = record["source"]
      p.insert(insert_index,span)
      insert_index = insert_index+1

      br = soup.new_tag("br")
      p.insert(insert_index,br)
      insert_index = insert_index+1

    if record["synonyms"] != "missing data":
      b = soup.new_tag("b")
      b.string = "Synonyms: "
      p.insert(insert_index,b)
      insert_index = insert_index+1

      span = soup.new_tag("span")
      span.string = record["synonyms"]
      p.insert(insert_index,span)
      insert_index = insert_index+1

      br = soup.new_tag("br")
      p.insert(insert_index,br)
      insert_index = insert_index+1

    if record["abbreviation"] != "missing data":
      b = soup.new_tag("b")
      b.string = "Abbreviations: "
      p.insert(insert_index,b)
      insert_index = insert_index+1

      span = soup.new_tag("span")
      span.string = record["abbreviation"]
      p.insert(insert_index,span)
      insert_index = insert_index+1

      br = soup.new_tag("br")
      p.insert(insert_index,br)
      insert_index = insert_index+1

    soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_index,p)

    filename = classname_to_filename(str(record['class name']))
    f= open(directory + filename,"w+")
    f.write(soup.prettify())
    f.close()


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

def classname_to_filename(class_name):
  filename = class_name+".html"
  filename = filename.replace("/", "-")
  filename = filename.replace("*", "-")
  filename = filename.replace(" ", "")
  filename = filename.replace("\t", "")
  filename = filename.replace("\n", "")
  return filename

def create_index_row(record, directory):
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = classname_to_filename(str(record['class name']))
      url = directory + filename
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
      return tr
  else:
    return None

def create_index_row_with_supplements(record, directory):
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      tr.insert(1,td_supplement)

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = classname_to_filename(str(record['class name']))
      url = directory + filename
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
     
      return tr
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
      filename = classname_to_filename(str(record['class name']))
      url = directory + filename
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
     
      return tr
  else:
    return None
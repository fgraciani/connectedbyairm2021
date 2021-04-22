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
  
  for record in airm_abbreviations:
    if record["supplement"] == "\t\t\t":
      directory = "contextual-model/"
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      directory="contextual-model/european-supplement/"
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
  airm_terms = airm.contextual_terms.to_dict('records')
  template = open("docs/airm/templates/viewer/contextual-model-terms-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "contextual-model/"

  for record in airm_terms:
    if record["supplement"] == "\t\t\t":     
      soup.find('tbody').insert(1,create_index_row(record,directory))
  
  f= open("docs/airm/viewer/1.0.0/contextual-model-terms.html","w+")
  f.write(soup.prettify())
  f.close() 
  
def create_contextual_model_terms_with_supplements_index_page():
  import airm
  airm = airm.Airm()
  airm_terms = airm.contextual_terms.to_dict('records')
  template = open("docs/airm/templates/viewer/contextual-model-terms-with-supplements-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  
  for record in airm_terms:
    if record["supplement"] == "\t\t\t":
      directory = "contextual-model/"
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      directory = "contextual-model/european-supplement/"
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
  import airm
  airm = airm.Airm()
  airm_concepts = airm.conceptual_concepts.to_dict('records')
  template = open("docs/airm/templates/viewer/conceptual-model-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "conceptual-model/"

  for record in airm_concepts:
    if record["supplement"] == "\t\t\t":     
      soup.find('tbody').insert(1,create_index_row(record,directory))
  
  f= open("docs/airm/viewer/1.0.0/conceptual-model.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_conceptual_model_with_supplements_index_page():
  import airm
  airm = airm.Airm()
  airm_concepts = airm.conceptual_concepts.to_dict('records')
  airm_concepts_supp = airm.conceptual_supp_concepts.to_dict('records')
  template = open("docs/airm/templates/viewer/conceptual-model-with-supplements-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  
  for record in airm_concepts:
    if record["supplement"] == "\t\t\t":
      directory = "conceptual-model/"
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))

  for record in airm_concepts_supp:
    if record["supplement"] == "\t\t\tEuropean Supplement":
      directory="conceptual-model/european-supplement/"
      soup.find('tbody').insert(1,create_index_row_with_supplements(record,directory))

  f= open("docs/airm/viewer/1.0.0/conceptual-model-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_conceptual_model_item_pages():
  import airm
  airm = airm.Airm()
  airm_concepts = airm.conceptual_concepts.to_dict('records')
  airm_concepts_supp = airm.conceptual_supp_concepts.to_dict('records')

  for record in airm_concepts_supp:
    template = open("docs/airm/templates/viewer/conceptual-model/european-supplement/conceptual-model-concept-template.html").read()
    scope = "european-supplement/"
    create_conceptual_model_item_page(record, template, scope)

  for record in airm_concepts:
    template = open("docs/airm/templates/viewer/conceptual-model/conceptual-model-concept-template.html").read()
    scope = ""
    create_conceptual_model_item_page(record, template, scope)

def create_conceptual_model_item_page(record, template, scope):
    if record["stereotype"] != "missing data":
      print(record['class name'])
      from bs4 import BeautifulSoup
      soup = BeautifulSoup(template, "lxml") 

      soup.title.string = str(record['class name'])+" - Conceptual Model | AIRM.aero"
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
        span.string = str(record["abbreviation"])
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1
      
      # Insert related concepts
      import airm
      airm = airm.Airm()
      results = airm.get_concept_properties_by_parent(str(record['class name']), scope)
      if results != None:
        print("RESULTS for " + str(record['class name'])+ "SCOPE: "+scope)
        print(results)
        hr = soup.new_tag("hr")
        p.insert(insert_index,hr)
        insert_index = insert_index+1

        b = soup.new_tag("b")
        b.string = "Related: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

        for result in results:
          print('\t'+result['property name'])
          
          span = soup.new_tag("span")
          span.string = result["property name"]
          p.insert(insert_index,span)
          insert_index = insert_index+1

          url = create_url_for_supplements(str(result['type']), result['type urn'], scope)

          text = result["type"]
          print(text)
          new_link = soup.new_tag("a")
          new_link['href'] = url
          new_link.string = text
          p.insert(insert_index,new_link)
          insert_index = insert_index+1

          br = soup.new_tag("br")
          p.insert(insert_index,br)
          insert_index = insert_index+1

      soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_index,p)
      
      filename = classname_to_filename(str(record['class name']))
      f= open("docs/airm/viewer/1.0.0/conceptual-model/" + scope + filename,"w+")
      f.write(soup.prettify())
      f.close()

def create_logical_model_index_page():  
  import airm
  airm = airm.Airm()
  airm_logical_concepts = airm.logical_concepts.to_dict('records')
  template = open("docs/airm/templates/viewer/logical-model-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  directory = "logical-model/"

  for record in airm_logical_concepts:
    soup.find('tbody').insert(1,create_index_row_logical_model(record,directory))
  
  f= open("docs/airm/viewer/1.0.0/logical-model.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_logical_model_with_supplements_index_page():  
  import airm
  airm = airm.Airm()
  airm_logical_concepts = airm.logical_concepts.to_dict('records')
  airm_logical_concepts_supp = airm.logical_supp_concepts.to_dict('records')
  template = open("docs/airm/templates/viewer/logical-model-with-supplements-template.html").read()

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(template, "lxml")
  
  for record in airm_logical_concepts:
      directory = "logical-model/"
      soup.find('tbody').insert(1,create_index_row_logical_model_with_supplements(record,directory))

  for record in airm_logical_concepts_supp:
      directory="logical-model/european-supplement/"
      soup.find('tbody').insert(1,create_index_row_logical_model_with_supplements(record,directory))

  f= open("docs/airm/viewer/1.0.0/logical-model-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_logical_model_item_pages():
  import airm
  airm = airm.Airm()
  airm_logical_concepts = airm.logical_concepts.to_dict('records')
  airm_logical_concepts_supp = airm.logical_supp_concepts.to_dict('records')

  for record in airm_logical_concepts_supp:
    template = open("docs/airm/templates/viewer/logical-model/european-supplement/logical-model-concept-template.html").read()
    scope = "european-supplement/"
    children = airm.get_children_for_logical_model_class(record["urn"], scope)
    create_logical_model_item_page(record, template, scope, children)

  for record in airm_logical_concepts:
    template = open("docs/airm/templates/viewer/logical-model/logical-model-concept-template.html").read()
    scope = ""
    children = airm.get_children_for_logical_model_class(record["urn"], scope)
    supplements = airm.get_supplements_for_logical_model_class(record["urn"])
    create_logical_model_item_page(record, template, scope, children, supplements)

def create_logical_model_item_page(record, template, scope, children, supplements=None):

    if record["stereotype"] != "missing data":
      print(record['class name'])
      from bs4 import BeautifulSoup
      soup = BeautifulSoup(template, "lxml") 

      soup.title.string = str(record['class name'])+" - Logical Model | AIRM.aero"
      
      soup.find(text="FIXM_CLASS_NAME_BC").replace_with(str(record['class name']))

      h2 = soup.new_tag("h2")
      h2.string = str(record['class name'])
      span_supplement = soup.new_tag("spam")
      if scope=="european-supplement/":
        span_supplement['class'] = "badge badge-secondary"
        span_supplement.string = "European Supplement"
      h2.insert(1,span_supplement)
      soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)

      code = soup.new_tag("code")
      code.string = record['urn']
      code["class"] = "text-secondary"
      soup.find(id="INFO_CONCEPT_NAME").insert(1,code)

      soup.find(text="FIXM_CLASS_DEFINITION").replace_with(str(record['definition']))
      
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
      
      #insert parent
      if record["parent"] != "missing data":
        b = soup.new_tag("b")
        parent = str(record["parent"])    

        if scope=="european-supplement/":
          if "ses:eurocontrol" in record["parent urn"]:
            b.string = "Parent concept: : "
          else:
            b.string = "Supplements: "
        else:
          b.string = "Parent concept: "
        p.insert(insert_index,b)
        insert_index = insert_index+1        
        
        url = create_url_for_supplements(str(record["parent"]), str(record["parent urn"]), scope)
        text = parent
        print("-parent: "+text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link.string = text
        p.insert(insert_index,new_link)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1
      #insert children
      if children != None: 
        b = soup.new_tag("b")
        b.string = "Children: "
        p.insert(insert_index,b)
        insert_index = insert_index+1 
        for child in children:
          url = create_url_for_supplements(str(child["class name"]), str(record["urn"]), scope)
          text = str(child["class name"])+"; "
          print("-child: "+text)
          new_link = soup.new_tag("a")
          new_link['href'] = url
          new_link.string = text
          p.insert(insert_index,new_link)
          insert_index = insert_index+1
        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

      #insert supplemented by
      if supplements != None: 
        b = soup.new_tag("b")
        b.string = "Supplemented by: "
        p.insert(insert_index,b)
        insert_index = insert_index+1 
        for entry in supplements:
          url = create_url_for_supplements(str(entry["class name"]), str(entry["urn"]), scope)
          text = str(entry["class name"])+"; "
          print("-supplemented by: "+text)
          new_link = soup.new_tag("a")
          new_link['href'] = url
          new_link.string = text
          p.insert(insert_index,new_link)
          insert_index = insert_index+1
        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

      # Insert properties
      import airm
      airm = airm.Airm()
      results = airm.get_logical_properties_by_class(str(record['class name']), scope)
      if results != None:
        print("-scope: "+scope)
        hr = soup.new_tag("hr")
        p.insert(insert_index,hr)
        insert_index = insert_index+1

        b = soup.new_tag("b")
        b.string = "Properties: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

        for result in results:

          tr = soup.new_tag("tr")

          if result["property name"] != "":
            td_dc_name = soup.new_tag("td")
            url = "#"+str(result["property name"])
            text = str(result["property name"])
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            td_dc_name.insert(1,new_link)
            tr.insert(1,td_dc_name)
          
          if result["definition"] != "":
            td_def = soup.new_tag("td")
            td_def.string = str(result["definition"])
            tr.insert(2,td_def)
          
          if record["stereotype"] == "CodeList":
            td_dc_type = soup.new_tag("td")
            enump = soup.new_tag("p")
            enump.string = "enum value"
            td_dc_type.insert(1,enump)
            tr.insert(3,td_dc_type)
          elif str(result["type"]) in ["Integer", "CharacterString", "Boolean", "Number", "Date", "DateTime", "TM_Duration", "GM_Curve", "GM_Point", "GM_Solid", "GM_Surface", "MD_Metadata", "Angle", "Decimal", "Real", "Bit", "LanguageCode", "ClockTime"]:
            td_dc_type = soup.new_tag("td")
            enump = soup.new_tag("p")
            enump.string = str(result["type"])
            td_dc_type.insert(1,enump)
            tr.insert(3,td_dc_type)
          elif result["type"] != "":
            td_dc_type = soup.new_tag("td")
            url = create_url_for_supplements(str(result['type']), str(result['type urn']), scope)
            text = str(result["type"])
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            td_dc_type.insert(1,new_link)
            tr.insert(3,td_dc_type)
          
          soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)
        for trace in results:
          print('\t+'+str(trace['property name']))
          property_div = soup.new_tag("div")
          property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"

          h3 = soup.new_tag("h3")
          h3.string = str(trace["property name"])
          h3["id"] = str(trace["property name"])
          h3["style"] = "padding-top: 120px; margin-top: -120px;"
          property_div.insert(0,h3)

          code = soup.new_tag("code")
          identifier = trace['urn']
          code.string = identifier
          code["class"] = "text-secondary"
          property_div.insert(1,code)
          
          p2 = soup.new_tag("p")
          p2.string = str(trace["definition"])
          br = soup.new_tag("br")
          p2.insert(2,br)
          property_div.insert(2,p2)
          
          if record["stereotype"] == "CodeList":
            p3 = soup.new_tag("p")
            p3.string = "type: enum value"
            property_div.insert(3,p3)
          elif str(trace["type"]) in ["Integer", "CharacterString", "Boolean", "Number", "Date", "DateTime", "TM_Duration", "GM_Curve", "GM_Point", "GM_Solid", "GM_Surface", "MD_Metadata", "Angle", "Decimal", "Real", "Bit", "LanguageCode", "ClockTime"]:
            td_dc_type = soup.new_tag("td")
            enump = soup.new_tag("p")
            enump.string = "type: "+str(trace["type"])
            property_div.insert(3,enump)
          else:
            p3 = soup.new_tag("p")
            p3.string = "type: "
            span = soup.new_tag("span")
            url = create_url_for_supplements(str(trace['type']), trace['type urn'], scope)
            text = trace["type"]
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            span.insert(1,new_link)
            p3.insert(2,span)
            property_div.insert(3,p3)

          connections = airm.get_connections_by_urn(trace['urn'])
          if connections != None:
            p4 = soup.new_tag("p")
            button = soup.new_tag("button")
            button["class"] = "btn btn-light"
            button["type"] = "button"
            button["data-toggle"] = "collapse"
            button["data-target"] = "#"+str(trace["property name"])+"collapse"
            button["aria-expanded"] = "false"
            button["aria-controls"] = "collapseExample"
            button.string = "Show correspondences"
            p4.insert(1,button)
            property_div.insert(4,p4)

            sc_div = soup.new_tag("div")
            sc_div["class"] = "table-responsive collapse"
            sc_div["id"] = str(trace["property name"])+"collapse"
            sc_table = soup.new_tag("table")
            sc_table["class"] = "table"
            sc_thead = soup.new_tag("thead")
            tr = soup.new_tag("tr")
            th = soup.new_tag("th")
            th.string = "Model"
            tr.insert(1,th)
            th = soup.new_tag("th")
            th.string = "Concept"
            tr.insert(2,th)
            sc_thead.insert(1,tr)
            sc_table.insert(1,sc_thead)
            tbody = soup.new_tag("tbody")
          
            for entry in connections:
              tr = soup.new_tag("tr")
              url_path = ""

              if scope == "european-supplement/":
                url_path = "../../../../developers/"
              else:
                url_path = "../../../developers/"

              if entry["concept_name"] != 'missing data':
                print('\t\t*'+str(entry["concept_target"]))
                td = soup.new_tag("td")
                text = entry["model_name"]
                pm = soup.new_tag("p")
                pm.string = text
                td.insert(1,pm)
                tr.insert(1,td)
                td = soup.new_tag("td")
                url = url_path+entry["model_path"]+"/"+entry["concept_target"]
                text = entry["concept_name"]
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a.string = text
                td.insert(1,a)
                tr.insert(2,td)
              tbody.insert(1,tr)

            sc_table.insert(2,tbody)
            sc_div.insert(1,sc_table)
            property_div.insert(5,sc_div)

          top_link_p = soup.new_tag("p")
          new_link = soup.new_tag("a")
          new_link['href'] = "#top"
          new_icon = soup.new_tag("i")
          new_icon['class'] = "fa fa-arrow-circle-up"
          new_icon["data-toggle"] = "tooltip"
          new_icon["data-placement"] = "left"
          new_icon["title"] = "Top of page"
          new_link.insert(1,new_icon)
          top_link_p.insert(1,new_link)
          top_link_p['class'] =   "text-right"
          property_div.insert(6,top_link_p)

          soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)
          
      soup.find(id="INFO_CONCEPT_OTHER").insert(insert_index,p)

      filename = classname_to_filename(str(record['class name']))
      f= open("docs/airm/viewer/1.0.0/logical-model/"+scope + filename,"w+")
      f.write(soup.prettify())
      f.close()

def create_url_for_supplements(class_name, class_urn, scope):
  filename = classname_to_filename(class_name)
  if "ses:eurocontrol" in class_urn:#target is in eur supp
    if scope == "european-supplement/":#current page in eur supp
      path = ""
    else:#current page in global
      path = "european-supplement/"
  else:#target is in global
    if scope == "european-supplement/":
      path = "../"
    else:
      path = ""
  url = path+filename
  return url

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

def create_index_row_logical_model(record, directory):
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  if record["supplement"] == "\t\t\t" or record["supplement"] == "\t":
      tr = soup.new_tag("tr")
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      if record["stereotype"] != "missing data": #The record is a class
        filename = classname_to_filename(str(record['class name']))
        url = "logical-model/"+filename
        text = record["class name"]
        print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_ic_name.insert(1,new_link)
        tr.insert(1,td_ic_name)
      else: #The record is a property
        td_ic_name.string = record["class name"]
        tr.insert(1,td_ic_name)
      
      td_dc_name = soup.new_tag("td")
      td_dc_name["data-order"] = str(record["property name"])
      if record["stereotype"] == "missing data": #The record is a property
        filename = str(record['class name'])+".html#"+str(record['property name'])
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        url = directory+filename
        text = str(record["property name"])
        print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_dc_name.insert(1,new_link)
        tr.insert(2,td_dc_name)
      else: #The record is a class
        td_dc_name.string = "-"
        tr.insert(2,td_dc_name)

      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(3,td_def)
      
      if record["type"] != "missing data":
        td_def = soup.new_tag("td")
        td_def.string = str(record["type"])
        tr.insert(4,td_def)
      else:
        td_def = soup.new_tag("td")
        td_def.string = "-"
        tr.insert(4,td_def)   
      return tr
  else:
    return None

def create_index_row_logical_model_with_supplements(record, directory):
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  tr = soup.new_tag("tr")
  td_supplement = soup.new_tag("td")

  if "European Supplement" in record["supplement"]:
    span_supplement = soup.new_tag("spam")
    span_supplement['class'] = "badge badge-secondary"
    span_supplement.string = "European Supplement"
    td_supplement.insert(1,span_supplement)
  tr.insert(1,td_supplement)

  td_ic_name = soup.new_tag("td")
  td_ic_name["data-order"] = record["class name"]
  if record["stereotype"] != "missing data": #The record is a class
    filename = classname_to_filename(str(record['class name']))
    url = directory+filename
    text = record["class name"]
    print(text)
    new_link = soup.new_tag("a")
    new_link['href'] = url
    new_link['target'] = "_blank"
    new_link.string = text
    td_ic_name.insert(1,new_link)
    tr.insert(2,td_ic_name)
  else: #The record is a property
    td_ic_name.string = record["class name"]
    tr.insert(2,td_ic_name)
  
  td_dc_name = soup.new_tag("td")
  td_dc_name["data-order"] = str(record["property name"])
  if record["stereotype"] == "missing data": #The record is a property
    filename = str(record['class name'])+".html#"+str(record['property name'])
    filename = filename.replace("/", "-")
    filename = filename.replace("*", "-")
    filename = filename.replace(" ", "")
    filename = filename.replace("\t", "")
    filename = filename.replace("\n", "")
    url = directory+filename
    text = str(record["property name"])
    print(text)
    new_link = soup.new_tag("a")
    new_link['href'] = url
    new_link['target'] = "_blank"
    new_link.string = text
    td_dc_name.insert(1,new_link)
    tr.insert(3,td_dc_name)
  else: #The record is a class
    td_dc_name.string = "-"
    tr.insert(3,td_dc_name)

  if record["definition"] != "":
    td_def = soup.new_tag("td")
    td_def.string = str(record["definition"])
    tr.insert(4,td_def)
  
  if record["type"] != "missing data":
    td_def = soup.new_tag("td")
    td_def.string = str(record["type"])
    tr.insert(5,td_def)
  else:
    td_def = soup.new_tag("td")
    td_def.string = "-"
    tr.insert(5,td_def)
  
  return tr
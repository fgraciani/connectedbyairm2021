def create_mapping_index_page (mapping_file_pathname, template):
  """Create an index html page for a mapping. e.g. http://airm.aero/developers/fixm-4.2.0-to-airm-1.0.0.html

  Keyword arguments:
    mapping_file_pathname -- string defining the location and name of the mapping e.g. data/xlsx/mapping FIXM 4.2.0.xlsx
    template -- string defining the location and name of the html template e.g. data/html/templates/concept-list-template.html
  """

  import mapping
  mapping = mapping.Mapping(mapping_file_pathname)
  mapping_metadata = mapping.metadata
  mapping_dict = mapping.dictionary

  import utils
  utils.create_directory("docs/airm/developers/" + mapping_metadata["url_name"])
  soup = utils.create_html_soup(template)
   
  soup.title.string = mapping_metadata["name"] + " | Semantic Correspondences | AIRM.aero"
  soup.find(text="MAPPING_NAME_BC").replace_with(mapping_metadata["name"])
  soup.find(text="MAPPING_NAME_H2").replace_with(mapping_metadata["name"])

  for record in mapping_dict:
    new_table_row = create_index_table_row(record, mapping_metadata)
    soup.find('tbody').insert(1,new_table_row)

  f = open("docs/airm/developers/" + mapping_metadata["url_name"] + ".html","w+")
  f.write(soup.prettify())
  f.close()

def create_mapping_item_pages (mapping_file_pathname, template):
  """Create an html page for each information concept in a mapping. e.g. http://airm.aero/developers/fixm-4.2.0-to-airm-1.0.0/AerodromeSurfaceWind.html

  Keyword arguments:
    mapping_file_pathname -- string defining the location and name of the mapping e.g. data/xlsx/mapping FIXM 4.2.0.xlsx
    template -- string defining the location and name of the html template e.g. data/html/templates/concept-list-template.html
  """
  import mapping
  mapping = mapping.Mapping(mapping_file_pathname)
  mapping_metadata = mapping.metadata

  information_concepts = mapping.get_information_concepts()
  
  for info_concept in information_concepts:
    print(info_concept["Information Concept"])
    import utils
    soup = utils.create_html_soup(template)

    soup.title.string = str(info_concept['Information Concept']) + " - " + mapping_metadata["name"] + " | AIRM.aero"
    soup.find(text="MAPPING_NAME_BC").replace_with(str(mapping_metadata["name"])) 
    soup.find(id="MAPPING_NAME_BC")["href"]="../"+mapping_metadata["url_name"] + ".html"
    soup.find(text="INFO_CONCEPT_NAME_BC").replace_with(str(info_concept['Information Concept']))
    h2 = soup.new_tag("h2")
    h2.string = str(info_concept['Information Concept'])
    soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
    
    code = soup.new_tag("code")
    code.string = info_concept['Concept Identifier']
    code["class"] = "text-secondary"
    soup.find(id="INFO_CONCEPT_NAME").insert(1,code)

    soup.find(text="INFO_CONCEPT_DEFINITION").replace_with(str(info_concept['Concept Definition']))
    
    data_concepts = mapping.get_data_concepts(info_concept['Information Concept'])
    insert_position=0
    for data_concept in data_concepts:
      if data_concept["Data Concept"] != 'missing data':
        new_table_row = create_properties_table_row(data_concept)
        soup.find(id="DATA_CONCEPTS_LIST").insert(insert_position,new_table_row)
      insert_position += 1
    
    insert_position=0
    soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_position,soup.new_tag("hr"))
    insert_position += 1
    h3 = soup.new_tag("h3")
    h3["style"]="text-align:center; color:grey; margin-top: 50px; margin-bottom: 20px;"
    h3.string = "Details"
    soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_position,h3)
    insert_position += 1

    new_div = create_class_detail_div(info_concept)
    soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_position,new_div)
    insert_position += 1
    
    soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_position,new_div)
    for data_concept in data_concepts:
      if data_concept["Data Concept"] != 'missing data':
        new_div = create_property_detail_div(data_concept)
        soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_position,new_div)
      insert_position += 1

    f= open("docs/airm/developers/" + mapping_metadata["url_name"]+ "/" + info_concept["Information Concept"] + ".html","w+")
    f.write(soup.prettify())
    f.close()

def create_properties_table_row(data_concept):
  """Return an html table row for a data concept.

  Keyword arguments:
    data_concept -- A dictionary containing the data concept.
  """
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  new_tr = soup.new_tag("tr")

  td_dc_name = soup.new_tag("td")
  new_link = soup.new_tag("a")
  new_link['href'] = "#"+data_concept["Data Concept"]
  new_link.string = data_concept["Data Concept"]
  td_dc_name.insert(1,new_link)
  new_tr.insert(1,td_dc_name)
  
  td_def = soup.new_tag("td")
  if data_concept["Concept Definition"] != "missing data":
    td_def.string = str(data_concept["Concept Definition"])
  else:
    td_def.string = '-'
  new_tr.insert(2,td_def)
  
  td_type = soup.new_tag("td")
  if data_concept["Data Concept Type"] != "missing data":
    if data_concept["Data Concept Type"] != "enum value":
      new_link = soup.new_tag("a")
      new_link['href'] = str(data_concept["Data Concept Type"])+".html"
      new_link['target'] = "_blank"
      new_link.string = str(data_concept["Data Concept Type"])
      td_type.insert(1,new_link)
    else:
      td_type.string = str(data_concept["Data Concept Type"])
  else:
    td_type.string = '-'
  new_tr.insert(3,td_type)
  
  return new_tr

def create_class_detail_div(info_concept):
  """Return an html div for a mapping information concept.

  Keyword arguments:
    info_concept -- A dictionary containing the info concept.
  """
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  class_div = soup.new_tag("div")
  class_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"

  h4 = soup.new_tag("h4")
  h4.string = str(info_concept["Information Concept"])
  h4["id"] = str(info_concept["Information Concept"])
  h4["style"] = "padding-top: 120px; margin-top: -120px;"
  class_div.insert(0,h4)

  code = soup.new_tag("code")
  identifier = info_concept["Information Concept"]
  code.string = identifier
  code["class"] = "text-secondary"
  class_div.insert(1,code)

  p = soup.new_tag("p")
  definition = str(info_concept["Concept Definition"])
  definition = definition.replace("Definition: ","")
  p.string = definition
  br = soup.new_tag("br")
  p.insert(2,br)
  class_div.insert(2,p)

  if info_concept["AIRM Concept Identifier"] != "missing data":
    sc_h5 = soup.new_tag("h5")
    sc_h5.string = "Semantic Correspondence"
    sc_h5['style'] = "margin-top: 40px;"
    class_div.insert(3,sc_h5)

    sc_div = soup.new_tag("div")
    sc_div["class"] = "table-responsive"
    sc_div.insert(1,create_semantic_correspondence_table(info_concept))
    class_div.insert(4,sc_div)

  if str(info_concept["Rationale"]) != "missing data":
    h5 = soup.new_tag("h5")
    h5.string = "Rationale"
    class_div.insert(5,h5)

    p = soup.new_tag("p")
    p.string = str(info_concept["Rationale"])
    #print('Rationale:'+str(info_concept["Rationale"]))
    class_div.insert(6,p)

  if str(info_concept["Notes"]) != "missing data":
    notes_h5 = soup.new_tag("h5")
    notes_h5.string = "Notes"
    class_div.insert(7,notes_h5)

    p = soup.new_tag("p")
    p.string = str(info_concept["Notes"])
    #print('Notes:'+str(data_concept["Notes"]))
    class_div.insert(8,p)

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
  class_div.insert(9,top_link_p)

  return class_div

def create_property_detail_div(data_concept):
  """Return an html div for a mapping data concept.

  Keyword arguments:
    data_concept -- A dictionary containing the data concept.
  """
  #merge with create_class_detail_div
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  property_div = soup.new_tag("div")
  property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"
                  
  h4 = soup.new_tag("h4")
  h4.string = str(data_concept["Data Concept"])
  h4["id"] = str(data_concept["Data Concept"])
  h4["style"] = "padding-top: 120px; margin-top: -120px;"
  property_div.insert(0,h4)

  code = soup.new_tag("code")
  identifier = data_concept['Concept Identifier']
  code.string = identifier
  code["class"] = "text-secondary"
  property_div.insert(1,code)

  p = soup.new_tag("p")
  definition = str(data_concept["Concept Definition"])
  definition = definition.replace("Definition: ","")
  p.string = definition
  br = soup.new_tag("br")
  p.insert(2,br)
  property_div.insert(2,p)

  sc_h5 = soup.new_tag("h5")
  sc_h5.string = "Semantic Correspondence"
  sc_h5['style'] = "margin-top: 40px;"
  property_div.insert(3,sc_h5)

  sc_div = soup.new_tag("div")
  sc_div["class"] = "table-responsive"
  sc_div.insert(1,create_semantic_correspondence_table(data_concept))
  property_div.insert(4,sc_div)

  if str(data_concept["Rationale"]) != "missing data":
    h5 = soup.new_tag("h5")
    h5.string = "Rationale"
    property_div.insert(5,h5)

    p = soup.new_tag("p")
    p.string = str(data_concept["Rationale"])
    #print('Rationale:'+str(data_concept["Rationale"]))
    property_div.insert(6,p)

  if str(data_concept["Notes"]) != "missing data":
    notes_h5 = soup.new_tag("h5")
    notes_h5.string = "Notes"
    property_div.insert(7,notes_h5)

    p = soup.new_tag("p")
    p.string = str(data_concept["Notes"])
    #print('Notes:'+str(data_concept["Notes"]))
    property_div.insert(8,p)

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
  property_div.insert(9,top_link_p)

  return property_div

def create_semantic_correspondence_table(data_concept):
  """Return an html table containing the semantic correspondence for a data concept.

  Keyword arguments:
    data_concept -- A dictionary containing the data concept.
  """
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  sc_table = soup.new_tag("table")
  sc_table["class"] = "table"
  sc_thead = soup.new_tag("thead")
  tr = soup.new_tag("tr")
  th = soup.new_tag("th")
  th.string = "AIRM Concept"
  tr.insert(1,th)
  th = soup.new_tag("th")
  th.string = "Definition"
  tr.insert(2,th)
  sc_thead.insert(1,tr)
  sc_table.insert(1,sc_thead)
  tbody = soup.new_tag("tbody")
  insert_position=0
  if str(data_concept['AIRM Concept Identifier']) != "missing data":
    import airm
    airm = airm.Airm()
    urns = str(data_concept['AIRM Concept Identifier']).split('\n')
    for urn in urns:
      airm_concept = airm.get_concept(urn)
      if airm_concept != None:
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag("a")
        a['href'] = relativise_url(airm_concept['url'])
        a['target'] = "_blank"
        a.string = airm_concept['name']
        td.insert(1,a)
        tr.insert(1,td)
        td = soup.new_tag("td")
        td.string = airm_concept['definition']
        tr.insert(2,td)
        tbody.insert(insert_position,tr)
        insert_position+=1
  if str(data_concept['Additional Traces']) != "missing data":
    import airm
    airm = airm.Airm()
    urns = str(data_concept['Additional Traces']).split('\n')
    for urn in urns:
      airm_concept = airm.get_concept(urn)
      if airm_concept != None:
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        spam = soup.new_tag("spam")
        spam["class"] = "badge badge-secondary"
        spam["data-toggle"] = "tooltip" 
        spam["data-placement"] = "bottom" 
        spam["title"] = "Additional traces to clarify the mapping of narrower concepts"
        spam.string ="Additional trace"
        td.insert(1,spam)
        a = soup.new_tag("a")
        a['href'] = relativise_url(airm_concept['url'])
        a['target'] = "_blank"
        a.string = airm_concept['name']
        td.insert(2,a)
        tr.insert(1,td)
        td = soup.new_tag("td")
        td.string = airm_concept['definition']
        tr.insert(2,td)
        tbody.insert(insert_position,tr)
        insert_position+=1
  if str(data_concept['Special cases \n(CR, OutOfScope, Not Established)']) != "missing data":
    import airm
    airm = airm.Airm()
    parts = str(data_concept['Special cases \n(CR, OutOfScope, Not Established)']).split('\n')
    for case in parts:
      airm_concept = airm.get_concept(case)
      if airm_concept != None:
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag("a")
        a['href'] = relativise_url(airm_concept['url'])
        a['target'] = "_blank"
        a.string = airm_concept['name']
        td.insert(1,a)
        tr.insert(1,td)
        td = soup.new_tag("td")
        td.string = airm_concept['definition']
        tr.insert(2,td)
        tbody.insert(insert_position,tr)
        insert_position+=1
  sc_table.insert(2,tbody)

  return sc_table

def create_index_table_row(mapping_entry, mapping_metadata):
  """Return an html table row for a mapping entry (information or data concept).

  Keyword arguments:
    mapping_entry -- A dictionary containing the mapping entry.
    mapping_metadata -- A dictionary containing the mapping metadata.
  """
  from bs4 import BeautifulSoup
  soup = BeautifulSoup("<b></b>", 'lxml')
  new_tr = soup.new_tag("tr")

  td_ic_name = soup.new_tag("td")
  if mapping_entry["Data Concept"] != "missing data":
    td_ic_name.string = str(mapping_entry["Information Concept"])
  else:
    text = mapping_entry["Information Concept"]
    new_link = soup.new_tag("a")
    new_link['href'] = mapping_metadata["url_name"] + "/" + mapping_entry["Information Concept"] + ".html"
    new_link['target'] = "_blank"
    new_link.string = text
    td_ic_name.insert(1,new_link)
  td_ic_name["data-order"] = mapping_entry["Information Concept"]
  new_tr.insert(1,td_ic_name)

  td_dc_name = soup.new_tag("td")
  if mapping_entry["Data Concept"] != "missing data":
    text = str(mapping_entry["Data Concept"])
    new_link = soup.new_tag("a")
    print(str(mapping_entry["Information Concept"])+"."+str(mapping_entry["Data Concept"]))
    new_link['href'] = mapping_metadata["url_name"] + "/" + mapping_entry["Information Concept"] + ".html" + "#" + str(mapping_entry["Data Concept"])
    new_link['target'] = "_blank"
    new_link.string = text
    td_dc_name.insert(1,new_link)
    td_dc_name["data-order"] = mapping_entry["Data Concept"]
  else:
    td_dc_name = soup.new_tag("td")
    td_dc_name.string = '-'
    td_dc_name["data-order"] = "-"
  new_tr.insert(2,td_dc_name)

  if mapping_entry["Concept Definition"] != "missing data":
    td_def = soup.new_tag("td")
    td_def.string = str(mapping_entry["Concept Definition"])
    new_tr.insert(3,td_def)
  else:
    td_def = soup.new_tag("td")
    td_def.string = '-'
    new_tr.insert(3,td_def)

  if mapping_entry["Data Concept Type"] != "missing data":
    td_dc_type = soup.new_tag("td")
    parts = str(mapping_entry["Data Concept Type"]).split(":")
    clean_type = parts[-1]
    td_dc_type.string = clean_type
    new_tr.insert(4,td_dc_type)
  else:
    td_dc_type = soup.new_tag("td")
    td_dc_type.string = '-'
    new_tr.insert(4,td_dc_type)

  return new_tr

def relativise_url(url):
  """"Return a relative url from an absolute url."""
  relative_url = url.replace("http://airm.aero/","../../")
  return relative_url
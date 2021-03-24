def calculate_url_for_airm_urn(urn):#old name: create_url
  """Return a URL te be used as a hyperlink when displaying a given URN.

  Keyword arguments:
    urn -- the URN string to be processed
  """
  #TO-DO support supplements
  #TO-DO support other than logical model
  #TO-DO support multiple versions of the AIRM
  #TO-DO improve URL options for non-urn cases

  url=""
  if isinstance(urn, str):
    if urn.startswith("changeRequest"):
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-014+Forms+of+semantic+correspondence"
    elif urn=="outOfScope":
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-015+Out-of-scope+or+no+correspondence"
    elif urn.startswith("noSemanticCorrespondence"):
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-015+Out-of-scope+or+no+correspondence"
    elif urn.startswith("urn"):
      components = urn.split(":")
      last_component = components[-1]
      components = last_component.split("@")
      entity = components[0]
      prop = ""
      if len(components) == 2:
        prop = components[1]
      url="../../viewer/1.0.0/logical-model/"+entity+"#"+prop
  return url

def calculate_name_for_airm_urn(urn):
  """Return a name to be displayed for a given URN.
  If the URN is valid, the display name follows the Class#property syntax.

  Keyword arguments:
    urn -- the URN string to be processed
  """
  name = "Unknown URN: " + str(urn)
  if isinstance(urn, str):
    if urn.startswith("changeRequest"):
      name="AIRM Change Request"
    elif urn=="outOfScope":
      name="Out of Scope"
    elif urn.startswith("noSemanticCorrespondence"):
      name="No Semantic Correspondence"
    elif urn.startswith("urn"):
      components = urn.split(":")
      last_component = components[-1]
      name = last_component  
  return name

def create_directory(path):
  """Create a directory with path/name provided by path.

  Keyword arguments:
    path -- string defining the location and name of the new directory
  """
  import os
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)

def create_html_soup(template):
  """Create a soup variable from a html template.

  Keyword arguments:
    template -- string defining the location and name of the template e.g. data/html/templates/concept-list-template.html
  """
  from bs4 import BeautifulSoup
  html = open(template).read()
  soup = BeautifulSoup(html, "lxml")
  return soup
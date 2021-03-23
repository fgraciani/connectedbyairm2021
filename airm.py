import pandas as pd

class Airm:
  contextual_abbreviations = pd.read_excel (r'xlsx/airm/cx_abbr.xlsx', sheet_name='cx_abbr')
  contextual_terms = pd.read_excel (r'xlsx/airm/cx_terms.xlsx', sheet_name='cx_terms')
  conceptual_concepts = pd.read_excel (r'xlsx/airm/cp_core.xlsx', sheet_name='test')
  conceptual_supp_concepts = pd.read_excel (r'xlsx/airm/cp_supp.xlsx', sheet_name='test')
  logical_concepts = pd.read_excel (r'xlsx/airm/logical_core.xlsx', sheet_name='test')
  logical_supp_concepts = pd.read_excel (r'xlsx/airm/logical_supp.xlsx', sheet_name='test')
  
  #df_connected_index = pd.read_excel (r'data/xlsx/connected_index.xlsx', sheet_name='connceted_index')

  not_found_counter = 0
  
  def __init__(self):
    self.contextual_abbreviations.fillna("missing data", inplace = True)
    self.contextual_terms.fillna("missing data", inplace = True)
    self.conceptual_concepts.fillna("missing data", inplace = True)
    self.logical_concepts.fillna("missing data", inplace = True)
    self.logical_supp_concepts.fillna("missing data", inplace = True)
    
    #self.df_connected_index.fillna("missing data", inplace = True)
    
    self.contextual_abbreviations.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    self.contextual_terms.columns =         ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    
    self.conceptual_concepts.columns =         ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]
    self.conceptual_supp_concepts.columns =    ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]

    self.logical_concepts.columns =         ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]
    self.logical_supp_concepts.columns =    ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]

  def get_concept(self, urn):
    urn = urn.replace(' ','')
    if urn == "":
      print("! empty urn")
    if "urn:" in urn:#if valid_urn(urn):
      if "ContextualModel" in urn:
        dataframe = self.contextual_terms.copy()
      elif "ConceptualModel" in urn:
        if "ses:eurocontrol" in urn:
          dataframe = self.conceptual_supp_concepts.copy()
        else:
          dataframe = self.conceptual_concepts.copy()
      elif "LogicalModel" in urn:
        if "ses:eurocontrol" in urn:
          dataframe = self.logical_supp_concepts.copy()
        else:
          dataframe = self.logical_concepts.copy()

      #Search block:
      filter = dataframe["urn"]==urn
      dataframe.sort_values("urn", inplace = True)
      dataframe.where(filter, inplace = True) 
      results = dataframe.dropna(how='all')  

      if results.empty:
        print("! URN not found in AIRM: "+urn)
        concept = {
          "name" : "Not found",
          "definition" : "The provided URN does not exist.",
          "url"  : "http://airm.aero/viewer/not-found"
        }
      else: 
        if '@' in urn:
          name = results["class name"].iloc[0]+'.'+results["property name"].iloc[0]
        else:
          name = results["class name"].iloc[0]
        concept = {
          "name" : name,
          "definition" : results["definition"].iloc[0],
          "url"  : urn_to_url(urn)
        }
    elif urn == "outOfScope":
      concept = {
        "name" : "Out of scope",
        "definition" : "This concept is considered as out of the scope of the AIRM.",
        "url"  : "http://airm.aero/developers/airm-out-of-scope.html"
      }
    elif urn == "changeRequest":
      concept = {
        "name" : "Change request",
        "definition" : "A change request is required on the AIRM.",
        "url"  : "http://airm.aero/developers/airm-change-request.html"
      }
    elif urn.lower() == "notestablished":
      concept = {
        "name" : "Not Established",
        "definition" : "Semantic correspondence has not been established for this concept.",
        "url"  : "http://airm.aero/developers/airm-change-request.html"
      }
    else:
      print("! URN not valid: "+urn)
      concept = {
        "name" : "Not found",
        "definition" : "The provided URN does not exist.",
        "url"  : "http://airm.aero/viewer/not-found"
      }
    return concept

def urn_to_url(urn):
  if "urn:" in urn:
    urn_parts = urn.split(':')
    if ":ses:" in urn:
      supplement = "european-supplement/"
    else:
      supplement = ''

    if "ContextualModel" in urn:
      model = "contextual-model"
    elif "ConceptualModel" in urn:
      model = "conceptual-model"
    elif "LogicalModel" in urn:
      model = "logical-model"
    else:
      model = "unknown"
    
    if "@" in urn:
      subparts = urn_parts[-1].split('@')
      page = subparts[-2]+".html"
      target = '#'+subparts[-1]
    else:  
      page = urn_parts[-1]
      target = ''
      
    return "http://airm.aero/viewer/1.0.0/"+model+'/'+supplement+page+target
  else: 
    return "http://airm.aero/viewer/not-found"
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
    urn = urn.replace(' ','').replace('\t','').replace('	','')
    if urn == "":
      return None
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
      else:
        print("! URN not found in AIRM: " + urn)
        return {
          "name" : "Not found: "+urn,
          "definition" : "The provided URN does not exist.",
          "url"  : "http://airm.aero/viewer/not-found"
        }
        
      #Search block:
      filter = dataframe["urn"]==urn
      dataframe.sort_values("urn", inplace = True)
      dataframe.where(filter, inplace = True) 
      results = dataframe.dropna(how='all')  
      results = results.applymap(str)

      if results.empty:
        print("! URN not found in AIRM: "+urn)
        concept = {
          "name" : "Not found: "+urn,
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
    elif urn == "noSemanticCorrespondence":
      concept = {
        "name" : "Not Established",
        "definition" : "Semantic correspondence has not been established for this concept.",
        "url"  : "http://airm.aero/developers/airm-change-request.html"
      }
    else:
      print("! URN not valid: "+urn)
      concept = {
        "name" : "Invalid URN: "+urn,
        "definition" : "The URN does not respect the URN syntax.",
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


def create_connected_index():
  df_connected_index_cols = ["airm_urn", "model_name", "concept_name", "concept_id", "concept_type"]
  df_connected_index_rows = []

  import fixm
  fixm = fixm.Fixm()
  fixm_mapping_dict = fixm.fixm_mapping_dataframe.to_dict('records')

  for entry in fixm_mapping_dict:
    sem_correspondences = str(entry['Semantic Correspondence']).split('\n')
    for line in sem_correspondences:
      urn = line
      df_connected_index_rows.append({"airm_urn": urn, "model_name": "FIXM 4.2.0", "concept_name": entry["Data Concept"], "concept_id": entry["Identifier"], "concept_type": entry["Type"]})
  
  import amxm
  amxm = amxm.Amxm()
  amxm_mapping_dict = amxm.amxm_mapping_dataframe.to_dict('records')

  for entry in amxm_mapping_dict:
    sem_correspondences = str(entry['AIRM Concept Identifier']).split('\n')
    for line in sem_correspondences:
      urn = line
      if str(entry["Data Concept"]) == "missing data":
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "AMXM 2.0.0", "concept_name": entry["Information Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})
      else:
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "AMXM 2.0.0", "concept_name": entry["Data Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})

  amxm_mapping_dict = amxm.amxm_mapping_enum_dataframe.to_dict('records')

  for entry in amxm_mapping_dict:
    sem_correspondences = str(entry['AIRM Concept Identifier']).split('\n')
    for line in sem_correspondences:
      urn = line
      if str(entry["Data Concept"]) == "missing data":
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "AMXM 2.0.0", "concept_name": entry["Information Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})
      else:
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "AMXM 2.0.0", "concept_name": entry["Data Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})

  import aixm
  aixm = aixm.Aixm()
  aixm_mapping_merged_dict = aixm.aixm_mapping_merged_dataframe.to_dict('records')

  for entry in aixm_mapping_merged_dict:
    sem_correspondences = str(entry['AIRM Concept Identifier']).split('\n')
    for line in sem_correspondences:
      urn = line
      if str(entry["Data Concept"]) == "missing data":
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "AIXM 5.1.1", "concept_name": entry["Information Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})
      else:
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "AIXM 5.1.1", "concept_name": entry["Data Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})

  import aixm_adr
  aixm_adr = aixm_adr.Aixm_adr()
  aixm_adr_mapping_dict = aixm_adr.aixm_adr_mapping_dataframe.to_dict('records')

  for entry in aixm_adr_mapping_dict:
    sem_correspondences = str(entry['AIRM Concept Identifier']).split('\n')
    for line in sem_correspondences:
      urn = line
      if str(entry["Data Concept"]) == "missing data":
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "ADR 23.5.0 Extension (AIXM 5.1.1)", "concept_name": entry["Information Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})
      else:
        df_connected_index_rows.append({"airm_urn": urn, "model_name": "ADR 23.5.0 Extension (AIXM 5.1.1)", "concept_name": entry["Data Concept"], "concept_id": entry["Concept Identifier"], "concept_type": entry["Basic Type"]})
  
  df_connected_index_out = pd.DataFrame(df_connected_index_rows, columns = df_connected_index_cols) 
  with pd.ExcelWriter('data/xlsx/'+'connected_index.xlsx', engine='xlsxwriter') as writer:  
      df_connected_index_out.to_excel(writer, sheet_name='connceted_index')
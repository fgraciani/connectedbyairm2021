import pandas as pd

class Airm:
  contextual_abbreviations = pd.read_excel (r'xlsx/airm/cx_abbr.xlsx', sheet_name='cx_abbr')
  contextual_terms = pd.read_excel (r'xlsx/airm/cx_terms.xlsx', sheet_name='cx_terms')
  conceptual_concepts = pd.read_excel (r'xlsx/airm/cp_core.xlsx', sheet_name='test')
  conceptual_supp_concepts = pd.read_excel (r'xlsx/airm/cp_supp.xlsx', sheet_name='test')
  logical_concepts = pd.read_excel (r'xlsx/airm/logical_core.xlsx', sheet_name='test')
  logical_supp_concepts = pd.read_excel (r'xlsx/airm/logical_supp.xlsx', sheet_name='test')
  df_connected_index = pd.read_excel (r'xlsx/connected_index.xlsx', sheet_name='connected_index')

  not_found_counter = 0
  
  def __init__(self):
    self.contextual_abbreviations.fillna("missing data", inplace = True)
    self.contextual_terms.fillna("missing data", inplace = True)
    self.conceptual_concepts.fillna("missing data", inplace = True)
    self.conceptual_supp_concepts.fillna("missing data", inplace = True)
    self.logical_concepts.fillna("missing data", inplace = True)
    self.logical_supp_concepts.fillna("missing data", inplace = True)
    self.df_connected_index.fillna("missing data", inplace = True)
    
    self.contextual_abbreviations.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    self.contextual_terms.columns =         ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    
    self.conceptual_concepts.columns =         ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]
    self.conceptual_supp_concepts.columns =    ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]

    self.logical_concepts.columns =         ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]
    self.logical_supp_concepts.columns =    ["supplement","stereotype","class name","property name", "type","type urn", "definition", "synonyms", "abbreviation", "urn",  "parent", "parent urn", "source"]

  def get_connections_by_urn(self,urn):
    connections_df = self.df_connected_index.copy()
    
    filter = connections_df["airm_urn"]==urn
    connections_df.sort_values("airm_urn", inplace = True)
    connections_df.where(filter, inplace = True) 
    df_results = connections_df.dropna(how='all')      

    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict

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

  def get_concept_properties_by_parent(self, parent, scope):
    if scope == "european-supplement/":
      concepts_df = self.conceptual_supp_concepts.copy()
      scope_filter = "\tEuropean Supplement"
    elif scope == "":
      concepts_df = self.conceptual_concepts.copy()
      scope_filter = "\t"
    
    filter = concepts_df["class name"]==parent
    concepts_df.sort_values("class name", inplace = True)
    concepts_df.where(filter, inplace = True) 
    df_results01 = concepts_df.copy()    
    
    df_results01.fillna("missing data", inplace = True)
    filter = df_results01["stereotype"]=="missing data"
    df_results01.sort_values("stereotype", inplace = True)
    df_results01.where(filter, inplace = True)
    df_results02 = df_results01.copy()

    filter = df_results02["supplement"]==scope_filter
    df_results02.sort_values("supplement", inplace = True)
    df_results02.where(filter, inplace = True) 
    df_results03 = df_results02.dropna(how='all') 

    if df_results03.empty:
      return None
    else:
      results_dict = df_results03.to_dict('records')
      return results_dict

  def get_logical_properties_by_class(self, class_name, scope):
    if scope == "european-supplement/":
      logical_df = self.logical_supp_concepts.copy()
    elif scope == "":
      logical_df = self.logical_concepts.copy()

    filtered_df = logical_df[(logical_df['class name'] == class_name) & (logical_df['stereotype'] == 'missing data')]
    print("-attributes: "+str(len(filtered_df.index)))

    if filtered_df.empty:
      return None
    else:
      return filtered_df.to_dict('records')

  def get_children_for_logical_model_class(self, urn, scope):
    if scope == "european-supplement/":
      logical_df = self.logical_supp_concepts.copy()
    elif scope == "":
      logical_df = self.logical_concepts.copy()

    filtered_df = logical_df[(logical_df['parent urn'] == urn)]
    if filtered_df.empty:
      return None
    else:
      return filtered_df.to_dict('records')

  def get_supplements_for_logical_model_class(self, urn):
    logical_df = self.logical_supp_concepts.copy()

    filtered_df = logical_df[(logical_df['parent urn'] == urn)]
    if filtered_df.empty:
      return None
    else:
      return filtered_df.to_dict('records')

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
  df_connected_index_cols = ["airm_urn", "model_name", "model_path", "concept_name", "concept_target"]
  df_connected_index_rows = []

  df_connected_index_rows = add_mapping_to_connected_index(df_connected_index_rows, "xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report.xlsx")
  df_connected_index_rows = add_mapping_to_connected_index(df_connected_index_rows, "xlsx/AMXM_2.0.0_Semantic_Correspondence_Report.xlsx")
  df_connected_index_rows = add_mapping_to_connected_index(df_connected_index_rows, "xlsx/ADR_23.5.0_Semantic_Correspondence_Report.xlsx")
  df_connected_index_rows = add_mapping_to_connected_index(df_connected_index_rows, "xlsx/AIXM_5.1.1_Semantic_Correspondence_Report.xlsx")
  df_connected_index_rows = add_mapping_to_connected_index(df_connected_index_rows, "xlsx/FIXM_4.2.0_Semantic_Correspondence_Report.xlsx")
  
  df_connected_index_out = pd.DataFrame(df_connected_index_rows, columns = df_connected_index_cols) 
  with pd.ExcelWriter('xlsx/'+'connected_index.xlsx', engine='xlsxwriter') as writer:  
      df_connected_index_out.to_excel(writer, sheet_name='connected_index')

def add_mapping_to_connected_index(connected_index, mapping_file_pathname):
  import mapping
  mapping = mapping.Mapping(mapping_file_pathname)
  mapping_dict = mapping.dataframe.to_dict('records')
  mapping_metadata = mapping.metadata
  model_name = str(mapping_metadata["name"]).replace(" to AIRM 1.0.0", "")
  path = mapping.metadata["url_name"]

  for entry in mapping_dict:
    sem_correspondences = str(entry['AIRM Concept Identifier']).split('\n')
    for line in sem_correspondences:
      urn = line
      if str(entry["Data Concept"]) == "missing data":
        concept = str(entry["Information Concept"])
        target = str(entry["Information Concept"])+".html"
      else:
        concept = str(entry["Data Concept"])
        target = str(entry["Information Concept"])+".html#"+str(entry["Data Concept"])
      
      connected_index.append({"airm_urn": urn, "model_name": model_name, "model_path": path ,"concept_name": concept, "concept_target": target})
  
  return connected_index
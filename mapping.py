import pandas as pd

class Mapping:
  metadata = {}
  dictionary = {}
  fixm_mapping_dataframe = pd.read_excel (r'data/xlsx/mapping FIXM 4.2.0.xlsx', sheet_name='semantic correspondences')
  fixm_definitions_dataframe = pd.read_excel (r'data/xlsx/FIXM classes.xlsx', sheet_name='FIXM Core 4.2.0')
  #classes = pd.Dataframe() #TO DO load in init
  #properties = pd.Dataframe() #TO DO load in init
     
  def __init__(self, mapping_file_pathname):
    self.fixm_mapping_dataframe.fillna("missing data", inplace = True)
    self.fixm_definitions_dataframe.fillna("missing data", inplace = True)
    #self.classes.fillna("missing data", inplace = True)
    #self.properties.fillna("missing data", inplace = True)
  
  def get_information_concepts():
    return None
    
  def create_dictionary():
    """
    import fixm
    fixm = fixm.Fixm()
    fixm_mapping_dict = fixm.fixm_mapping_dataframe.to_dict('records')
    """
    return None

  def create_metadata(mapping_file_pathname):
    """
    mapping_metadata["name"] = "FIXM 4.2.0 to AIRM 1.0.0"
    mapping_metadata["url_name"] = "fixm-4.2.0-to-airm-1.0.0"
    """
    metadata = {
      "name": "FIXM 4.2.0 to AIRM 1.0.0",
      "url_name": "fixm-4.2.0-to-airm-1.0.0"
    }
    return metadata
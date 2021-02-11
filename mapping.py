import pandas as pd

class Mapping:
  metadata = {
      "name": "ICAO WXXM 3.0.0 to AIRM 1.0.0",
      "url_name": "icao_wxxm_3.0.0_to_airm_1.0.0"
  }
  dictionary = None
  dataframe = None
     
  def __init__(self, mapping_file_pathname):
    self.dataframe = pd.read_excel(r''+mapping_file_pathname, sheet_name='semantic correspondences')
    self.dataframe.fillna("missing data", inplace = True)
    self.dictionary = dataframe.to_dict('records')
  
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
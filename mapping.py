import pandas as pd

class Mapping:
  metadata = {
      "name": "ICAO WXXM 3.0.0 to AIRM 1.0.0",
      "url_name": "icao_wxxm_3.0.0_to_airm_1.0.0"
  }
  dictionary = None
  dataframe = None
     
  def __init__(self, mapping_file_pathname):
    self.dataframe = pd.read_excel(r''+mapping_file_pathname, sheet_name='semantic correspondences', engine='openpyxl')
    self.dataframe.fillna("missing data", inplace = True)
    self.dictionary = self.dataframe.to_dict('records')
  
  def get_information_concepts(self):
    dataframe = self.dataframe.copy()
    #dataframe = dataframe.drop_duplicates(subset='Information Concept', keep="last")
    #TO DO Update list of tags dataframe = dataframe.drop(["Data Concept", "Definition", "Type", "Semantic Correspondence", "Additional Traces", "Rationale", "Notes"], axis=1)
    filter = dataframe["Data Concept"]=="missing data"
    dataframe.sort_values("Information Concept", inplace = True)
    dataframe.where(filter, inplace = True) 
    results = dataframe.dropna(how='all')      
    
    if dataframe.empty:
      return None
    else:
      return results.to_dict('records')

  def get_data_concepts(self, info_concept):
      dataframe = self.dataframe.copy()
      #dataframe = dataframe.drop_duplicates(subset='Information Concept', keep="last")
      #TO DO Update list of tags dataframe = dataframe.drop(["Data Concept", "Definition", "Type", "Semantic Correspondence", "Additional Traces", "Rationale", "Notes"], axis=1)
      filter = dataframe["Information Concept"] == info_concept
      dataframe.sort_values("Data Concept", inplace = True)
      dataframe.where(filter, inplace = True) 
      results = dataframe.dropna(how='all')      
      
      if dataframe.empty:
        return None
      else:
        return results.to_dict('records')
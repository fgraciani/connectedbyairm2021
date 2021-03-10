class Airm:
  def __init__(self):
        print("init")
  
  def get_concept(self, urn):
    concept = {
      "name" : "testName",
      "definition" : "testDefinition",
      "url"  : "http://airm.aero/viewer/1.0.0/logical-model/testURL"
    }
    return concept
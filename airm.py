class Airm:
  def __init__(self):
        print("init")
  
  def get_concept(self, urn):
    if urn == "outOfScope":
      concept = {
        "name" : "Out of scope",
        "definition" : "This concept is considered as out of the scope of the AIRM.",
        "url"  : "http://airm.aero/developers/airm-out-of-scope.html"
      }
    elif urn == "CR":
      concept = {
        "name" : "Change request",
        "definition" : "A change request is required on the AIRM.",
        "url"  : "http://airm.aero/developers/airm-change-request.html"
      }
    elif urn == "Not Established":
      concept = {
        "name" : "Not Established",
        "definition" : "Semantic correspondence has not been established for this concept.",
        "url"  : "http://airm.aero/developers/airm-change-request.html"
      }
    else: #TO-DO retrieve element from AIRM
      concept = {
        "name" : "testName",
        "definition" : "testDefinition",
        "url"  : "http://airm.aero/viewer/1.0.0/logical-model/testURL"
      }
    return concept
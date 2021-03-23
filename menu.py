def test(): #See https://github.com/Mckinsey666/bullet for improvements
  choice ='0'
  while choice =='0':
    print("Menu: ")
    print('')
    print("1: Test airm.urn_to_url(urn)")
    print('')
    print("2: Test airm.get_concept(urn)")
    print('')
    choice = input ("Please make a choice: ")
    print('')

    if choice == "1":
        print('\n')
        urn = input ("Paste a urn: ")
        import airm
        print(airm.urn_to_url(urn))
        test()    
    elif choice == "2":
        print('\n')
        urn = input ("Paste a urn: ")
        import airm
        airm = airm.Airm()
        print(airm.get_concept(urn))
        test()   

def main_menu():
  choice ='0'
  while choice =='0':
    print("Menu: ")
    print('')
    print("1: create_mapping_index_page icao_wxxm_3.0.0")
    print('')
    print("2: create_mapping_item_pages icao_wxxm_3.0.0")
    print('')
    choice = input ("Please make a choice: ")
    print('')

    if choice == "1":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report_v2.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        main_menu()    
    elif choice == "2":
        print('\n')
        import mapping2html
        mapping2html.dummy_create_mapping_item_pages("xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report_v2.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        main_menu()   
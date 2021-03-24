def test(): #See https://github.com/Mckinsey666/bullet for improvements
  """Print the testing menu and wait for a selection."""
  choice ='0'
  while choice =='0':
    print("Menu: ")
    print('')
    print("1: Test airm.urn_to_url(urn)")
    print('')
    print("2: Test airm.get_concept(urn)")
    print('')
    print("99: main menu")
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
    elif choice == "99":
        main_menu()   

def main_menu():
  """Print the main menu and wait for a selection."""
  choice ='0'
  while choice =='0':
    print('')
    print("Menu: ")
    print('')
    print("1: create_mapping_index_page icao_wxxm_3.0.0")
    print('')
    print("2: create_mapping_item_pages icao_wxxm_3.0.0")
    print('')
    print("3: create_mapping_index_page amxm_2.0.0")
    print('')
    print("4: create_mapping_item_pages amxm_2.0.0")
    print('')
    print("5: create_mapping_index_page aixm_5.1.1")
    print('')
    print("6: create_mapping_item_pages aixm_5.1.1")
    print('')
    print("7: create_mapping_index_page adr_23.5.0")
    print('')
    print("8: create_mapping_item_pages adr_23.5.0")
    print('')
    choice = input ("Please make a choice: ")
    print('')

    if choice == "1":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        main_menu()    
    elif choice == "2":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        main_menu()   
    elif choice == "3":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/AMXM_2.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        main_menu()    
    elif choice == "4":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/AMXM_2.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        main_menu()   
    elif choice == "5":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/AIXM_5.1.1_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        main_menu()    
    elif choice == "6":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/AIXM_5.1.1_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        main_menu()   
    elif choice == "7":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/ADR_23.5.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        main_menu()    
    elif choice == "8":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/ADR_23.5.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        main_menu()   
    elif choice == "9":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/FIXM_4.2.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        main_menu()    
    elif choice == "10":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/FIXM_4.2.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        main_menu()
    elif choice == "99":
        test()  
    
 
 
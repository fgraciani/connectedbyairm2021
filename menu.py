def main_menu(): 
  """Print the main menu and wait for a selection."""
  choice ='0'
  while choice =='0':
    print("Menu: ")
    print('')
    print("1: AIRM Viewer menu")
    print('')
    print("2: Semantic Correspondences menu")
    print('')
    print("99: Test menu")
    print('')
    choice = input ("Please make a choice: ")
    print('')

    if choice == "1":
        print('\n')
        viewer_menu()
        main_menu()    
    elif choice == "2":
        print('\n')
        semantic_correspondences_menu()
        main_menu()  
    elif choice == "99":
        test_menu()   

def viewer_menu(): 
  """Print the AIRM Viewer menu and wait for a selection."""
  choice ='0'
  while choice =='0':
    print('')
    print("AIRM Viewer menu: ")
    print('')
    print("1: create_contextual_model_abbreviations_index_page")
    print('')
    print("2: create_contextual_model_abbreviations_with_supplements_index_page")
    print('')
    print("3: create_contextual_model_abbreviations_item_pages")
    print('')
    print("4: create_contextual_model_terms_index_page")
    print('')
    print("5: create_contextual_model_terms_with_supplements_index_page")
    print('')
    print("6: create_contextual_model_terms_item_pages")
    print('')
    print("7: create_conceptual_model_index_page")
    print('')
    print("8: create_conceptual_model_with_supplements_index_page")
    print('')
    print("9: create_conceptual_model_item_pages")
    print('')
    print("10: create_logical_model_index_page")
    print('')
    print("11: create_logical_model_with_supplements_index_page")
    print('')
    print("12: create_connected_index")
    print('')
    print("13: create_logical_model_item_pages")
    print('')
    print("99: Back to main menu")
    print('')
    choice = input ("Please make a choice: ")
    print('')
    if choice == "1":
        print('\n')
        import airm2html
        airm2html.create_contextual_model_abbreviations_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "2":
        print('\n')
        import airm2html
        airm2html.create_contextual_model_abbreviations_with_supplements_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "3":
        print('\n')
        import airm2html
        airm2html.create_contextual_model_abbreviations_item_pages()
        print("Done.")
        viewer_menu()
    elif choice == "4":
        print('\n')
        import airm2html
        airm2html.create_contextual_model_terms_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "5":
        print('\n')
        import airm2html
        airm2html.create_contextual_model_terms_with_supplements_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "6":
        print('\n')
        import airm2html
        airm2html.create_contextual_model_terms_item_pages()
        print("Done.")
        viewer_menu()
    elif choice == "7":
        print('\n')
        import airm2html
        airm2html.create_conceptual_model_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "8":
        print('\n')
        import airm2html
        airm2html.create_conceptual_model_with_supplements_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "9":
        print('\n')
        import airm2html
        airm2html.create_conceptual_model_item_pages()
        print("Done.")
        viewer_menu()
    elif choice == "10":
        print('\n')
        import airm2html
        airm2html.create_logical_model_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "11":
        print('\n')
        import airm2html
        airm2html.create_logical_model_with_supplements_index_page()
        print("Done.")
        viewer_menu()
    elif choice == "13":
        print('\n')
        import airm2html
        airm2html.create_logical_model_item_pages()
        print("Done.")
        viewer_menu()
    elif choice == "12":
        print('\n')
        import airm
        airm.create_connected_index()
        print("Done.")
        viewer_menu()
    elif choice == "99":
        main_menu() 

    """
    create_logical_model_item_pages()"""

def semantic_correspondences_menu():
  """Print the Semantic Correspondences menu and wait for a selection."""
  choice ='0'
  while choice =='0':
    print('')
    print("Semantic Correspondences menu: ")
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
    print("9: create_mapping_index_page fixm_4.2.0")
    print('')
    print("10: create_mapping_item_pages fixm_4.2.0")
    print('')
    print("99: Back to main menu")
    print('')
    choice = input ("Please make a choice: ")
    print('')

    if choice == "1":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        semantic_correspondences_menu()    
    elif choice == "2":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/ICAO_WXXM_3.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        semantic_correspondences_menu()   
    elif choice == "3":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/AMXM_2.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        semantic_correspondences_menu()    
    elif choice == "4":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/AMXM_2.0.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        semantic_correspondences_menu()   
    elif choice == "5":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/AIXM_5.1.1_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        semantic_correspondences_menu()    
    elif choice == "6":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/AIXM_5.1.1_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        semantic_correspondences_menu()   
    elif choice == "7":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/ADR_23.5.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        semantic_correspondences_menu()    
    elif choice == "8":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/ADR_23.5.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        semantic_correspondences_menu()   
    elif choice == "9":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_index_page("xlsx/FIXM_4.2.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concept-list-template.html")
        print("Done.")
        semantic_correspondences_menu()    
    elif choice == "10":
        print('\n')
        import mapping2html
        mapping2html.create_mapping_item_pages("xlsx/FIXM_4.2.0_Semantic_Correspondence_Report.xlsx","docs/airm/templates/concepts/concept-template.html")
        print("Done.")
        semantic_correspondences_menu()
    elif choice == "99":
        main_menu()  
    
def test_menu():
  """Print the testing menu and wait for a selection."""
  choice ='0'
  while choice =='0':
    print("Testing menu: ")
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
        test_menu()    
    elif choice == "2":
        print('\n')
        urn = input ("Paste a urn: ")
        import airm
        airm = airm.Airm()
        print(airm.get_concept(urn))
        test_menu()  
    elif choice == "99":
        main_menu()  
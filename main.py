import mapping2html

mapping2html.create_mapping_index_page("xlsx/icao_wxxm_3.0.0_Semantic_Correspondence_Report_v1.xlsx","docs/airm/templates/concept-list-template.html")

mapping2html.dummy_create_mapping_item_pages("xlsx/icao_wxxm_3.0.0_Semantic_Correspondence_Report_v1.xlsx","docs/airm/templates/concepts/concept-template.html")

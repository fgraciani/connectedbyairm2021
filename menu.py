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
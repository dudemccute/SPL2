#regen.py
regen = True

if (regen == True):
    while(True):
        eingabe = input ("Hast du einen Regenschirm")
        if(eingabe == "nein"):
            while (regen):
                print("warten bis regen aufhört..")
                eingabe = input("Regnet es noch?")
                if (eingabe == "nein"):
                    regen = False
                    print("es hat aufgehört zu regnen")
                elif (eingabe == "ja"):
                    print("es regnet immer noch...")
                else:
                    print("bitte nur ja oder nein eingeben!!")
            print("Dann geh raus") 
            break
        elif (eingabe == "ja"):
            regen = False
            print("Dann geh raus") 
            break     
        else:
            print("Bitte nur ja oder nein!")
            

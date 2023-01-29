def question1():
    boucle1 = None
    while boucle1 == None:
        choix1_str = input("Fortinaiti ila babaji ? ")
        if choix1_str == ("babaji" or "Babaji"):
            print ("Question2")
            boucle1 = 1
        else:
            print ("purpl u nub")

def question2 ():
    boucle2 = None
    while boucle2 == None:
        choix2_str = input("Babaji ila ikis bokis siris ikis? ")
        if choix2_str == ("babaji" or "Babaji"):
            print ("question3")
            boucle2 = 1
        else:
            print ("nop")

def question3 ():
    boucle3 = None
    while boucle3 == None:
        choix3_str = input("Babaji ila balas steinsen faif? ")
        if choix3_str == ("balas steinsen faif"):
            print ("question4")
            boucle3 = 1
        else:
            print ("t une merde")

def question4 (): 
    boucle4 = None
    while boucle4 == None:
        choix4_str = input("Pain au chocolat ou chocolatine ")
        if choix4_str == ("croissant"):
            print ("question5")
            boucle4 = 1
        else:
            print ("connard")

def question5 ():
    boucle5 = None
    while boucle5 == None:
        choix5_str = input("Quelle est la 28ème décimal de pi? ")
        if choix5_str == ("pi"):
            print ("TU AS GAGNE LE DROIT DE RESPIRER !!!")
            boucle5 = 1
        else:
            print ("pfff amateur")


question1()
question2()
question3()
question4()
question5()
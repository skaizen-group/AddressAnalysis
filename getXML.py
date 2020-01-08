import spacy
import loadModel

nlp = loadModel.loadModel()

def getXML(file):
    

    
    tabLabel = ["Sexe","Prenom","Nom","Role","nomLieu","noRue","nomRue","CodePostal","Ville","Cedex","Type","Pays","complementRue","Identification","Service"]

    tabAdr = ['nomLieu','noRue','nomRue','CodePostal','Ville','Cedex','Pays','etage']
    tabAdrXML = ['BldgNm','BldgNb','StrtNm','PstCd','TwnNm','DstrctNm','Ctry','Flr']
    
    
    
    text = str(file[0],'utf-8').replace('\r','')
    
    doc = nlp( text )
    
    print('--------------------------------- \n')
    
    for entity in doc.ents:
        print(entity.label_, ' | ', entity.text)
        
        
    print('--------------------------------- \n\n')
        
    adresse = '<PostalAddress>\n'
    expediteur = '<Sender>\n'
    for entity in doc.ents:
       
        if( entity.label_ in  tabAdr ):
            index = tabAdr.index( entity.label_  )
            adresse += "	<"+tabAdrXML[index]+">"+entity.text + "</"+tabAdrXML[index]+">\n"
        else : 
            expediteur += "	<"+entity.label_+">"+entity.text + "</"+entity.label_+">\n" 
    
    adresse += '</PostalAddress>\n\n'
    expediteur += '</Sender>'
    
    chaine = adresse + expediteur
    
    return chaine
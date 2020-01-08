import spacy 
nlp = spacy.load("Modele/Modele_8Jan")
def preproc(doc):
    doc2 = ""
    bol = 1
    for i in doc:
        string = ' '.join(i.text.split())
        if string != '':
            if bol:
                bol = 0
            else:
                doc2 += ' '
            doc2 += (string)
    
    return nlp.make_doc(doc2)

def newLine(doc):
    doc2 = ""
    tabNL = []
    tabNomLieu = ["batiment","residence","immeuble","zone"]
    tabNL.extend(tabNomLieu)
    tabType = ['cp','bp','tsa']
    tabNL.extend(tabType)
    tabComplement = ['bureau','appartement','couloir','escalier',"entree"]
    tabNL.extend(tabComplement)
    tabCedex = ['cedex']
    tabNL.extend(tabCedex)
    
    for i in doc:
        if ( i.text[0].isdigit()):
            if( doc[i.i-1].text.lower() not in tabNL ):
                doc2 += "\n"
        if ( i.text.lower() in tabNL ) :

            doc2 += "\n"
        doc2 += i.text+' '
        
    tabSplit = doc2.split('\n')
    bol = 1 
    
    while ( bol == 1):
        bol = 0
        idx = -1
        
        for index, line in enumerate(tabSplit):
            firstWord = line.split(' ')[0].lower()
            if firstWord in tabComplement:
                idx = index
            if firstWord in tabNomLieu and idx != -1 :
                tmp = tabSplit[idx]
                tabSplit[idx] = line
                tabSplit[index] = tmp
         
                bol = 1

    doc2 = '\n'.join(tabSplit)
        
    return nlp.make_doc(doc2)

def loadModel():
    
    nlp.add_pipe(preproc, first=True)
    nlp.add_pipe(newLine, after='preproc')
    
    return nlp
    
    
    
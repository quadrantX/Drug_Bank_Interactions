'''
Extracting AE/Interactions from Twosides
Extracting AE from Offsides
'''


#Extracting AE/Interactions from Twosides
def get_ae_interaction(drug1, drug2):
    tpl_keys = tuple([drug1, drug2].sort())
    if tpl_keys in list(dct_DB_TS.keys()):
        return dct_DB_TS[tpl_keys] 
    else:
        return None

def get_interaction(drug1, drug2):
    tpl_keys = tuple([drug1, drug2].sort())
    if tpl_keys in list(dct_DB_TS.keys()):
        return dct_DB_TS[tpl_keys][1] 
    else:
        return None
    
def get_ae(drug1, drug2):
    tpl_keys = tuple([drug1, drug2].sort())
    if tpl_keys in list(dct_DB_TS.keys()):
        return dct_DB_TS[tpl_keys][0] 
    else:
        return None    
    
#Extracting AE from Offsides
def get_ae_offsides(drug):
    if drug in list(set(offsides['drug'])):
    #if drug in lst_drugs_offsides:
        offsides_subset = offsides[offsides['drug']==drug]
        dct_drug_extract_offsides = dict(zip( offsides_subset['umls_id'], list(zip(offsides_subset['rr'].round(2), offsides_subset['pvalue'])) ))
        return dct_drug_extract_offsides
    else:
        #print(drug + ' has no reported AE in Offsides')
        return None

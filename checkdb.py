'''

Check occurrences Drug1-Drug2 pairs in DrugBank and Twosides

'''

#DrugBank
def get_interaction(drug1, drug2):
    if drug1 in list(dct_interact.keys()):
        if drug2 in list(dct_interact[drug1].keys()):
            result = dct_interact[drug1][drug2]
            return result
        else:
            #print(drug1 + ' does not interact with ' + drug2)
            return None         
    else:
        #print(drug1 + ' not in DrugBank')
        return None

def get_ae(drug1, drug2):
    twosides_subset = twosides[(twosides['drug1'] == drug1) & (twosides['drug2'] == drug2) |
        (twosides['drug2'] == drug1) & (twosides['drug1'] == drug2)]
    if twosides_subset.empty:
        return None
    else:
        dct = dict(zip( twosides_subset['event_umls_id'], twosides_subset['proportional_reporting_ratio'].round(2) ))
        return dct

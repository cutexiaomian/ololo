import requests
import json
def get_description_from_pubchem_by_cid(cid:int):
    description = ''
    response = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON/')
    j = json.loads(response.text)
    for a in j['Record']['Section']:
        if a['TOCHeading']=='Names and Identifiers':
            for b in a['Section']:
                if b['TOCHeading'] =='Record Description':
                    for c in b['Information']:
                        description = description+str(c['Value']['StringWithMarkup'][0]['String'])+'\n'
    return description

if __name__ == '__main__':
    print(get_description_from_pubchem_by_cid(1983))


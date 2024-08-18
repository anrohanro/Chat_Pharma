import requests

def chemblid_to_smiles(chembl_id):
    url = f'https://www.ebi.ac.uk/chembl/api/data/molecule/{chembl_id}.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('molecule_structures', {}).get('canonical_smiles', 'SMILES not found')
    else:
        return 'Error fetching data'

if __name__ == '__main__':
    chembl_id = input("Enter the ChEMBL ID: ")
    smiles = chemblid_to_smiles(chembl_id)
    print(f'SMILES string for {chembl_id}: {smiles}')

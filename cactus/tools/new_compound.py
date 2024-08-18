import requests
import os
import toml
import json
import subprocess
from langchain.tools import BaseTool
import re

DESC = """This tool generates new compounds similar to those represented by provided ChEMBL IDs. It creates a folder containing potential drug candidates based on the input list of ChEMBL IDs.
Example Usage:
Input a list of ChEMBL IDs, and this tool will analyze the compounds they represent.
It will then generate a set of new, similar compounds and save them in a designated folder.
These newly created compounds can serve as potential candidates for drug development.
"""

class new_compound(BaseTool):
    name = "new_compound"
    description = DESC

    def chemblid_to_smiles(self, chembl_id):
        chembl_id = re.sub(r'[^A-Za-z0-9 ]+', '', chembl_id)
        url = f'https://www.ebi.ac.uk/chembl/api/data/molecule/{chembl_id}.json'
        # open("output_cool.txt", "w").write(str(url))
        with open("output_cool2.txt", "w") as file:
            file.write(str(url))
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('molecule_structures', {}).get('canonical_smiles', 'SMILES not found')
        else:
            return str(url)

    def convert_chemblids_to_smiles(self, chembl_ids):
        smiles_dict = {}
        for chembl_id in chembl_ids:
            smiles = self.chemblid_to_smiles(chembl_id)
            smiles_dict[chembl_id] = smiles
        return smiles_dict

    def save_smiles_to_files(self, smiles_dict, folder='smiles'):
        # Create the folder if it does not exist
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        for i, (chembl_id, smiles) in enumerate(smiles_dict.items(), start=1):
            filename = os.path.join(folder, f'f{i}.smi')
            with open(filename, 'w') as file:
                file.write(f'{smiles}\t{chembl_id}\n')
            print(f'SMILES string for {chembl_id} saved to {filename}')

    def get_smiles_for_chembl_ids(self, chembl_ids):
        smiles_dict = self.convert_chemblids_to_smiles(chembl_ids)
        self.save_smiles_to_files(smiles_dict)
        return smiles_dict

    def generate_config_toml(self, smiles_file, output_file):
        # Fixed parameters
        model_file = "priors/mol2mol_medium_similarity.prior"
        sample_strategy = "beamsearch"
        temperature = 1.0
        tb_logdir = "tb_logs"
        num_smiles = 3
        unique_molecules = True
        randomize_smiles = True
        run_type = "sampling"
        device = "cuda:0"
        json_out_config = "_sampling.json"
        
        # Create TOML configuration
        config = {
            'run_type': run_type,
            'device': device,
            'json_out_config': json_out_config,
            'parameters': {
                'model_file': model_file,
                'smiles_file': smiles_file,
                'sample_strategy': sample_strategy,
                'temperature': temperature,
                'tb_logdir': tb_logdir,
                'output_file': output_file,
                'num_smiles': num_smiles,
                'unique_molecules': unique_molecules,
                'randomize_smiles': randomize_smiles,
            }
        }
        
        # Save TOML configuration to file
        toml_filename = 'config.toml'
        with open(toml_filename, 'w') as f:
            toml.dump(config, f)
        print(f'TOML configuration file "{toml_filename}" has been created.')
        
        # Save TOML configuration to JSON file
        json_filename = 'config.json'
        with open(json_filename, 'w') as f:
            json.dump(config, f, indent=4)
        print(f'JSON configuration file "{json_filename}" has been created.')

    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print("STDOUT:")
            print(result.stdout)
            print("\nSTDERR:")
            print(result.stderr)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return e

    def new_compound(self, l1):
        smiles_dict = self.get_smiles_for_chembl_ids(l1)
        results = []
        for i, chembl_id in enumerate(l1, start=1):
            smiles_file = f"C:\\Users\\Rohan KumarMishra\\Desktop\\hide\\chat_pharma\\src\\smiles\\f{i}.smi"
            output_file = f"C:\\Users\\Rohan KumarMishra\\Desktop\\hide\\chat_pharma\\src\\samples\\sampling{i}.csv"
            self.generate_config_toml(smiles_file, output_file)
            command = "reinvent -l sampling.log config.toml"
            result = self.execute_command(command)
            results.append({
                "chembl_id": chembl_id,
                "smiles_file": smiles_file,
                "output_file": output_file,
                "command_result": result.stdout
            })
        return results

    def _run(self, lig: list) -> list:
        """
        Retrieve (gene/protein)-ligand associations for a given of gene/protein name and return the ligands chembl id which attach to that particular protein.

        Args:
        gene/protein name (str): The ID of the gene/protein.

        Returns:
        list: A list of tuples containing ligands Chembl-ID 
        """
        lig2=lig.strip('[]').replace(' ', '').split(',')
        results = self.new_compound(lig2)
        return results

    async def _arun(self, gene: str, num_results: int = 10) -> list:
        """Use the new_compound tool asynchronously."""
        raise NotImplementedError()

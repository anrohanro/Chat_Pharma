import requests
import xml.etree.ElementTree as ET
from langchain.tools import BaseTool

DESC = """This tool retrieves ligand associations for a given gene or protein name from the ChEMBL database.
Provide a gene or protein name as input to fetch ChEMBL IDs of ligands associated with it.

Example Usage:
If you input a gene or protein name, this tool will search the ChEMBL database for ligands known to interact with it. It returns ChEMBL IDs that represent these ligands, facilitating research into protein-ligand interactions.
"""

class get_ligands(BaseTool):
    name = "get_ligands"
    description = DESC

    def _run(self, gene: str) -> list:
        """
        Retrieve (gene/protein)-ligand associations for a given of gene/protein name and return the ligands chembl id which attach to that particular protein.

        Args:
        gene/protein name (str): The ID of the gene/protein.

        Returns:
        list: A list of tuples containing ligands Chembl-ID 
        """
        def get_chembl_ids(target_name):
            base_url = "https://www.ebi.ac.uk/chembl/api/data/target/search"
            params = {
                "q": target_name
            }

            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()  # Raise an exception for bad status codes

                root = ET.fromstring(response.content)
                targets = root.findall('.//target_chembl_id')

                chembl_ids = [target.text for target in targets]

                if chembl_ids:
                    return chembl_ids
                else:
                    return ["Target not found in ChEMBL."]

            except requests.exceptions.RequestException as e:
                return [f"Error: {e}"]

        def get_ligand_chembl_ids(chembl_id):
            base_url = "https://www.ebi.ac.uk/chembl/api/data/activity"
            params = {
                "target_chembl_id__in": chembl_id,
                "assay_type": "B"
            }

            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()  # Raise an exception for bad status codes

                root = ET.fromstring(response.content)
                ligands = root.findall('.//molecule_chembl_id')

                ligand_chembl_ids = [ligand.text for ligand in ligands]

                if ligand_chembl_ids:
                    return ligand_chembl_ids
                else:
                    return ["No ligands found for this ChEMBL ID."]

            except requests.exceptions.RequestException as e:
                return [f"Error: {e}"]

        def fetch_ligands_for_target(target_name):
            chembl_ids = get_chembl_ids(target_name)
            if not chembl_ids or any("Error" in cid for cid in chembl_ids) or "not found" in chembl_ids:
                return "Cannot fetch ligands without a valid ChEMBL ID."

            unique_ligand_ids = set()
            for chembl_id in chembl_ids:
                ligand_ids = get_ligand_chembl_ids(chembl_id)
                unique_ligand_ids.update(ligand_ids)

            return list(unique_ligand_ids)
        rep=f"Ligand ChEMBL IDs for {gene}:{fetch_ligands_for_target(gene)}"
        return rep

    async def _arun(self, gene: str, num_results: int = 10) -> list:
        """Use the get_ligands tool asynchronously."""
        raise NotImplementedError()

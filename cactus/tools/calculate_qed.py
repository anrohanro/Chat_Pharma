# """Tool to calculate the QED of a compound."""

# from langchain.tools import BaseTool
# from rdkit.Chem import Descriptors, MolFromSmiles


# class CalculateQED(BaseTool):
#     """Calculate the QED of the compound."""

#     name = "CalculateQED"
#     description = "Compute Quantitative Estimate of Druglikeness (QED) of the given molecule"

#     def _run(self, compound: str) -> float:
#         """Compute Quantitative Estimate of Druglikeness (QED) of the given molecule.

#         Bickerton et al 2012.

#         Parameters
#         ----------
#         compound: Compound in SMILES format

#         Returns
#         -------
#         float: The QED from 0 (druglike) to 1 (not)
#         """
#         return Descriptors.qed(MolFromSmiles(compound))

#     async def _arun(self, compound: str) -> float:
#         """Use the calculate_QED tool asynchronously."""
#         raise NotImplementedError()
    

import os
import pandas as pd
from typing import List, Dict
from rdkit.Chem import Descriptors, MolFromSmiles
from langchain.tools import BaseTool
import json

class CalculateQED(BaseTool):
    """Tool to calculate the QED of compounds."""
    name = "CalculateQED"
    description = "Compute Quantitative Estimate of Druglikeness (QED) of the given molecule and return those with QED > 0.5."
    def _run(self, compounds: List[str]) -> Dict[str, float]:
        """Calculate the QED for each compound and return those with QED > 0.5."""
        folder_path = r"C:\Users\Rohan KumarMishra\Desktop\hide\chat_pharma\src\samples"  # Your folder path
        new_comp = self.read_csv_files_from_folder(folder_path)

        results = {}
        for compound in new_comp:
            mol = MolFromSmiles(compound)
            if mol:
                qed_value = Descriptors.qed(mol)
                if qed_value > 0.5:
                    results[compound] = qed_value
        with open(r"C:\Users\Rohan KumarMishra\Desktop\final_comp.json", 'w') as file:
            json.dump(results, file, indent=4)  # indent=4 for pretty printing
        return list(islice(results.keys(), 3))

    def read_csv_files_from_folder(self, folder_path: str) -> List[str]:
        """Read CSV files from a folder and extract the first column."""
        compounds = []

        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(folder_path, filename)

                try:
                    # Read the CSV file, skipping the header row
                    df = pd.read_csv(file_path, skiprows=1, header=None)

                    if not df.empty:
                        # Extract the first column and filter out NaN values
                        first_column = df.iloc[:, 0].dropna().tolist()
                        if first_column:
                            compounds.extend(first_column)
                        else:
                            print(f"{filename} has no data in the first column (excluding the first row).")
                    else:
                        print(f"{filename} is empty.")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

        return compounds

    async def _arun(self, compounds: List[str]) -> Dict[str, float]:
        """Use the CalculateQED tool asynchronously."""
        raise NotImplementedError("Asynchronous execution is not supported.")


'''
    
    from langchain.tools import BaseTool
from rdkit.Chem import Descriptors, MolFromSmiles
from typing import List, Dict


class CalculateQED(BaseTool):
    """Calculate the QED of the compound."""

    def _run(self, compounds: List[str]) -> Dict[str, float]:
        """Calculate the QED for each compound and return those with QED > 0.5."""
        results = {}
        for compound in compounds:
            mol = MolFromSmiles(compound)
            if mol:
                qed_value = Descriptors.qed(mol)
                if qed_value > 0.5:
                    results[compound] = qed_value
        return results

    async def _arun(self, compounds: List[str]) -> Dict[str, float]:
        """Use the calculate_QED tool asynchronously."""
        raise NotImplementedError()

    
    '''

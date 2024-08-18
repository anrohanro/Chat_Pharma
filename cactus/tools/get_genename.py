import requests
from langchain.tools import BaseTool

DESC = """Use this tool when you need to retrieve gene information from the NCBI Datasets API. 
Provide a gene symbol as input to fetch gene description(which is the gene full name) for the specified gene. 
"""


class get_genename(BaseTool):
    name = "get_genename"
    description = DESC

    def _run(self, gene_symbol: str) -> list:
        """
        Retrieve gene information from the NCBI Datasets API.

        Args:
            gene_symbol (str): The symbol or identifier of the gene.

        Returns:
            str: A description of the gene if found, otherwise an error message.
        """

        # Define the base URL for the NCBI Datasets API
        base_url = 'https://api.ncbi.nlm.nih.gov/datasets/v2alpha'
        taxon = '9606'  # Taxon for human (Homo sapiens)
        api_key = 'b90ce033aeb44a7741d92d596e6ce32f2008'
        
        # Construct the endpoint URL for gene reports
        endpoint = f'{base_url}/gene/symbol/{gene_symbol}/taxon/{taxon}'

        # Set headers including the API key
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            gene_data = response.json()
            if isinstance(gene_data, dict) and 'reports' in gene_data:
                for report in gene_data['reports']:
                    gene_info = report.get('gene')
                    if gene_info:
                        return gene_info.get('description')
            return f"Gene symbol '{gene_symbol}' not found in taxon '{taxon}'."
        else:
            return f"Failed to retrieve gene data. Status code: {response.status_code}"

    async def _arun(self, gene_symbol: str, num_results: int = 10) -> list:
        """Use the GetTargets tool asynchronously."""
        raise NotImplementedError()

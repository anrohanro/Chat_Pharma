import requests
import json
import time
from langchain.tools import BaseTool

DESC = """Use this tool when you need to retrieve gene-disease associations from the DisGeNET database. 
Provide a disease ID as input and optionally specify the number of top results to return based on the gene-disease association score.
"""

class get_targets(BaseTool):
    name = "get_targets"
    description = DESC

    def _run(self, disease_id: str) -> list:
        """
        Retrieve gene-disease associations for a given disease ID and return the specified number of results sorted by score.

        Args:
        disease_id (str): The ID of the disease.
        num_results (int): The number of top associations to return based on score. Default is 10.

        Returns:
        list: A list of tuples containing gene symbol, Gene NCBI ID, and score.
        """
        # Provide your API key
        # API_KEY = "eb6a0063-7b68-44d8-b435-a38303701f29"
        API_KEY = "1cdfc68d-442f-4185-8b67-d51efc1e8748"
        
        # Specify query parameters by means of a dictionary
        params = {
            "disease": disease_id,
            "page_number": "0"
        }

        # Create a dictionary with the HTTP headers of your API call
        HTTPheadersDict = {
            'Authorization': API_KEY,
            'accept': 'application/json'
        }

        # Query the gda summary endpoint
        response = requests.get("https://api.disgenet.com/api/v1/gda/summary",
                                params=params, headers=HTTPheadersDict, verify=False)

        # If the status code of response is 429, it means you have reached one of your query limits
        # You can retrieve the time you need to wait until doing a new query in the response headers
        if not response.ok:
            if response.status_code == 429:
                while response.ok is False:
                    wait_time = int(response.headers['x-rate-limit-retry-after-seconds'])
                    print(f"You have reached a query limit. Please wait {wait_time} seconds.")
                    time.sleep(wait_time)

                    # Repeat your query
                    response = requests.get("https://api.disgenet.com/api/v1/gda/summary",
                                            params=params, headers=HTTPheadersDict, verify=False)
                    if response.ok:
                        break

        # Parse response content in JSON format since we set 'accept:application/json' as HTTP header
        response_parsed = json.loads(response.text)

        if response.ok:
            # Check if 'payload' key is present and not empty in the response
            if "payload" in response_parsed and response_parsed["payload"]:
                gene_disease_associations = []
                # Extract gene-disease associations
                for assoc in response_parsed["payload"]:
                    gene_symbol = assoc.get('symbolOfGene', 'N/A')
                    gene_ncbi_id = assoc.get('geneNcbiID', 'N/A')
                    score = assoc.get('score', 'N/A')
                    gene_disease_associations.append((gene_symbol, gene_ncbi_id, score))
                
                # Sort the associations by score in descending order and return the top num_results
                gene_disease_associations.sort(key=lambda x: x[2], reverse=True)
                return gene_disease_associations[:5]
            else:
                return "No gene-disease associations found for the given disease ID."
        else:
            return f"Error: {response_parsed.get('error', 'Unknown error')}"

    async def _arun(self, disease_id: str, num_results: int = 10) -> list:
        """Use the GetTargets tool asynchronously."""
        raise NotImplementedError()

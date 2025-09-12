import requests
import json

# for api key
from dotenv import load_dotenv
import os

def search_papers(params: dict, headers: dict, limit: int = 10):
    """
    Searches for papers on Semantic Scholar using specified criteria.

    Args:
        query (str): The search term.
        fields (list): A list of fields to retrieve for each paper.
        filters (dict): A dictionary of optional filters like 'year', 'openAccessPdf', etc.
        limit (int): The number of results to return.

    Returns:
        dict: The JSON response from the API, or None if an error occurs.
    """
    # Define the API endpoint URL

    # Specify the search term
    url = "http://api.semanticscholar.org/graph/v1/paper/search/bulk"

    response = requests.get(url, params=params, headers=headers).json()

    # print(f"Will retrieve an estimated {response['total']} documents")
    retrieved = 0
    # Write results to json file and get next batch of results
    with open(f"papers.json", "a") as file:
        while True:
            if "data" in response:
                retrieved += len(response["data"])
                print(f"Retrieved {retrieved} papers...")
                for paper in response["data"]:
                    print(json.dumps(paper), file=file)
            # checks for continuation token to get next batch of results
            if "token" not in response:
                break
            response = requests.get(f"{url}&token={response['token']}").json()

    print(f"Done! Retrieved {retrieved} papers total")


def main():
    """
    Main function to run the paper search and display results.
    """
    # --- Search Criteria ---
    # Specify the fields you want in the response.
    # Note 'authors' will return authorId and name by default.
    result_fields = ['title', 'year', 'authors', 'url', 'publicationTypes', 'publicationDate', 'openAccessPdf']

    # Specify filters. Note: 'openAccessPdf' is a boolean flag, its value doesn't matter.
    query_params = {
        "query": '"Approximating new spaces of consumption at the Abasto Shopping Mall, Buenos Aires, Argentina"',
        "fields": ','.join(result_fields),
        "year": "1950-"
    }

    load_dotenv()
    api_key = os.getenv("API_KEY")  # Replace with the actual API key

    # Define headers with API key
    headers = {"x-api-key": api_key}

    search_results = search_papers(
        params=query_params,
        headers=headers,
        limit=5  # Let's get 5 results for this example
    )


if __name__ == "__main__":
    main()

"""
'fields': ",".join(fields),
"""

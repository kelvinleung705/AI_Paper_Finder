import requests
import json

def search_papers(query: str, fields: list, filters: dict, limit: int = 10):
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
    api_url = 'https://api.semanticscholar.org/graph/v1/paper/search'

    # Construct the parameters for the GET request
    params = {
        'query': query,
        'fields': ",".join(fields),
        'limit': limit
    }
    # Add optional filters to the parameters
    params.update(filters)

    print("Requesting URL:", requests.Request('GET', api_url, params=params).prepare().url)

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON. Response text: {response.text}")
    return None


def main():
    """
    Main function to run the paper search and display results.
    """
    # --- Search Criteria ---
    search_query = 'language models code generation'
    # Specify the fields you want in the response.
    # Note 'authors' will return authorId and name by default.
    result_fields = ['title', 'year', 'authors']

    # Specify filters. Note: 'openAccessPdf' is a boolean flag, its value doesn't matter.
    search_filters = {
        'year': '2021-2023',
        'openAccessPdf': True,
        'fieldsOfStudy': ['Computer Science']
    }

    # --- Perform the Search ---
    search_results = search_papers(
        query=search_query,
        fields=result_fields,
        filters=search_filters,
        limit=5  # Let's get 5 results for this example
    )

    # --- Process and Display Results ---
    if search_results:
        print("\n--- Search Results ---")
        print(f"Total results found: {search_results.get('total', 0)}")
        print(f"Next offset for pagination: {search_results.get('next', 'N/A')}")

        papers = search_results.get('data', [])

        if not papers:
            print("No papers found matching the criteria.")
            return

        for i, paper in enumerate(papers, 1):
            title = paper.get('title', 'N/A')
            year = paper.get('year', 'N/A')
            authors = ", ".join([author['name'] for author in paper.get('authors', [])])

            print(f"\n{i}. Title: {title}")
            print(f"   Year: {year}")
            print(f"   Authors: {authors}")
            print(f"   Paper ID: {paper['paperId']}")


if __name__ == "__main__":
    main()

"""
'fields': ",".join(fields),
"""

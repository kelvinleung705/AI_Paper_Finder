import requests
import json


def main():
    """
    Main function to fetch paper details from the Semantic Scholar API.
    """
    api_url = 'https://api.semanticscholar.org/graph/v1/paper/batch'

    # --- Parameters for the API request ---

    # The fields you want the API to return for each paper.
    fields_to_request = 'referenceCount,citationCount,title'

    # A list of paper IDs to look up.
    # You can use S2 Paper IDs, Corpus IDs, DOI, ArXiv IDs, etc.
    paper_ids = ["649def34f8be52c8b66281af98ae884c09aef38b", "ARXIV:2106.15928"]

    print(f"Fetching data for {len(paper_ids)} papers...")

    try:
        # Make the POST request
        response = requests.post(
            api_url,
            params={'fields': fields_to_request},
            json={"ids": paper_ids}
        )

        # Raise an exception if the request returned an error status code
        response.raise_for_status()

        # Get the JSON response data
        data = response.json()

        # Pretty-print the JSON response
        print(json.dumps(data, indent=2))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the network request: {e}")
    except json.JSONDecodeError:
        print("Failed to decode the response as JSON. Response text:")
        print(response.text)


# This standard Python construct ensures that main() is called only when
# the script is executed directly.
if __name__ == "__main__":
    main()

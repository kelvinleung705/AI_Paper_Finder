import requests
import json

# for api key
from dotenv import load_dotenv
import os

# Define the API endpoint URL
url = "https://api.semanticscholar.org/recommendations/v1/papers"

# Define the query parameters
query_params = {
    "fields": "title,url,citationCount,authors",
    "limit": "500"
}

# Define the request data
data = {
    "positivePaperIds": [
        "02138d6d094d1e7511c157f0b1a3dd4e5b20ebee",
        "018f58247a20ec6b3256fd3119f57980a6f37748"
    ],
    "negativePaperIds": [
        "0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc"
    ]
}

# Directly define the API key (Reminder: Securely handle API keys in production environments)
load_dotenv()
api_key = os.getenv("API_KEY")  # Replace with the actual API key

# Define headers with API key
headers = {"x-api-key": api_key}

# Send the API request
response = requests.post(url, params=query_params, json=data, headers=headers).json()

# Sort the recommended papers by citation count
papers = response["recommendedPapers"]
papers.sort(key=lambda paper: paper["citationCount"], reverse=True)

with open('recommended_papers_sorted.json', 'w') as output:
    json.dump(papers, output)

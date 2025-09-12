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
"""
data = {
    "positivePaperIds": [
        "02138d6d094d1e7511c157f0b1a3dd4e5b20ebee",
        "018f58247a20ec6b3256fd3119f57980a6f37748"
    ],
    "negativePaperIds": [
        "0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc"
    ]
}
"""

data = {
    "positivePaperIds": [
        "fa7b3285a2c6badbf66323489238a3c8889d1191",
        "8c5d12d1341acb5a56951b7847ceb0b7b17a8187",
        "a809fa9179f3af0b6f521333d287fe4f4d7de1ba",
        "0aa00409766cb4d9553cda30b0e72ab78b8985e2"
    ],
    "negativePaperIds": []
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
for item in papers:
    print(item)

with open('recommended_papers_sorted.json', 'w') as output:
    json.dump(papers, output)

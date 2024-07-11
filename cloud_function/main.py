import json
import requests
from google.cloud import bigquery
from bs4 import BeautifulSoup

def save_to_bq(request):
    # Get the URL from the request
    request_json = request.get_json(silent=True)
    url = request_json.get('url')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Initialize BigQuery client
    client = bigquery.Client()

    # Define the BigQuery table schema
    table_id = "nlp-cc-project.scraper_ds.web_content"
    rows_to_insert = [{"url": url, "content":content}]

    # Insert the URL into BigQuery
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        return "Content saved to BigQuery."
    else:
        return f"Failed to save URL: {errors}", 500

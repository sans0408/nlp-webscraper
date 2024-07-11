# NLP Webscraper
Website to webscrape a given link and display information about it

## Table of Contents
1. [Introduction](#introduction)
2. [Cloud Platform Setup](#cloud-platform-setup)
3. [Web Interface for Web Scraping](#web-interface-for-web-scraping)
4. [Data Warehousing with BigQuery](#data-warehousing-with-bigquery)
5. [NLP Analysis](#nlp-analysis)
6. [Cloud Deployment of NLP Analysis](#cloud-deployment-of-nlp-analysis)
7. [HTTP Trigger and Data Transfer](#http-trigger-and-data-transfer)
8. [Conclusion](#conclusion)
9. [Getting Started](#getting-started)
10. [Usage](#usage)

## Introduction
This project integrates Natural Language Processing (NLP) and cloud-based web scraping to create a comprehensive data processing pipeline. The goal is to collect, analyze, and derive insights from web-sourced textual data using scalable cloud resources.

## Cloud Platform Setup
### Create New Project on Google Cloud Platform
- Log in to Google Cloud Platform.
- Create a new project from the dashboard.

### Enable Necessary APIs
- Enable APIs for Storage, Functions, BigQuery, and NLP services.

### Set Appropriate Permissions
- Configure IAM roles for access management.

## Web Interface for Web Scraping
### Design and Host the Web Interface
- Use HTML/CSS for the frontend.
- Use Flask for the backend.

### Develop Web Scraping Functionality
- Python scripts with BeautifulSoup for data extraction.
- Triggered by user input on the web interface.

## Data Warehousing with BigQuery
### Set Up BigQuery
- Create datasets and tables.
- Define schema for the data.

### Insert Scraped Data into BigQuery
- Use BigQuery client library.
- Insert scraped data into the defined table.

## NLP Analysis
### Setup Environment
- Launch a VM instance on Google Cloud.
- Install Python and NLTK library.
- Setup NLTK data resources.

### Perform NLP Analysis with NLTK
- **Tokenization**: Use `word_tokenize()` for word segmentation.
- **Grammar Creation with CFG**: Define grammar rules using NLTK’s CFG class.
- **Text Encoding and Decoding**: Encode with UTF-8 and decode, checking for consistency.
- **POS Tagging**: Tag words using `pos_tag()`.
- **Frequency Distribution**: Analyze word frequency with FreqDist.

## Cloud Deployment of NLP Analysis
### Store Results in Cloud Storage
- Save processed data in a Google Cloud Storage bucket.

### Display Results on Web Page
- Show analysis results on the web interface.

## HTTP Trigger and Data Transfer
### HTTP Trigger for BigQuery
- Define an HTTP trigger to transfer data.
- Define the schema and data insertion code.

### Results
- Successful deployment and demonstration of results.

## Conclusion
### Summary
- Integration of NLP with cloud-based web scraping.
- Efficient data processing and storage using cloud resources.

## Getting Started
### Prerequisites
- Google Cloud Platform account.
- Python 3.x installed locally.
- Basic knowledge of HTML, CSS, JavaScript, and Python.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/nlp-cloud-pipeline.git
    cd nlp-cloud-pipeline
    ```
2. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration
1. Set up Google Cloud Project and enable necessary APIs.
2. Configure `app.py` with your Google Cloud credentials and project details.

## Usage
1. Run the Flask app locally:
    ```bash
    flask run
    ```
2. Open a browser and navigate to `http://127.0.0.1:5000`.
3. Enter the URL to be scraped and click 'Scrape'.
4. View the results on the results page.

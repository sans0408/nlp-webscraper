from flask import Flask, render_template, request
import requests
from scraper import scrape_and_analyze

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            pos_tags, frequency_distribution, grammar = scrape_and_analyze(url)

            # Save URL to BigQuery
            bigquery_response = requests.post(
                "https://us-central1-nlp-cc-project.cloudfunctions.net/save_to_bq",
                json={"url": url}
            )

            # Save results to GCS
            results = {
                "pos_tags": pos_tags,
                "frequency_distribution": frequency_distribution,
                "grammar": grammar
            }
            gcs_response = requests.post(
                "https://us-central1-nlp-cc-project.cloudfunctions.net/save_results_to_gcs",
                json={"results": results}
            )

            return render_template('results.html', pos_tags=pos_tags, frequency_distribution=frequency_distribution, grammar=grammar, encoding_check="No changes detected between encoded and decoded text.")
        return "No URL provided", 400
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
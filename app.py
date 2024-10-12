from flask import Flask, render_template, request, jsonify, redirect, url_for
from tavily import TavilyClient
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Hardcode the Tavily API key
tavily_api_key = "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"

tavily_client = TavilyClient(api_key=tavily_api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({"error": "Search query is empty"}), 400
    
    if len(query) < 3:
        return jsonify({"error": "Search query must be at least 3 characters long"}), 400
    
    try:
        # Perform search using Tavily API
        search_response = tavily_client.search(query=query, search_depth="advanced")
        
        # Extract relevant information from the API response
        results = []
        for result in search_response.get('results', []):
            results.append({
                'title': result.get('title', ''),
                'url': result.get('url', ''),
                'snippet': result.get('content', '')
            })
        
        return render_template('results.html', results=results, query=query)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/lucky')
def lucky():
    query = request.args.get('q', '')
    if not query:
        return redirect(url_for('index'))
    
    try:
        # Perform search using Tavily API
        search_response = tavily_client.search(query=query, search_depth="advanced", max_results=1)
        
        # Redirect to the first result if available
        if search_response.get('results'):
            return redirect(search_response['results'][0].get('url', url_for('index')))
        else:
            return redirect(url_for('index'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

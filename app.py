# expose one end point here at least

"""
Option 1:
An APScheduler job within app.py that runs once a day and triggers generation for a predefined
keyword (e.g., "wireless earbuds"), storing the result in a local file or printing to console;
"""

from flask import Flask, request, jsonify
from ai_generator import generate_blog_post
from seo_fetcher import fetch_seo_data
app =  Flask(__name__)


@app.route("/generate")
def generate():
    keyword = request.args.get("keyword")
    seo_data = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)
    return jsonify({"keyword": keyword, "seo_data": seo_data, "content": content})

if __name__ == "__main__":
    app.run(debug=True)

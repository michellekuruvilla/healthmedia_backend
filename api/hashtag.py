from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# In-memory storage of hashtag data (you can upgrade to a database later)
hashtag_data = defaultdict(list)

@app.route('/')
def home():
    return "Legoland Hashtag Effectiveness API is running."

@app.route('/api/hashtag', methods=['POST'])
def add_hashtag_data():
    """
    Accepts JSON:
    {
        "hashtag": "#legoland",
        "views": 12000
    }
    """
    data = request.json
    hashtag = data.get('hashtag', '').lower()
    views = data.get('views')

    if not hashtag or views is None:
        return jsonify({"error": "Missing hashtag or views"}), 400

    hashtag_data[hashtag].append(views)
    return jsonify({"message": f"Added {views} views to {hashtag}"}), 201

@app.route('/api/hashtags', methods=['GET'])
def get_all_data():
    return jsonify(hashtag_data)

@app.route('/api/hashtag/averages', methods=['GET'])
def get_averages():
    averages = {
        tag: int(sum(views) / len(views))
        for tag, views in hashtag_data.items()
        if views
    }
    return jsonify(averages)

if __name__ == '__main__':
    app.run(debug=True)

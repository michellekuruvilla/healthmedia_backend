from flask import Flask, jsonify, request
import csv
from collections import defaultdict

app = Flask(__name__)

@app.route("/api/analyze_hashtags", methods=["POST"])
def analyze_hashtags():
    # Get the CSV file from the POST request
    file = request.files.get("csv_file")

    if not file:
        return jsonify({"error": "CSV file is required"}), 400

    input_file = "temp_legolandcalifornia_hashtags.csv"
    file.save(input_file)

    hashtag_stats = defaultdict(lambda: {
        "total_posts": 0,
        "total_likes": 0,
        "total_comments": 0,
        "total_engagement_rate": 0.0
    })

    try:
        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                hashtags = row["Hashtags"].split(", ")
                likes = int(row["Likes"])
                comments = int(row["Comments"])
                engagement = (likes + comments) / 100000  # Example: 100k followers

                for tag in hashtags:
                    stats = hashtag_stats[tag]
                    stats["total_posts"] += 1
                    stats["total_likes"] += likes
                    stats["total_comments"] += comments
                    stats["total_engagement_rate"] += engagement
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Calculate averages
    result = {}
    for tag, stats in hashtag_stats.items():
        total = stats["total_posts"]
        result[tag] = {
            **stats,
            "avg_likes": stats["total_likes"] / total,
            "avg_comments": stats["total_comments"] / total,
            "avg_engagement_rate": stats["total_engagement_rate"] / total
        }

    # Return the result as JSON
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

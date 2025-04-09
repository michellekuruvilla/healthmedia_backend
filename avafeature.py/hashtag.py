import csv
import json
from collections import defaultdict

input_file = "legolandcalifornia_hashtags.csv"
output_file = "hashtag_metrics.json"

hashtag_stats = defaultdict(lambda: {
    "total_posts": 0,
    "total_likes": 0,
    "total_comments": 0,
    "total_engagement_rate": 0.0
})

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        hashtags = row["Hashtags"].split(", ")
        likes = int(row["Likes"])
        comments = int(row["Comments"])
        engagement = (likes + comments) / 100000  # Assume 100k followers (adjust if needed)

        for tag in hashtags:
            stats = hashtag_stats[tag]
            stats["total_posts"] += 1
            stats["total_likes"] += likes
            stats["total_comments"] += comments
            stats["total_engagement_rate"] += engagement

# Calculate averages
for tag, stats in hashtag_stats.items():
    total = stats["total_posts"]
    stats["avg_likes"] = stats["total_likes"] / total
    stats["avg_comments"] = stats["total_comments"] / total
    stats["avg_engagement_rate"] = stats["total_engagement_rate"] / total

# Save to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(hashtag_stats, f, indent=2)

print(f"Saved hashtag metrics to {output_file}")

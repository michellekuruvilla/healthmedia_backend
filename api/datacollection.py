import instaloader
from collections import defaultdict

# Set up Instaloader
L = instaloader.Instaloader()

# Login (optional but better for full access)
# L.login("your_username", "your_password")

# Load profile
profile = instaloader.Profile.from_username(L.context, "legolandcalifornia")

# Collect hashtag view data
hashtag_views = defaultdict(list)

for post in profile.get_posts():
    if post.caption:
        hashtags = [word.lower() for word in post.caption.split() if word.startswith('#')]
        views = post.video_view_count if post.is_video else post.likes
        for tag in hashtags:
            hashtag_views[tag].append(views)

# Calculate average views per hashtag
avg_views_per_hashtag = {
    tag: int(sum(views) / len(views))
    for tag, views in hashtag_views.items()
    if len(views) >= 3
}

# Optional: print top hashtags
top = sorted(avg_views_per_hashtag.items(), key=lambda x: x[1], reverse=True)
for tag, avg in top[:10]:
    print(f"{tag}: {avg}")

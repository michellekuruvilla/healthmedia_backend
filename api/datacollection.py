import instaloader
from collections import defaultdict

# Set up Instaloader
L = instaloader.Instaloader()

# Log in with your Instagram credentials
USERNAME = "avaroseswims@gmail.com"  # Replace with your IG username
PASSWORD = "avarose2008"  # Replace with your IG password

# Optional: load session if saved before
# L.load_session_from_file(USERNAME)

# Login to Instagram
L.login(USERNAME, PASSWORD)

# Optional: save session so you don’t need to login again next time
# L.save_session_to_file()

# Load Legoland California's profile
profile = instaloader.Profile.from_username(L.context, "legolandcalifornia")

# Collect hashtag view data
hashtag_views = defaultdict(list)

for post in profile.get_posts():
    if post.caption:
        hashtags = [word.lower() for word in post.caption.split() if word.startswith('#')]
        views = post.video_view_count if post.is_video else post.likes
        for tag in hashtags:
            hashtag_views[tag].append(views)

# Calculate average views per hashtag (only include hashtags used at least 3 times)
avg_views_per_hashtag = {
    tag: int(sum(views) / len(views))
    for tag, views in hashtag_views.items()
    if len(views) >= 3
}

# Optional: print top 10 performing hashtags
top = sorted(avg_views_per_hashtag.items(), key=lambda x: x[1], reverse=True)
for tag, avg in top[:10]:
    print(f"{tag}: {avg}")

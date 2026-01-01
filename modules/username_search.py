import requests

SITES = {
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "weight": 0.9
    },
    "Instagram": {
        "url": "https://www.instagram.com/{}/",
        "weight": 0.95
    },
    "Twitter/X": {
        "url": "https://twitter.com/{}",
        "weight": 0.9
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "weight": 0.9
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}/",
        "weight": 0.85
    },
    "GitHub": {
        "url": "https://github.com/{}",
        "weight": 0.95
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "weight": 0.7
    },
    "Pinterest": {
        "url": "https://www.pinterest.com/{}/",
        "weight": 0.7
    },
    "SoundCloud": {
        "url": "https://soundcloud.com/{}",
        "weight": 0.7
    },
    "Steam": {
        "url": "https://steamcommunity.com/id/{}",
        "weight": 0.6
    }
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def find_socials(username, tor=False):
    results = {}

    for site, info in SITES.items():
        profile_url = info["url"].format(username)

        try:
            r = requests.get(
                profile_url,
                headers=HEADERS,
                timeout=5,
                allow_redirects=True
            )

            if r.status_code == 200:
                results[site] = {
                    "weight": info["weight"],
                    "urls": [profile_url]
                }

        except requests.RequestException:
            continue

    return results

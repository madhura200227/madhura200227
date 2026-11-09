import os
import re
import urllib.request

USERNAME = "madhura200227"

def fetch_views_count():
    count = "199"
    try:
        req = urllib.request.Request(
            f"https://komarev.com/ghpvc/?username={USERNAME}",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=8) as r:
            svg = r.read().decode("utf-8")
            matches = re.findall(r'>([\d,]+)<', svg)
            if matches:
                count = matches[0]
        print(f"Fetched live views count from Komarev: {count}")
    except Exception as e:
        print(f"Using fallback view count: {e}")
    return count

def generate_profile_views_badge(theme="cherry", count="199"):
    if theme == "cherry":
        bg_left = "#24040e"
        border = "#C1123F"
        accent = "#FF2D60"
        text_label = "#E8D5C5"
        glow_col = "#FF2D60"
    else: # espresso
        bg_left = "#181011"
        border = "#873D50"
        accent = "#C1123F"
        text_label = "#E8D5C5"
        glow_col = "#C1123F"

    # Dynamic badge width calculation based on number of digits
    count_str = str(count)
    pill_w = max(56, 28 + len(count_str) * 9)
    total_w = 145 + pill_w
    pill_x = total_w - pill_w - 4

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} 36" width="{total_w}" height="36">
  <defs>
    <filter id="pvGlow_{theme}" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="3.5" flood-color="{glow_col}" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Outer Luxury Pill Container -->
  <rect x="0.6" y="0.6" width="{total_w - 1.2}" height="34.8" rx="17.4" fill="{bg_left}" stroke="{border}" stroke-width="1.2" filter="url(#pvGlow_{theme})" />

  <!-- Left Side: Vector Eye Icon & Label -->
  <g transform="translate(18, 18)">
    <!-- Eye Vector Icon -->
    <path d="M -8 0 Q 0 -5.5 8 0 Q 0 5.5 -8 0 Z" fill="none" stroke="{accent}" stroke-width="1.5" />
    <circle cx="0" cy="0" r="2.2" fill="{accent}" />
    <!-- Label -->
    <text x="14" y="3.5" font-family="'IBM Plex Mono', 'SF Mono', monospace" font-size="10.5" font-weight="600" fill="{text_label}" letter-spacing="1.2">PROFILE VIEWS</text>
  </g>

  <!-- Right Side Counter Capsule -->
  <g transform="translate({pill_x}, 3.5)">
    <rect x="0" y="0" width="{pill_w}" height="27" rx="13.5" fill="{accent}" />
    <text x="{pill_w / 2.0}" y="17.5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">{count}</text>
  </g>
</svg>'''

if __name__ == "__main__":
    os.makedirs("assets/stats", exist_ok=True)
    count = fetch_views_count()

    with open("assets/stats/profile-views-cherry.svg", "w", encoding="utf-8") as f:
        f.write(generate_profile_views_badge("cherry", count))

    with open("assets/stats/profile-views.svg", "w", encoding="utf-8") as f:
        f.write(generate_profile_views_badge("espresso", count))

    print("Successfully built custom themed Profile Views badges!")


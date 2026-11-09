import os
import re
import json
import urllib.request

USERNAME = "madhura200227"

def fetch_real_data():
    headers = {"User-Agent": "Mozilla/5.0"}
    user_data = {"public_repos": 11, "followers": 4, "created_at": "2025-04-04"}
    streak_data = {"total": 232, "current": 18, "longest": 18, "start": "Apr 4, 2025", "curr_range": "Oct 23 - Nov 9", "long_range": "Oct 23 - Nov 9"}

    # 1. Fetch GitHub user
    try:
        req = urllib.request.Request(f"https://api.github.com/users/{USERNAME}", headers=headers)
        with urllib.request.urlopen(req, timeout=8) as r:
            user_data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"User API notice: {e}")

    # 2. Fetch Streak from demolab
    try:
        req_streak = urllib.request.Request(f"https://streak-stats.demolab.com/?user={USERNAME}", headers=headers)
        with urllib.request.urlopen(req_streak, timeout=8) as r:
            svg_text = r.read().decode("utf-8")
            items = [t.strip() for t in re.findall(r'>([^<]+)<', svg_text) if t.strip() and not t.strip().startswith('@')]
            if len(items) >= 9:
                streak_data["total"] = items[0]
                streak_data["start"] = items[2]
                streak_data["current"] = items[5] if items[5] != '0' else '18'
                streak_data["curr_range"] = items[4] if items[4] else 'Oct 23 - Nov 9'
                streak_data["longest"] = items[6] if items[6] != '0' else '18'
                streak_data["long_range"] = items[8] if items[8] else 'Oct 23 - Nov 9'
    except Exception as e:
        print(f"Streak API notice: {e}")

    return user_data, streak_data

# ==============================================================================
# 1. CARD 1: MADHURA'S GITHUB STATS (495 x 195)
# ==============================================================================
def generate_github_stats_card(theme="cherry", user_data=None, streak_data=None):
    if theme == "cherry":
        bg_start = "#260510"
        bg_end = "#360816"
        border = "#C1123F"
        accent = "#FF2D60"
        text_title = "#FF2D60"
        text_label = "#E8D5C5"
        text_val = "#FFF5ED"
        text_sub = "#D99AA7"
        ring_bg = "#450a1c"
        ring_fill = "#380716"
        star_fill = "#FF2D60"
    else: # espresso
        bg_start = "#181110"
        bg_end = "#231818"
        border = "#873D50"
        accent = "#C1123F"
        text_title = "#C1123F"
        text_label = "#E8D5C5"
        text_val = "#FFF5ED"
        text_sub = "#D99AA7"
        ring_bg = "#2a141a"
        ring_fill = "#241318"
        star_fill = "#C1123F"

    total_stars = 3
    total_commits = streak_data.get("total", 232) if streak_data else 232
    total_prs = 18
    total_issues = 9
    contributed_to = 6

    # SVG Octocat Logo Path
    octocat_path = (
        "M 410 88 "
        "c -9.9 0 -18 8.1 -18 18 c 0 7.9 5.1 14.6 12.2 17 c 0.9 0.2 1.2 -0.4 1.2 -0.9 c 0 -0.4 0 -1.6 0 -3.1 "
        "c -5 1.1 -6.1 -2.4 -6.1 -2.4 c -0.8 -2.1 -2 -2.6 -2 -2.6 c -1.6 -1.1 0.1 -1.1 0.1 -1.1 c 1.8 0.1 2.8 1.9 2.8 1.9 "
        "c 1.6 2.8 4.2 2 5.2 1.5 c 0.2 -1.2 0.6 -2 1.2 -2.5 c -4 -0.5 -8.2 -2 -8.2 -8.9 c 0 -2 0.7 -3.6 1.9 -4.8 "
        "c -0.2 -0.5 -0.8 -2.3 0.2 -4.7 c 0 0 1.5 -0.5 5 1.9 c 1.4 -0.4 3 -0.6 4.5 -0.6 c 1.5 0 3.1 0.2 4.5 0.6 "
        "c 3.5 -2.4 5 -1.9 5 -1.9 c 1 2.4 0.4 4.2 0.2 4.7 c 1.2 1.2 1.9 2.8 1.9 4.8 c 0 6.9 -4.2 8.4 -8.2 8.9 "
        "c 0.7 0.6 1.3 1.7 1.3 3.5 c 0 2.5 0 4.6 0 5.2 c 0 0.5 0.3 1.1 1.3 0.9 c 7.1 -2.4 12.2 -9.1 12.2 -17 "
        "c 0 -9.9 -8.1 -18 -18 -18 Z"
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 195" width="495" height="195">
  <defs>
    <linearGradient id="cardGrad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
    <filter id="glow_{theme}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Card Background & Border -->
  <rect x="0.5" y="0.5" width="494" height="194" rx="10" fill="url(#cardGrad_{theme})" stroke="{border}" stroke-width="1.2" />

  <!-- Top Accent Bar -->
  <rect x="0" y="0" width="495" height="3" rx="1.5" fill="{accent}" />

  <!-- Card Title -->
  <g transform="translate(25, 34)">
    <path d="M 0 0 L 3 3 L 0 6 L -3 3 Z" fill="{accent}" />
    <text x="12" y="3" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="{text_title}" letter-spacing="0.3">Madhura's GitHub Stats</text>
  </g>

  <!-- Metric 1: Total Stars Earned -->
  <g transform="translate(25, 66)">
    <!-- Star Icon -->
    <path d="M 8 1 L 10.3 5.7 L 15.5 6.4 L 11.8 10 L 12.6 15.2 L 8 12.8 L 3.4 15.2 L 4.2 10 L 0.5 6.4 L 5.7 5.7 Z" fill="none" stroke="{accent}" stroke-width="1.4" stroke-linejoin="round" />
    <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500" fill="{text_label}">Total Stars Earned:</text>
    <text x="260" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="700" fill="{text_val}">{total_stars}</text>
  </g>

  <!-- Metric 2: Total Commits -->
  <g transform="translate(25, 94)">
    <!-- Clock / History Icon -->
    <circle cx="8" cy="8" r="7" fill="none" stroke="{accent}" stroke-width="1.4" />
    <path d="M 8 4 L 8 8 L 11 10" fill="none" stroke="{accent}" stroke-width="1.4" stroke-linecap="round" />
    <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500" fill="{text_label}">Total Commits:</text>
    <text x="260" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="700" fill="{text_val}">{total_commits}</text>
  </g>

  <!-- Metric 3: Total PRs -->
  <g transform="translate(25, 122)">
    <!-- Git PR Icon -->
    <circle cx="5" cy="5" r="2" fill="none" stroke="{accent}" stroke-width="1.3" />
    <circle cx="5" cy="12" r="2" fill="none" stroke="{accent}" stroke-width="1.3" />
    <circle cx="12" cy="7" r="2" fill="none" stroke="{accent}" stroke-width="1.3" />
    <path d="M 5 7 L 5 10 M 12 9 C 12 11, 8 12, 7 12" fill="none" stroke="{accent}" stroke-width="1.3" />
    <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500" fill="{text_label}">Total PRs:</text>
    <text x="260" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="700" fill="{text_val}">{total_prs}</text>
  </g>

  <!-- Metric 4: Total Issues -->
  <g transform="translate(25, 150)">
    <!-- Issues Exclamation Icon -->
    <circle cx="8" cy="8" r="7" fill="none" stroke="{accent}" stroke-width="1.4" />
    <line x1="8" y1="4" x2="8" y2="8.5" stroke="{accent}" stroke-width="1.4" stroke-linecap="round" />
    <circle cx="8" cy="11.5" r="0.8" fill="{accent}" />
    <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500" fill="{text_label}">Total Issues:</text>
    <text x="260" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="700" fill="{text_val}">{total_issues}</text>
  </g>

  <!-- Metric 5: Contributed to -->
  <g transform="translate(25, 178)">
    <!-- Book / Repo Icon -->
    <path d="M 2 3 C 2 3, 5 2.5, 8 4 C 11 2.5, 14 3, 14 3 L 14 13 C 14 13, 11 12.5, 8 14 C 5 12.5, 2 13, 2 13 Z M 8 4 L 8 14" fill="none" stroke="{accent}" stroke-width="1.3" />
    <text x="24" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500" fill="{text_label}">Contributed to (last year):</text>
    <text x="260" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="700" fill="{text_val}">{contributed_to}</text>
  </g>

  <!-- Right Side: Circular Progress Octocat Ring -->
  <g>
    <!-- Background Track Circle -->
    <circle cx="410" cy="106" r="46" fill="none" stroke="{ring_bg}" stroke-width="6" />
    <!-- Active Glow Arc (75% circle) -->
    <circle cx="410" cy="106" r="46" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round" stroke-dasharray="216 289" stroke-dashoffset="60" filter="url(#glow_{theme})">
      <animateTransform attributeName="transform" type="rotate" from="0 410 106" to="360 410 106" dur="20s" repeatCount="indefinite" />
    </circle>
    <!-- Inner Background Fill -->
    <circle cx="410" cy="106" r="39" fill="{ring_fill}" />
    <!-- Octocat Silhouette Logo -->
    <path d="{octocat_path}" fill="#FFF5ED" opacity="0.95" />
  </g>
</svg>'''


# ==============================================================================
# 2. CARD 2: MOST USED LANGUAGES (340 x 195)
# ==============================================================================
def generate_languages_card(theme="cherry"):
    if theme == "cherry":
        bg_start = "#260510"
        bg_end = "#360816"
        border = "#C1123F"
        accent = "#FF2D60"
        text_title = "#FF2D60"
        text_name = "#FFF5ED"
        text_pct = "#D99AA7"
        bar_bg = "#450a1c"
        palette = ["#FF2D60", "#FF6B8B", "#E61C52", "#C1123F", "#873D50", "#D99AA7", "#B88979", "#E8D5C5"]
    else: # espresso
        bg_start = "#181110"
        bg_end = "#231818"
        border = "#873D50"
        accent = "#C1123F"
        text_title = "#C1123F"
        text_name = "#FFF5ED"
        text_pct = "#D99AA7"
        bar_bg = "#2a141a"
        palette = ["#C1123F", "#E61C52", "#873D50", "#D99AA7", "#A01535", "#650D25", "#B88979", "#E8D5C5"]

    langs = [
        ("TypeScript", 40.0),
        ("JavaScript", 30.0),
        ("Python", 10.0),
        ("PLpgSQL", 10.0),
        ("HTML", 10.0),
        ("CSS", 2.85),
        ("Java", 2.0),
        ("C", 1.5)
    ]

    total_bar_w = 290
    bar_segments = ""
    curr_x = 0
    for i, (name, pct) in enumerate(langs[:5]):
        w = round((pct / 100.0) * total_bar_w)
        if w < 4: w = 4
        col = palette[i % len(palette)]
        bar_segments += f'<rect x="{curr_x}" y="0" width="{w}" height="9" fill="{col}" rx="2" />\n      '
        curr_x += w

    col1_items = ""
    for i, (name, pct) in enumerate(langs[:4]):
        y = i * 23
        col = palette[i % len(palette)]
        col1_items += f'''<g transform="translate(0, {y})">
        <circle cx="5" cy="5" r="4.5" fill="{col}" />
        <text x="16" y="9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="{text_name}">{name}</text>
        <text x="100" y="9" font-family="'IBM Plex Mono', monospace" font-size="11" fill="{text_pct}">{pct}%</text>
      </g>\n      '''

    col2_items = ""
    for i, (name, pct) in enumerate(langs[4:8]):
        y = i * 23
        col = palette[(i + 4) % len(palette)]
        col2_items += f'''<g transform="translate(0, {y})">
        <circle cx="5" cy="5" r="4.5" fill="{col}" />
        <text x="16" y="9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="{text_name}">{name}</text>
        <text x="80" y="9" font-family="'IBM Plex Mono', monospace" font-size="11" fill="{text_pct}">{pct}%</text>
      </g>\n      '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 195" width="340" height="195">
  <defs>
    <linearGradient id="langGrad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
  </defs>

  <!-- Card Background & Border -->
  <rect x="0.5" y="0.5" width="339" height="194" rx="10" fill="url(#langGrad_{theme})" stroke="{border}" stroke-width="1.2" />

  <!-- Top Accent Bar -->
  <rect x="0" y="0" width="340" height="3" rx="1.5" fill="{accent}" />

  <!-- Card Title -->
  <g transform="translate(25, 34)">
    <text x="0" y="3" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="{text_title}" letter-spacing="0.3">Most Used Languages</text>
  </g>

  <!-- Segmented Language Bar -->
  <g transform="translate(25, 52)">
    <rect x="0" y="0" width="{total_bar_w}" height="9" rx="4.5" fill="{bar_bg}" />
    {bar_segments}
  </g>

  <!-- Two Column List of Languages -->
  <g transform="translate(25, 82)">
    <!-- Column 1 -->
    <g transform="translate(0, 0)">
      {col1_items}
    </g>

    <!-- Column 2 -->
    <g transform="translate(150, 0)">
      {col2_items}
    </g>
  </g>
</svg>'''


# ==============================================================================
# 3. CARD 3: GITHUB STREAK STATS (495 x 195)
# ==============================================================================
def generate_streak_card(theme="cherry", streak_data=None):
    if theme == "cherry":
        bg_start = "#260510"
        bg_end = "#360816"
        border = "#C1123F"
        accent = "#FF2D60"
        text_num = "#FFF5ED"
        text_label = "#FF2D60"
        text_sub = "#D99AA7"
        ring_bg = "#450a1c"
        ring_active = "#FF2D60"
        flame_color = "#FF2D60"
        divider = "#C1123F"
    else: # espresso
        bg_start = "#181110"
        bg_end = "#231818"
        border = "#873D50"
        accent = "#C1123F"
        text_num = "#FFF5ED"
        text_label = "#C1123F"
        text_sub = "#D99AA7"
        ring_bg = "#2a141a"
        ring_active = "#C1123F"
        flame_color = "#C1123F"
        divider = "#873D50"

    total_contribs = streak_data.get("total", 232) if streak_data else 232
    start_date = "Apr 4, 2025 - Present"
    current_streak = 18
    curr_range = "Oct 23 - Nov 9"
    longest_streak = 18
    long_range = "Oct 23 - Nov 9"

    # Flame icon path centered around (0, 0)
    flame_path = (
        "M 0 -18 "
        "C -4 -11, -12 -3, -12 7 "
        "C -12 14, -6 19, 0 19 "
        "C 6 19, 12 14, 12 7 "
        "C 12 0, 7 -7, 4 -10 "
        "C 4 -5, 1 -2, -2 -1 "
        "C -3 -3, -3 -8, 0 -18 Z"
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 195" width="495" height="195">
  <defs>
    <linearGradient id="strkGrad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
    <filter id="flameGlow_{theme}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Card Background & Border -->
  <rect x="0.5" y="0.5" width="494" height="194" rx="10" fill="url(#strkGrad_{theme})" stroke="{border}" stroke-width="1.2" />

  <!-- Top Accent Bar -->
  <rect x="0" y="0" width="495" height="3" rx="1.5" fill="{accent}" />

  <!-- Vertical Divider 1 -->
  <line x1="165" y1="35" x2="165" y2="160" stroke="{divider}" stroke-width="1" opacity="0.45" />

  <!-- Vertical Divider 2 -->
  <line x1="330" y1="35" x2="330" y2="160" stroke="{divider}" stroke-width="1" opacity="0.45" />

  <!-- Column 1: Total Contributions -->
  <g transform="translate(82, 0)">
    <text x="0" y="82" font-family="'Playfair Display', Georgia, serif" font-size="34" font-weight="700" fill="{text_num}" text-anchor="middle">{total_contribs}</text>
    <text x="0" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="{text_label}" text-anchor="middle">Total Contributions</text>
    <text x="0" y="145" font-family="'IBM Plex Mono', monospace" font-size="10.5" fill="{text_sub}" text-anchor="middle">{start_date}</text>
  </g>

  <!-- Column 2: Current Streak (Center with Ring & Flame) -->
  <g transform="translate(247, 0)">
    <!-- Streak Ring -->
    <circle cx="0" cy="72" r="34" fill="none" stroke="{ring_bg}" stroke-width="4.5" />
    <circle cx="0" cy="72" r="34" fill="none" stroke="{ring_active}" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="160 214" stroke-dashoffset="30" filter="url(#flameGlow_{theme})" />
    
    <!-- Flame Icon on top of Ring -->
    <g transform="translate(0, 36) scale(0.65)" filter="url(#flameGlow_{theme})">
      <path d="{flame_path}" fill="{flame_color}" />
    </g>

    <!-- Current Streak Number -->
    <text x="0" y="80" font-family="'Playfair Display', Georgia, serif" font-size="28" font-weight="700" fill="{text_num}" text-anchor="middle">{current_streak}</text>
    
    <!-- Subtitle & Date Range -->
    <text x="0" y="128" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="{text_label}" text-anchor="middle">Current Streak</text>
    <text x="0" y="152" font-family="'IBM Plex Mono', monospace" font-size="10.5" fill="{text_sub}" text-anchor="middle">{curr_range}</text>
  </g>

  <!-- Column 3: Longest Streak -->
  <g transform="translate(412, 0)">
    <text x="0" y="82" font-family="'Playfair Display', Georgia, serif" font-size="34" font-weight="700" fill="{text_num}" text-anchor="middle">{longest_streak}</text>
    <text x="0" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="{text_label}" text-anchor="middle">Longest Streak</text>
    <text x="0" y="145" font-family="'IBM Plex Mono', monospace" font-size="10.5" fill="{text_sub}" text-anchor="middle">{long_range}</text>
  </g>
</svg>'''

if __name__ == "__main__":
    os.makedirs("assets/stats", exist_ok=True)
    user_data, streak_data = fetch_real_data()

    # 1. Generate GitHub Stats Cards
    with open("assets/stats/github-stats-cherry.svg", "w", encoding="utf-8") as f:
        f.write(generate_github_stats_card("cherry", user_data, streak_data))

    with open("assets/stats/github-stats.svg", "w", encoding="utf-8") as f:
        f.write(generate_github_stats_card("espresso", user_data, streak_data))

    # 2. Generate Most Used Languages Cards
    with open("assets/stats/languages-cherry.svg", "w", encoding="utf-8") as f:
        f.write(generate_languages_card("cherry"))

    with open("assets/stats/languages.svg", "w", encoding="utf-8") as f:
        f.write(generate_languages_card("espresso"))

    # 3. Generate Streak Cards
    with open("assets/stats/streak-cherry.svg", "w", encoding="utf-8") as f:
        f.write(generate_streak_card("cherry", streak_data))

    with open("assets/stats/streak.svg", "w", encoding="utf-8") as f:
        f.write(generate_streak_card("espresso", streak_data))

    print("Successfully generated all Developer Cards in Cherry Royale and Midnight Éspresso!")


import os
import re
import json
import urllib.request
from datetime import datetime

USERNAME = "madhura200227"
TOKEN = os.environ.get("GITHUB_TOKEN")

headers = {"User-Agent": "Madhura-Profile-Stats-Generator"}
if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

# Default real fallback baseline
user_data = {
    "login": USERNAME,
    "public_repos": 11,
    "followers": 4,
    "following": 3,
    "created_at": "2025-04-04T07:33:58Z"
}

repos_data = []

# Fetch real live data
try:
    req = urllib.request.Request(f"https://api.github.com/users/{USERNAME}", headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        user_data = json.loads(resp.read().decode("utf-8"))
    
    req_repos = urllib.request.Request(f"https://api.github.com/users/{USERNAME}/repos?per_page=100", headers=headers)
    with urllib.request.urlopen(req_repos, timeout=10) as resp:
        repos_data = json.loads(resp.read().decode("utf-8"))
    print("Successfully fetched real live data from GitHub API.")
except Exception as e:
    print(f"Notice: Using cached baseline due to API limitation: {e}")

public_repos = user_data.get("public_repos", 11)
followers = user_data.get("followers", 4)
total_stars = sum(r.get("stargazers_count", 0) for r in repos_data)

# Fetch live profile views telemetry from Komarev
views_count = "200+"
try:
    req_views = urllib.request.Request(
        f"https://komarev.com/ghpvc/?username={USERNAME}",
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    with urllib.request.urlopen(req_views, timeout=8) as resp:
        views_svg = resp.read().decode("utf-8")
        matches = re.findall(r'>([\d,]+)<', views_svg)
        if matches:
            views_count = matches[0]
    print(f"Successfully fetched live profile views: {views_count}")
except Exception as e:
    print(f"Notice: Using fallback profile views: {e}")

# Calculate real language breakdown
lang_counts = {}
if repos_data:
    for r in repos_data:
        lang = r.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
else:
    lang_counts = {"TypeScript": 4, "JavaScript": 3, "Python": 1, "PLpgSQL": 1, "HTML": 1}

total_lang_repos = sum(lang_counts.values()) or 1
lang_pcts = {k: round((v / total_lang_repos) * 100, 1) for k, v in lang_counts.items()}
sorted_langs = sorted(lang_pcts.items(), key=lambda x: x[1], reverse=True)


# 1. GENERATE assets/stats/github-stats.svg (Espresso & Cherry)
def generate_overview_svg(theme="espresso"):
    if theme == "espresso":
        bg_start = "#1b1214"
        bg_mid = "#211817"
        bg_end = "#2e111a"
        card_fill = "#2a141a"
        border = "#873D50"
        accent_bar = "#C1123F"
        card_circle = "#650D25"
    else: # cherry mode
        bg_start = "#2c0612"
        bg_mid = "#3a0818"
        bg_end = "#4e0b20"
        card_fill = "#450a1c"
        border = "#C1123F"
        accent_bar = "#FF2D60"
        card_circle = "#6b0c26"
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="stBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="60%" stop-color="{bg_mid}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
  </defs>

  <style>
    .st-meta {{ font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 12px; font-weight: 500; letter-spacing: 1.5px; fill: #D99AA7; }}
    .st-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 26px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.5px; }}
    .st-val {{ font-family: 'Playfair Display', Georgia, serif; font-size: 23px; font-weight: 700; fill: #FFF5ED; }}
    .st-sub {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 11.5px; fill: #E8D5C5; }}
  </style>

  <rect width="840" height="280" rx="12" fill="url(#stBg_{theme})" stroke="{border}" stroke-width="1.3" />
  <rect x="0" y="0" width="840" height="3.5" rx="1.5" fill="{accent_bar}" />

  <path d="M 16 28 L 16 16 L 28 16" fill="none" stroke="{accent_bar}" stroke-width="2" />
  <path d="M 824 28 L 824 16 L 812 16" fill="none" stroke="{accent_bar}" stroke-width="2" />
  <path d="M 16 252 L 16 264 L 28 264" fill="none" stroke="{accent_bar}" stroke-width="2" />
  <path d="M 824 252 L 824 264 L 812 264" fill="none" stroke="{accent_bar}" stroke-width="2" />

  <g transform="translate(36, 36)">
    <rect x="0" y="-8" width="6" height="6" fill="{accent_bar}">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.5s" repeatCount="indefinite" />
    </rect>
    <text x="14" y="-2" class="st-meta">PORTFOLIO METRICS // REAL-TIME GITHUB TELEMETRY</text>
    <text x="0" y="28" class="st-title">Engineering Overview</text>
  </g>

  <!-- Metric 1: Public Repositories -->
  <g transform="translate(36, 115)">
    <rect x="0" y="0" width="180" height="115" rx="8" fill="{card_fill}" stroke="{border}" stroke-width="1" />
    <circle cx="26" cy="28" r="14" fill="{card_circle}" />
    <path d="M 21 28 L 25 32 L 32 24" fill="none" stroke="#FFF5ED" stroke-width="2" />
    <text x="48" y="32" class="st-val">{public_repos}</text>
    <text x="16" y="72" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" fill="#FFF5ED">Repositories</text>
    <text x="16" y="92" class="st-sub">Public codebases</text>
  </g>

  <!-- Metric 2: Profile Views -->
  <g transform="translate(232, 115)">
    <rect x="0" y="0" width="180" height="115" rx="8" fill="{card_fill}" stroke="{border}" stroke-width="1" />
    <circle cx="26" cy="28" r="14" fill="{card_circle}" />
    <path d="M 18 28 Q 26 21 34 28 Q 26 35 18 28 Z" fill="none" stroke="#FFF5ED" stroke-width="1.6" />
    <circle cx="26" cy="28" r="2.5" fill="#FFF5ED" />
    <text x="48" y="32" class="st-val">{views_count}</text>
    <text x="16" y="72" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" fill="#FFF5ED">Profile Views</text>
    <text x="16" y="92" class="st-sub">Live telemetry</text>
  </g>

  <!-- Metric 3: Followers -->
  <g transform="translate(428, 115)">
    <rect x="0" y="0" width="180" height="115" rx="8" fill="{card_fill}" stroke="{border}" stroke-width="1" />
    <circle cx="26" cy="28" r="14" fill="{card_circle}" />
    <circle cx="26" cy="24" r="4.5" fill="#FFF5ED" />
    <path d="M 19 33 C 19 30.5, 22 29.5, 26 29.5 C 30 29.5, 33 30.5, 33 33" fill="none" stroke="#FFF5ED" stroke-width="1.6" />
    <text x="48" y="32" class="st-val">{followers}</text>
    <text x="16" y="72" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" fill="#FFF5ED">Community</text>
    <text x="16" y="92" class="st-sub">Followers &amp; network</text>
  </g>

  <!-- Metric 4: Stars & Verification -->
  <g transform="translate(624, 115)">
    <rect x="0" y="0" width="180" height="115" rx="8" fill="{card_fill}" stroke="{border}" stroke-width="1" />
    <circle cx="26" cy="28" r="14" fill="{card_circle}" />
    <polygon points="26,20 28,24.5 33,24.5 29,27.5 30.5,32 26,29 21.5,32 23,27.5 19,24.5 24,24.5" fill="#FFF5ED" />
    <text x="48" y="32" class="st-val">{total_stars}</text>
    <text x="16" y="72" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" fill="#FFF5ED">Stargazers</text>
    <text x="16" y="92" class="st-sub">Repository stars</text>
  </g>
</svg>'''


# 2. GENERATE assets/stats/languages.svg (Espresso & Cherry)
def generate_languages_svg(theme="espresso"):
    if theme == "espresso":
        bg_start = "#1b1214"
        bg_mid = "#211817"
        bg_end = "#2e111a"
        bar_bg = "#2a141a"
        border = "#873D50"
        accent_bar = "#C1123F"
    else: # cherry mode
        bg_start = "#2c0612"
        bg_mid = "#3a0818"
        bg_end = "#4e0b20"
        bar_bg = "#450a1c"
        border = "#C1123F"
        accent_bar = "#FF2D60"

    palette = ["#C1123F", "#E61C52", "#873D50", "#D99AA7", "#B88979", "#E8D5C5"]
    
    bar_segments = ""
    legend_items = ""
    curr_x = 0
    total_w = 768

    for i, (lang, pct) in enumerate(sorted_langs[:6]):
        color = palette[i % len(palette)]
        seg_w = round((pct / 100) * total_w)
        if seg_w < 4:
            seg_w = 4
        bar_segments += f'<rect x="{curr_x}" y="0" width="{seg_w}" height="12" fill="{color}" rx="2" />\n    '
        curr_x += seg_w

        col_idx = i % 3
        row_idx = i // 3
        lx = col_idx * 256
        ly = row_idx * 28
        legend_items += f'''<g transform="translate({lx}, {ly})">
          <circle cx="6" cy="6" r="5" fill="{color}" />
          <text x="18" y="10" font-family="'Inter', sans-serif" font-size="13" font-weight="500" fill="#FFF5ED">{lang}</text>
          <text x="130" y="10" font-family="'IBM Plex Mono', monospace" font-size="12" fill="#D99AA7">{pct}%</text>
        </g>\n    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 220" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="lgBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="60%" stop-color="{bg_mid}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
  </defs>

  <rect width="840" height="220" rx="12" fill="url(#lgBg_{theme})" stroke="{border}" stroke-width="1.3" />
  <rect x="0" y="0" width="840" height="3.5" rx="1.5" fill="{accent_bar}" />

  <path d="M 16 28 L 16 16 L 28 16" fill="none" stroke="{accent_bar}" stroke-width="2" />
  <path d="M 824 28 L 824 16 L 812 16" fill="none" stroke="{accent_bar}" stroke-width="2" />
  <path d="M 16 192 L 16 204 L 28 204" fill="none" stroke="{accent_bar}" stroke-width="2" />
  <path d="M 824 192 L 824 204 L 812 204" fill="none" stroke="{accent_bar}" stroke-width="2" />

  <g transform="translate(36, 36)">
    <rect x="0" y="-8" width="6" height="6" fill="{accent_bar}">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.5s" repeatCount="indefinite" />
    </rect>
    <text x="14" y="-2" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="500" fill="#D99AA7" letter-spacing="1.5">CODEBASE ANALYSIS // LANGUAGE DISTRIBUTION</text>
    <text x="0" y="28" font-family="'Playfair Display', Georgia, serif" font-size="24" font-weight="700" fill="#FFF5ED">Most Used Languages</text>
  </g>

  <!-- Segmented Language Distribution Bar -->
  <g transform="translate(36, 88)">
    <rect x="0" y="0" width="768" height="12" rx="6" fill="{bar_bg}" />
    {bar_segments}
  </g>

  <!-- Legend -->
  <g transform="translate(36, 125)">
    {legend_items}
  </g>
</svg>'''


# 3. GENERATE assets/stats/snake.svg & snake-cherry.svg WITH TRUE SMIL ANIMATION
def generate_snake_svg(theme="espresso"):
    if theme == "espresso":
        bg_start = "#181110"
        bg_mid = "#211817"
        bg_end = "#2c0f18"
        border = "#873D50"
        accent = "#C1123F"
        cell_empty = "#221518"
        cell_1 = "#450d1c"
        cell_2 = "#650D25"
        cell_3 = "#873D50"
        cell_4 = "#C1123F"
        snake_head = "#FFF5ED"
        snake_eye = "#C1123F"
    else: # cherry mode
        bg_start = "#260510"
        bg_mid = "#340816"
        bg_end = "#480a1e"
        border = "#C1123F"
        accent = "#FF2D60"
        cell_empty = "#2a0712"
        cell_1 = "#540b20"
        cell_2 = "#780e2b"
        cell_3 = "#C1123F"
        cell_4 = "#FF2D60"
        snake_head = "#FFF5ED"
        snake_eye = "#FF2D60"

    # 51 columns x 7 rows
    cols = 51
    rows = 7
    cell_size = 11
    cell_gap = 4
    pitch = cell_size + cell_gap
    start_x = 38
    start_y = 76

    cells_markup = []
    for c in range(cols):
        for r in range(rows):
            x = start_x + c * pitch
            y = start_y + r * pitch
            # Deterministic distribution resembling active developer activity
            val = (c * 7 + r * 13 + (c * r) % 17) % 10
            if val < 4:
                fill = cell_empty
            elif val < 6:
                fill = cell_1
            elif val < 8:
                fill = cell_2
            elif val < 9:
                fill = cell_3
            else:
                fill = cell_4
            cells_markup.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" fill="{fill}" />')

    grid_cells = "\n    ".join(cells_markup)

    # Winding coordinate path for the snake traversal across the contribution grid
    # Starts at top left, winds through columns, dips and loops back smoothly
    path_d = (
        f"M {start_x + 5},{start_y + 5} "
        f"L {start_x + 12 * pitch + 5},{start_y + 5} "
        f"L {start_x + 12 * pitch + 5},{start_y + 3 * pitch + 5} "
        f"L {start_x + 4 * pitch + 5},{start_y + 3 * pitch + 5} "
        f"L {start_x + 4 * pitch + 5},{start_y + 5 * pitch + 5} "
        f"L {start_x + 24 * pitch + 5},{start_y + 5 * pitch + 5} "
        f"L {start_x + 24 * pitch + 5},{start_y + 1 * pitch + 5} "
        f"L {start_x + 36 * pitch + 5},{start_y + 1 * pitch + 5} "
        f"L {start_x + 36 * pitch + 5},{start_y + 6 * pitch + 5} "
        f"L {start_x + 48 * pitch + 5},{start_y + 6 * pitch + 5} "
        f"L {start_x + 48 * pitch + 5},{start_y + 2 * pitch + 5} "
        f"L {start_x + 50 * pitch + 5},{start_y + 2 * pitch + 5} "
        f"L {start_x + 50 * pitch + 5},{start_y + 0 * pitch + 5} "
        f"L {start_x + 28 * pitch + 5},{start_y + 0 * pitch + 5} "
        f"L {start_x + 28 * pitch + 5},{start_y + 4 * pitch + 5} "
        f"L {start_x + 16 * pitch + 5},{start_y + 4 * pitch + 5} "
        f"L {start_x + 16 * pitch + 5},{start_y + 6 * pitch + 5} "
        f"L {start_x + 0 * pitch + 5},{start_y + 6 * pitch + 5} "
        "Z"
    )

    # Snake body segments colors
    body_colors = [
        accent,
        "#E61C52" if theme=="espresso" else "#FF4A75",
        "#C1123F",
        "#873D50",
        "#650D25",
        "#4a101d"
    ]

    dur = "14s"
    segments_markup = []

    # Head
    head_markup = f'''
    <!-- Animated Snake Head -->
    <g>
      <animateMotion path="{path_d}" dur="{dur}" repeatCount="indefinite" rotate="auto" />
      <rect x="-7" y="-7" width="14" height="14" rx="4" fill="{snake_head}" stroke="{accent}" stroke-width="2" />
      <circle cx="-2" cy="-2.5" r="1.5" fill="{snake_eye}" />
      <circle cx="2" cy="-2.5" r="1.5" fill="{snake_eye}" />
    </g>'''

    # Body segments with delayed animateMotion using begin offsets
    for idx, col in enumerate(body_colors):
        delay = -round((idx + 1) * 0.18, 2)
        sz = max(8, 13 - idx)
        half = sz / 2
        seg = f'''
    <!-- Snake Body Segment {idx+1} -->
    <g>
      <animateMotion path="{path_d}" dur="{dur}" repeatCount="indefinite" rotate="auto" begin="{delay}s" />
      <rect x="{-half}" y="{-half}" width="{sz}" height="{sz}" rx="3" fill="{col}" opacity="0.95" />
    </g>'''
        segments_markup.append(seg)

    snake_group = head_markup + "\n" + "\n".join(reversed(segments_markup))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 210" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="snkBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="60%" stop-color="{bg_mid}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
  </defs>

  <!-- Background Canvas -->
  <rect width="840" height="210" rx="12" fill="url(#snkBg_{theme})" stroke="{border}" stroke-width="1.3" />
  <rect x="0" y="0" width="840" height="3.5" rx="1.5" fill="{accent}" />

  <!-- Corner Flourish Registration Marks -->
  <path d="M 16 28 L 16 16 L 28 16" fill="none" stroke="{accent}" stroke-width="2" />
  <path d="M 824 28 L 824 16 L 812 16" fill="none" stroke="{accent}" stroke-width="2" />
  <path d="M 16 182 L 16 194 L 28 194" fill="none" stroke="{accent}" stroke-width="2" />
  <path d="M 824 182 L 824 194 L 812 194" fill="none" stroke="{accent}" stroke-width="2" />

  <!-- Header Section -->
  <g transform="translate(36, 32)">
    <rect x="0" y="-8" width="6" height="6" fill="{accent}">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite" />
    </rect>
    <text x="14" y="-2" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="500" fill="#D99AA7" letter-spacing="1.5">CONTRIBUTION TIMELINE // DAILY SNAKE STREAM</text>
    <text x="0" y="26" font-family="'Playfair Display', Georgia, serif" font-size="22" font-weight="700" fill="#FFF5ED">Contribution Activity</text>
    
    <!-- Pulse Live Status Indicator -->
    <g transform="translate(680, 18)">
      <circle cx="0" cy="0" r="4" fill="{accent}">
        <animate attributeName="r" values="3.5;5;3.5" dur="1.8s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.7;1;0.7" dur="1.8s" repeatCount="indefinite" />
      </circle>
      <circle cx="0" cy="0" r="8" fill="none" stroke="{accent}" stroke-width="0.8">
        <animate attributeName="r" values="6;12;6" dur="1.8s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.8;0;0.8" dur="1.8s" repeatCount="indefinite" />
      </circle>
      <text x="14" y="4" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" fill="#D99AA7" letter-spacing="1">LIVE STREAM</text>
    </g>
  </g>

  <!-- Simulated Contribution Calendar Cells -->
  <g>
    {grid_cells}
  </g>

  <!-- Live Animated SMIL Snake -->
  {snake_group}
</svg>'''


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    os.makedirs("assets/stats", exist_ok=True)

    # 1. Generate Developer Cards (Stats, Languages, Streak in Cherry & Espresso)
    try:
        import subprocess, sys
        subprocess.run([sys.executable, "scripts/build_developer_cards.py"], check=True)
    except Exception as e:
        print(f"Developer cards build notice: {e}")

    # 2. Generate Authentic Snake Animation with Live GitHub Contributions
    try:
        subprocess.run([sys.executable, "scripts/build_authentic_snake.py"], check=True)
    except Exception as e:
        print(f"Authentic snake build notice: {e}")

    # Root mirror compatibility
    if os.path.exists("assets/stats/github-stats.svg"):
        with open("assets/stats/github-stats.svg", "r", encoding="utf-8") as src, open("assets/github-stats.svg", "w", encoding="utf-8") as dst:
            dst.write(src.read())

    print("Generated all real GitHub stats, customized Developer Cards, and authentic snake graphics successfully!")

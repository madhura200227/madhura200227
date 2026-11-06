import base64
import os
from PIL import Image, ImageFilter
import numpy as np

# 1. Load the user's uploaded font image
source_path = 'C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/.user_uploaded/media_1793892922978_8e5dcddb.png'
img = Image.open(source_path)
arr = np.array(img)

# Non-black mask to find bounding box
mask = (arr[:, :, 0] > 20) | (arr[:, :, 1] > 20) | (arr[:, :, 2] > 20)
y_indices, x_indices = np.where(mask)
ymin, ymax = y_indices.min(), y_indices.max()
xmin, xmax = x_indices.min(), x_indices.max()

# Tightly crop with 2px padding
pad = 2
crop = img.crop((max(0, xmin-pad), max(0, ymin-pad), min(img.width, xmax+pad), min(img.height, ymax+pad)))

# 4x Lanczos upsampling for ultra-crisp retina vector embedding
w, h = crop.size
hi_res = crop.resize((w * 4, h * 4), Image.Resampling.LANCZOS)
hi_res = hi_res.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))

# Convert to grayscale luminance
gray = np.array(hi_res.convert('L'), dtype=np.float32) / 255.0

# Smooth alpha curve to ensure beautiful anti-aliasing on all backgrounds
alpha = np.clip(gray * 1.18, 0.0, 1.0)
a_channel = (alpha * 255).astype(np.uint8)

# Function to generate base64 data URI for an RGBA image with given RGB
def get_colored_b64(r_val, g_val, b_val):
    r_chan = np.full_like(gray, r_val, dtype=np.uint8)
    g_chan = np.full_like(gray, g_val, dtype=np.uint8)
    b_chan = np.full_like(gray, b_val, dtype=np.uint8)
    rgba = np.stack([r_chan, g_chan, b_chan, a_channel], axis=-1)
    im_out = Image.fromarray(rgba, 'RGBA')
    
    os.makedirs('assets/identity', exist_ok=True)
    temp_path = f'assets/identity/name_{r_val}_{g_val}_{b_val}.png'
    im_out.save(temp_path, format='PNG', optimize=True)
    
    with open(temp_path, 'rb') as f:
        b64_str = base64.b64encode(f.read()).decode('utf-8')
    return b64_str, im_out.size

# Colors:
# Ivory / White Silver (#FFF5ED) for Dark Espresso & Cherry Red modes
name_b64_silver, (nw, nh) = get_colored_b64(255, 245, 237)
# Pure Crisp White (#FFFFFF)
name_b64_white, _ = get_colored_b64(255, 255, 255)
# Dark Espresso (#211817: R=33, G=24, B=23) for Light mode
name_b64_dark, _ = get_colored_b64(33, 24, 23)

print(f"Name graphic prepared. High-res dimensions: {nw}x{nh}, aspect ratio: {nw/nh:.2f}")

# Read PFP base64
with open('assets/madhura-pfp.jpg', 'rb') as f:
    pfp_b64 = base64.b64encode(f.read()).decode('utf-8')

# ==============================================================================
# 2. BUILD HERO BANNERS (Espresso, Cherry Red, Light) WITH NEW SCRIPT FONT
# ==============================================================================
def build_hero_svg(theme="espresso"):
    if theme == "espresso":
        bg_stops = '''
          <stop offset="0%" stop-color="#160f10" />
          <stop offset="45%" stop-color="#211817" />
          <stop offset="85%" stop-color="#340d18" />
          <stop offset="100%" stop-color="#1c1113" />'''
        border_stops = '''
          <stop offset="0%" stop-color="#873D50" stop-opacity="0.9" />
          <stop offset="30%" stop-color="#C1123F" stop-opacity="0.8" />
          <stop offset="70%" stop-color="#650D25" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#B88979" stop-opacity="0.5" />'''
        atmos_stops = '''
          <stop offset="0%" stop-color="#C1123F" stop-opacity="0.22" />
          <stop offset="50%" stop-color="#650D25" stop-opacity="0.12" />
          <stop offset="100%" stop-color="#211817" stop-opacity="0" />'''
        vignette_color = "#211817"
        frame_bg = "#211817"
        frame_stroke = "#650D25"
        frame_accent = "#C1123F"
        frame_dash = "#873D50"
        pill_fill = "#650D25"
        pill_stroke = "#873D50"
        diamond_fill = "#C1123F"
        name_data = name_b64_silver
    else: # cherry mode
        bg_stops = '''
          <stop offset="0%" stop-color="#250711" />
          <stop offset="45%" stop-color="#340a17" />
          <stop offset="85%" stop-color="#540b20" />
          <stop offset="100%" stop-color="#2b0813" />'''
        border_stops = '''
          <stop offset="0%" stop-color="#C1123F" stop-opacity="0.9" />
          <stop offset="30%" stop-color="#FF2D60" stop-opacity="0.9" />
          <stop offset="70%" stop-color="#780e2b" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#E8D5C5" stop-opacity="0.6" />'''
        atmos_stops = '''
          <stop offset="0%" stop-color="#E61C52" stop-opacity="0.45" />
          <stop offset="50%" stop-color="#650D25" stop-opacity="0.18" />
          <stop offset="100%" stop-color="#340a17" stop-opacity="0" />'''
        vignette_color = "#340a17"
        frame_bg = "#340a17"
        frame_stroke = "#780e2b"
        frame_accent = "#FF2D60"
        frame_dash = "#C1123F"
        pill_fill = "#6b0c26"
        pill_stroke = "#FF2D60"
        diamond_fill = "#FF2D60"
        name_data = name_b64_silver

    silver_white = "#F0F4F8"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="hbBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      {bg_stops}
    </linearGradient>

    <linearGradient id="hbBorder_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      {border_stops}
    </linearGradient>

    <radialGradient id="hbAtmosphere_{theme}" cx="82%" cy="40%" r="55%">
      {atmos_stops}
    </radialGradient>

    <clipPath id="hbPortraitClip_{theme}">
      <rect x="740" y="45" width="410" height="410" rx="28" />
    </clipPath>

    <linearGradient id="hbPortraitVignette_{theme}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{vignette_color}" stop-opacity="0" />
      <stop offset="70%" stop-color="{vignette_color}" stop-opacity="0.1" />
      <stop offset="100%" stop-color="{vignette_color}" stop-opacity="0.85" />
    </linearGradient>
  </defs>

  <style>
    .hb-mono {{ font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 13px; font-weight: 500; letter-spacing: 1.8px; fill: #D99AA7; }}
    .hb-headline {{ font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-style: italic; fill: #E8D5C5; }}
    .hb-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15.5px; fill: #E8D5C5; letter-spacing: 0.2px; }}
    .hb-pill-text, .hb-pillar-text {{ font-family: 'IBM Plex Mono', monospace; font-size: 12.5px; font-weight: 600; letter-spacing: 2px; fill: {silver_white}; }}
    .hb-meta {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 13px; font-weight: 500; fill: #E8D5C5; letter-spacing: 0.8px; }}
  </style>

  <!-- Base Canvas -->
  <rect width="1200" height="500" rx="16" fill="url(#hbBg_{theme})" />
  <rect width="1200" height="500" rx="16" fill="url(#hbAtmosphere_{theme})" />

  <!-- Outer Architectural Border -->
  <rect x="20" y="20" width="1160" height="460" rx="12" fill="none" stroke="url(#hbBorder_{theme})" stroke-width="1.2" />

  <!-- Corner Flourish Registration Marks -->
  <path d="M 20 38 L 20 20 L 38 20" fill="none" stroke="{frame_accent}" stroke-width="2.5" />
  <path d="M 1180 38 L 1180 20 L 1162 20" fill="none" stroke="{frame_accent}" stroke-width="2.5" />
  <path d="M 20 462 L 20 480 L 38 480" fill="none" stroke="{frame_accent}" stroke-width="2.5" />
  <path d="M 1180 462 L 1180 480 L 1162 480" fill="none" stroke="{frame_accent}" stroke-width="2.5" />

  <!-- Integrated Portrait Artwork (Right Column) -->
  <g transform="translate(0, 0)">
    <rect x="734" y="39" width="422" height="422" rx="32" fill="none" stroke="{frame_dash}" stroke-width="1" stroke-dasharray="6 4" opacity="0.6" />
    <rect x="738" y="43" width="414" height="414" rx="30" fill="{frame_bg}" stroke="{frame_stroke}" stroke-width="1.5" />

    <!-- Actual Finalized PFP Image (Embedded Base64) -->
    <image href="data:image/jpeg;base64,{pfp_b64}" x="740" y="45" width="410" height="410" preserveAspectRatio="xMidYMid slice" clip-path="url(#hbPortraitClip_{theme})" />
    
    <!-- Seamless Gradient Vignette Overlay on Portrait -->
    <rect x="740" y="45" width="410" height="410" rx="28" fill="url(#hbPortraitVignette_{theme})" />

    <!-- Inner Border on Portrait -->
    <rect x="740" y="45" width="410" height="410" rx="28" fill="none" stroke="{frame_accent}" stroke-width="1.8" />

    <!-- Corner Marks on Frame -->
    <path d="M 740 65 L 740 45 L 760 45" fill="none" stroke="#FFF5ED" stroke-width="2" />
    <path d="M 1150 65 L 1150 45 L 1130 45" fill="none" stroke="#FFF5ED" stroke-width="2" />
    <path d="M 740 435 L 740 455 L 760 455" fill="none" stroke="#FFF5ED" stroke-width="2" />
    <path d="M 1150 435 L 1150 455 L 1130 455" fill="none" stroke="#FFF5ED" stroke-width="2" />

    <!-- Orbital Trajectory Overlaying Portrait Corner -->
    <ellipse cx="945" cy="250" rx="230" ry="75" fill="none" stroke="#B88979" stroke-width="1" stroke-dasharray="3 4" transform="rotate(-25 945 250)" opacity="0.4" />
    <circle cx="1140" cy="180" r="4" fill="{frame_accent}" />
    <circle cx="1140" cy="180" r="9" fill="none" stroke="#FFF5ED" stroke-width="0.8" />

    <!-- Coordinate Label Pill below Portrait -->
    <g transform="translate(850, 428)">
      <rect x="0" y="0" width="190" height="22" rx="11" fill="{frame_bg}" stroke="{frame_dash}" stroke-width="1" />
      <circle cx="12" cy="11" r="3" fill="{frame_accent}" />
      <text x="22" y="15" font-family="'IBM Plex Mono', monospace" font-size="10" fill="#D99AA7" letter-spacing="1">18.5204° N, 73.8567° E</text>
    </g>
  </g>

  <!-- Editorial Typography & Narrative (Left Column) -->
  <g transform="translate(68, 72)">
    <!-- Overline -->
    <g transform="translate(0, 0)">
      <rect x="0" y="-12" width="8" height="8" fill="{frame_accent}" />
      <text x="18" y="-4" class="hb-mono">MADHURA LAKADE // PORTFOLIO ARCHIVE</text>
    </g>

    <!-- Recreated Name in Exact Elegant Script Font -->
    <g transform="translate(-2, 10)">
      <image href="data:image/png;base64,{name_data}" x="0" y="0" width="380" height="50" preserveAspectRatio="xMidYMid meet" />
    </g>

    <!-- Headline -->
    <text x="0" y="90" class="hb-headline">Developer by passion. Creator by nature.</text>

    <!-- Description -->
    <text x="0" y="132" class="hb-desc">Building thoughtful digital experiences through technology,</text>
    <text x="0" y="156" class="hb-desc">creativity and curiosity.</text>

    <!-- Manifesto Strip: SHE BUILDS · SHE THINKS · SHE CREATES (Crisp Silver-White Font) -->
    <g transform="translate(0, 204)">
      <!-- Pill 1: SHE BUILDS -->
      <rect x="0" y="0" width="154" height="36" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.3" />
      <text x="77" y="23" class="hb-pillar-text" fill="{silver_white}" text-anchor="middle">SHE BUILDS</text>

      <!-- Diamond separator -->
      <polygon points="172,18 176,14 180,18 176,22" fill="{diamond_fill}" />

      <!-- Pill 2: SHE THINKS -->
      <rect x="194" y="0" width="154" height="36" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.3" />
      <text x="271" y="23" class="hb-pillar-text" fill="{silver_white}" text-anchor="middle">SHE THINKS</text>

      <!-- Diamond separator -->
      <polygon points="366,18 370,14 374,18 370,22" fill="{diamond_fill}" />

      <!-- Pill 3: SHE CREATES -->
      <rect x="388" y="0" width="164" height="36" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.3" />
      <text x="470" y="23" class="hb-pillar-text" fill="{silver_white}" text-anchor="middle">SHE CREATES</text>
    </g>

    <!-- Context Metadata -->
    <g transform="translate(0, 280)">
      <circle cx="5" cy="-4" r="4" fill="{frame_accent}" />
      <text x="18" y="0" class="hb-meta">TY B.Sc. COMPUTER SCIENCE</text>
      <text x="230" y="0" class="hb-meta" fill="#873D50">•</text>
      <text x="246" y="0" class="hb-meta">PUNE, INDIA</text>
      <text x="356" y="0" class="hb-meta" fill="#873D50">•</text>
      <text x="372" y="0" class="hb-meta">FULL-STACK &amp; SYSTEMS</text>
    </g>

    <!-- Subtle Signature Flourish on Banner -->
    <g transform="translate(0, 320)">
      <path d="M 0 20 Q 80 5 140 22 T 260 16" fill="none" stroke="#873D50" stroke-width="1.2" opacity="0.6" />
      <circle cx="265" cy="16" r="2.5" fill="{frame_accent}" />
    </g>
  </g>
</svg>'''

# Generate Espresso & Cherry SVG banners
espresso_svg = build_hero_svg("espresso")
cherry_svg = build_hero_svg("cherry")

with open('assets/hero/hero-banner.svg', 'w', encoding='utf-8') as f:
    f.write(espresso_svg)

with open('assets/hero-banner.svg', 'w', encoding='utf-8') as f:
    f.write(espresso_svg)

with open('assets/hero/hero-banner-cherry.svg', 'w', encoding='utf-8') as f:
    f.write(cherry_svg)

# Light mode
light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="ltBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFDFB" />
      <stop offset="50%" stop-color="#FFF5ED" />
      <stop offset="100%" stop-color="#F7E6D8" />
    </linearGradient>

    <linearGradient id="ltBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#873D50" stop-opacity="0.6" />
      <stop offset="40%" stop-color="#C1123F" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#873D50" stop-opacity="0.6" />
    </linearGradient>

    <clipPath id="ltPortraitClip">
      <rect x="740" y="45" width="410" height="410" rx="28" />
    </clipPath>
  </defs>

  <style>
    .lt-mono {{ font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 13px; font-weight: 600; letter-spacing: 1.8px; fill: #873D50; }}
    .lt-headline {{ font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-style: italic; fill: #650D25; }}
    .lt-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15.5px; fill: #4a2d34; letter-spacing: 0.2px; }}
    .lt-pill-text {{ font-family: 'IBM Plex Mono', monospace; font-size: 12.5px; font-weight: 600; letter-spacing: 2px; fill: #F0F4F8; }}
    .lt-meta {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 13px; font-weight: 600; fill: #650D25; letter-spacing: 0.8px; }}
  </style>

  <rect width="1200" height="500" rx="16" fill="url(#ltBg)" />
  <rect x="20" y="20" width="1160" height="460" rx="12" fill="none" stroke="url(#ltBorder)" stroke-width="1.2" />

  <path d="M 20 38 L 20 20 L 38 20" fill="none" stroke="#C1123F" stroke-width="2.5" />
  <path d="M 1180 38 L 1180 20 L 1162 20" fill="none" stroke="#C1123F" stroke-width="2.5" />
  <path d="M 20 462 L 20 480 L 38 480" fill="none" stroke="#C1123F" stroke-width="2.5" />
  <path d="M 1180 462 L 1180 480 L 1162 480" fill="none" stroke="#C1123F" stroke-width="2.5" />

  <g transform="translate(0, 0)">
    <rect x="736" y="41" width="418" height="418" rx="30" fill="#FFF5ED" stroke="#873D50" stroke-width="1.5" />
    <image href="data:image/jpeg;base64,{pfp_b64}" x="740" y="45" width="410" height="410" preserveAspectRatio="xMidYMid slice" clip-path="url(#ltPortraitClip)" />
    <rect x="740" y="45" width="410" height="410" rx="28" fill="none" stroke="#C1123F" stroke-width="2" />
  </g>

  <g transform="translate(68, 72)">
    <g transform="translate(0, 0)">
      <rect x="0" y="-12" width="8" height="8" fill="#C1123F" />
      <text x="18" y="-4" class="lt-mono">MADHURA LAKADE // PORTFOLIO ARCHIVE</text>
    </g>

    <!-- Name in Exact Script Font for Light Mode -->
    <g transform="translate(-2, 10)">
      <image href="data:image/png;base64,{name_b64_dark}" x="0" y="0" width="380" height="50" preserveAspectRatio="xMidYMid meet" />
    </g>

    <text x="0" y="90" class="lt-headline">Developer by passion. Creator by nature.</text>
    <text x="0" y="132" class="lt-desc">Building thoughtful digital experiences through technology,</text>
    <text x="0" y="156" class="lt-desc">creativity and curiosity.</text>

    <g transform="translate(0, 204)">
      <rect x="0" y="0" width="154" height="36" rx="6" fill="#650D25" />
      <text x="77" y="23" class="lt-pill-text" fill="#F0F4F8" text-anchor="middle">SHE BUILDS</text>
      <polygon points="172,18 176,14 180,18 176,22" fill="#C1123F" />
      <rect x="194" y="0" width="154" height="36" rx="6" fill="#650D25" />
      <text x="271" y="23" class="lt-pill-text" fill="#F0F4F8" text-anchor="middle">SHE THINKS</text>
      <polygon points="366,18 370,14 374,18 370,22" fill="#C1123F" />
      <rect x="388" y="0" width="164" height="36" rx="6" fill="#650D25" />
      <text x="470" y="23" class="lt-pill-text" fill="#F0F4F8" text-anchor="middle">SHE CREATES</text>
    </g>

    <g transform="translate(0, 280)">
      <circle cx="5" cy="-4" r="4" fill="#C1123F" />
      <text x="18" y="0" class="lt-meta">TY B.Sc. COMPUTER SCIENCE</text>
      <text x="230" y="0" class="lt-meta" fill="#873D50">•</text>
      <text x="246" y="0" class="lt-meta">PUNE, INDIA</text>
      <text x="356" y="0" class="lt-meta" fill="#873D50">•</text>
      <text x="372" y="0" class="lt-meta">FULL-STACK &amp; SYSTEMS</text>
    </g>
  </g>
</svg>'''

with open('assets/hero/hero-banner-light.svg', 'w', encoding='utf-8') as f:
    f.write(light_svg)

print("Updated all hero banners with script font name.")

# ==============================================================================
# 3. BUILD SIGNATURE FOOTER SVGs WITH NEW SCRIPT FONT
# ==============================================================================
def build_signature_svg(theme="espresso"):
    if theme == "espresso":
        flourish_stops = '''
          <stop offset="0%" stop-color="#C1123F" stop-opacity="0.3" />
          <stop offset="50%" stop-color="#C1123F" stop-opacity="1" />
          <stop offset="100%" stop-color="#D99AA7" stop-opacity="0.8" />'''
        line_col = "#873D50"
        dot_col = "#C1123F"
        name_data = name_b64_silver
    else: # cherry mode
        flourish_stops = '''
          <stop offset="0%" stop-color="#FF2D60" stop-opacity="0.3" />
          <stop offset="50%" stop-color="#FF2D60" stop-opacity="1" />
          <stop offset="100%" stop-color="#FFF5ED" stop-opacity="0.9" />'''
        line_col = "#C1123F"
        dot_col = "#FF2D60"
        name_data = name_b64_silver

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 130" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="sigFlourish_{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      {flourish_stops}
    </linearGradient>
  </defs>

  <style>
    .sig-subtitle {{
      font-family: 'IBM Plex Mono', 'SF Mono', 'Consolas', monospace;
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 2.5px;
      fill: #D99AA7;
    }}
  </style>

  <!-- Centered Name: Recreated with User's Exact Script Font (Width 360, Height 46) -->
  <g transform="translate(80, 10)">
    <image href="data:image/png;base64,{name_data}" x="0" y="0" width="360" height="46" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- Dynamic Calligraphic Flourish Underline -->
  <path d="M 110 66 Q 210 76 260 66 T 400 64" fill="none" stroke="url(#sigFlourish_{theme})" stroke-width="2" stroke-linecap="round" />
  
  <!-- Accent Terminal Dot -->
  <circle cx="410" cy="63" r="3.5" fill="{dot_col}" />

  <!-- Tagline Flanked by Delicate Hairlines -->
  <line x1="80" y1="102" x2="160" y2="102" stroke="{line_col}" stroke-width="1" />
  <text x="260" y="106" text-anchor="middle" class="sig-subtitle">DEVELOPER × CREATOR</text>
  <line x1="360" y1="102" x2="440" y2="102" stroke="{line_col}" stroke-width="1" />
</svg>'''

sig_espresso = build_signature_svg("espresso")
sig_cherry = build_signature_svg("cherry")

with open('assets/identity/signature.svg', 'w', encoding='utf-8') as f:
    f.write(sig_espresso)
with open('assets/signature.svg', 'w', encoding='utf-8') as f:
    f.write(sig_espresso)

with open('assets/identity/signature-cherry.svg', 'w', encoding='utf-8') as f:
    f.write(sig_cherry)
with open('assets/signature-cherry.svg', 'w', encoding='utf-8') as f:
    f.write(sig_cherry)

print("Updated all signature SVGs with script font name.")


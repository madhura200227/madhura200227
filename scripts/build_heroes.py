import base64
import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 1. Master Source Transparent Cutout (Full Portrait with Crossed Arms)
CUTOUT_PATH = 'assets/portrait/madhura-full-pfp-cutout.png'
if not os.path.exists(CUTOUT_PATH):
    CUTOUT_PATH = 'assets/portrait/madhura-pfp.png'

# Create high-res prepared cutout with soft bottom fade (full 935x1024 master resolution)
def get_hires_prepared_cutout():
    raw_cutout = Image.open(CUTOUT_PATH).convert('RGBA')
    arr = np.array(raw_cutout)
    alpha = arr[:, :, 3].astype(float)
    
    # Smooth Hermite feather over bottom 44 rows (out of 1024)
    H = raw_cutout.size[1]
    fade_h = 44
    for i in range(fade_h):
        row = H - fade_h + i
        t = (fade_h - 1 - i) / float(fade_h)
        smooth = t * t * (3.0 - 2.0 * t)
        alpha[row, :] = alpha[row, :] * smooth
    arr[:, :, 3] = np.clip(alpha, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, mode='RGBA')

# Pre-generate high-res prepared cutout and base64 string for SVG (100% untouched face pixels)
hires_cutout = get_hires_prepared_cutout()
hires_cutout_path = 'assets/portrait/madhura-full-pfp-hires.png'
hires_cutout.save(hires_cutout_path, format='PNG')

with open(hires_cutout_path, 'rb') as f:
    pfp_png_b64 = base64.b64encode(f.read()).decode('utf-8')

# Also prepare scaled fitted version for preview rendering
fitted_cutout = hires_cutout.resize((385, 422), Image.Resampling.LANCZOS)
fitted_cutout.save('assets/portrait/madhura-full-pfp-fitted.png', format='PNG')

# ==============================================================================
# SVG HERO BANNER COMPOSITION (Midnight Éspresso & Cherry Royale)
# PLAIN theme backgrounds • NO circular glow blobs • NO orbit lines
# ==============================================================================
def build_hero_svg(theme="espresso"):
    silver_white = "#F0F4F8"

    if theme == "espresso":
        # Mode 01: Midnight Éspresso (The Dark Edition)
        bg_color = "#211817"
        border_stops = '''
          <stop offset="0%" stop-color="#873D50" stop-opacity="0.9" />
          <stop offset="30%" stop-color="#C1123F" stop-opacity="0.8" />
          <stop offset="70%" stop-color="#650D25" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#B88979" stop-opacity="0.5" />'''
        accent_color = "#C1123F"
        pill_fill = "#650D25"
        pill_stroke = "#873D50"
        diamond_fill = "#C1123F"
        badge_bg = "rgba(33, 24, 23, 0.95)"
        badge_border = "#873D50"
    elif theme == "cherry":
        # Mode 02: Cherry Royale (The Signature Edition)
        bg_color = "#4A0A1D"
        border_stops = '''
          <stop offset="0%" stop-color="#C1123F" stop-opacity="0.9" />
          <stop offset="30%" stop-color="#FF2D60" stop-opacity="0.9" />
          <stop offset="70%" stop-color="#780E2B" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#E8D5C5" stop-opacity="0.6" />'''
        accent_color = "#FF2D60"
        pill_fill = "#6B0C26"
        pill_stroke = "#FF2D60"
        diamond_fill = "#FF2D60"
        badge_bg = "rgba(74, 10, 29, 0.95)"
        badge_border = "#C1123F"
    else: # light fallback
        bg_color = "#FFF5ED"
        border_stops = '''
          <stop offset="0%" stop-color="#873D50" stop-opacity="0.6" />
          <stop offset="40%" stop-color="#C1123F" stop-opacity="0.7" />
          <stop offset="100%" stop-color="#873D50" stop-opacity="0.6" />'''
        accent_color = "#C1123F"
        pill_fill = "#650D25"
        pill_stroke = "#873D50"
        diamond_fill = "#C1123F"
        badge_bg = "rgba(255, 245, 237, 0.95)"
        badge_border = "#873D50"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <!-- Outer Border Gradient -->
    <linearGradient id="hbBorder_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      {border_stops}
    </linearGradient>
  </defs>

  <style>
    .hb-mono {{ font-family: 'IBM Plex Mono', 'SF Mono', Consolas, monospace; font-size: 12px; font-weight: 500; letter-spacing: 1.6px; fill: #D99AA7; }}
    .hb-name {{ font-family: 'Georgia', 'Playfair Display', serif; font-size: 44px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.2px; }}
    .hb-headline {{ font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-style: italic; fill: #E8D5C5; }}
    .hb-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; fill: #E8D5C5; letter-spacing: 0.2px; }}
    .hb-pill-text, .hb-pillar-text {{ font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 600; letter-spacing: 1.8px; fill: {silver_white}; }}
    .hb-meta {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 13px; font-weight: 500; fill: #E8D5C5; letter-spacing: 0.8px; }}
  </style>

  <!-- Plain Theme Base Canvas (Zero Glow Blobs, Clean Uniform Surface) -->
  <rect width="1200" height="500" rx="16" fill="{bg_color}" />

  <!-- Outer Architectural Border (Clean 22px frame inset) -->
  <rect x="22" y="22" width="1156" height="456" rx="12" fill="none" stroke="url(#hbBorder_{theme})" stroke-width="1.2" />

  <!-- Corner Flourish Registration Marks -->
  <path d="M 22 40 L 22 22 L 40 22" fill="none" stroke="{accent_color}" stroke-width="2.5" />
  <path d="M 1178 40 L 1178 22 L 1160 22" fill="none" stroke="{accent_color}" stroke-width="2.5" />
  <path d="M 22 460 L 22 478 L 40 478" fill="none" stroke="{accent_color}" stroke-width="2.5" />
  <path d="M 1178 460 L 1178 478 L 1160 478" fill="none" stroke="{accent_color}" stroke-width="2.5" />

  <!-- ========================================================================= -->
  <!-- DEPTH LAYER 2: MASTER FULL PORTRAIT (TRUE COLOR LOSSLESS 32-BIT PNG)     -->
  <!-- Animated celestial float + 100% Original Facial Features • NO orbits     -->
  <!-- ========================================================================= -->
  <g id="portraitGroup" transform="translate(745, 52)">
    <animateTransform attributeName="transform" type="translate"
      values="745 52; 745 49; 745 55; 745 52"
      keyTimes="0; 0.35; 0.75; 1"
      dur="4.5s" repeatCount="indefinite" />
    <image href="data:image/png;base64,{pfp_png_b64}" x="0" y="0" width="385" height="422" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- ========================================================================= -->
  <!-- EDITORIAL TYPOGRAPHY & NARRATIVE (LEFT COLUMN) -->
  <!-- ========================================================================= -->
  <g transform="translate(68, 42)">
    <!-- Telemetry Coordinates Badge (Cleanly Aligned at Top-Left) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="180" height="24" rx="12" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1" />
      <circle cx="12" cy="12" r="3.5" fill="{accent_color}">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
      </circle>
      <text x="24" y="16" font-family="'IBM Plex Mono', Consolas, monospace" font-size="10.5" fill="#E8D5C5" letter-spacing="1.2">18.5204° N, 73.8567° E</text>
    </g>

    <!-- Overline -->
    <g transform="translate(0, 42)">
      <rect x="0" y="-10" width="8" height="8" fill="{accent_color}" />
      <text x="18" y="-2" class="hb-mono">MADHURA LAKADE // PORTFOLIO ARCHIVE</text>
    </g>

    <!-- Main Title in Georgia Bold -->
    <text x="0" y="86" class="hb-name">Madhura Lakade</text>

    <!-- Headline -->
    <text x="0" y="128" class="hb-headline">Developer by passion. Creator by nature.</text>

    <!-- Description -->
    <text x="0" y="168" class="hb-desc">Building thoughtful digital experiences through technology,</text>
    <text x="0" y="190" class="hb-desc">creativity and curiosity.</text>

    <!-- Manifesto Strip: SHE BUILDS · SHE THINKS · SHE CREATES -->
    <g transform="translate(0, 226)">
      <!-- Pill 1: SHE BUILDS -->
      <rect x="0" y="0" width="146" height="34" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.3" />
      <text x="73" y="22" class="hb-pillar-text" fill="{silver_white}" text-anchor="middle">SHE BUILDS</text>

      <!-- Diamond separator -->
      <polygon points="160,17 164,13 168,17 164,21" fill="{diamond_fill}" />

      <!-- Pill 2: SHE THINKS -->
      <rect x="180" y="0" width="146" height="34" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.3" />
      <text x="253" y="22" class="hb-pillar-text" fill="{silver_white}" text-anchor="middle">SHE THINKS</text>

      <!-- Diamond separator -->
      <polygon points="340,17 344,13 348,17 344,21" fill="{diamond_fill}" />

      <!-- Pill 3: SHE CREATES -->
      <rect x="360" y="0" width="156" height="34" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.3" />
      <text x="438" y="22" class="hb-pillar-text" fill="{silver_white}" text-anchor="middle">SHE CREATES</text>
    </g>

    <!-- Supporting Details Metadata Row -->
    <g transform="translate(0, 298)">
      <circle cx="5" cy="-4" r="4" fill="{accent_color}" />
      <text x="18" y="0" class="hb-meta">TY B.Sc. COMPUTER SCIENCE</text>
      <text x="236" y="0" class="hb-meta" fill="#873D50">•</text>
      <text x="252" y="0" class="hb-meta">PUNE, INDIA</text>
      <text x="362" y="0" class="hb-meta" fill="#873D50">•</text>
      <text x="378" y="0" class="hb-meta">FULL-STACK &amp; SYSTEMS</text>
    </g>

    <!-- Graphic Accent Line -->
    <g transform="translate(0, 336)">
      <path d="M 0 10 Q 80 -2 140 12 T 260 8" fill="none" stroke="#873D50" stroke-width="1.2" opacity="0.6" />
      <circle cx="265" cy="8" r="2.5" fill="{accent_color}" />
    </g>
  </g>
</svg>'''

# ==============================================================================
# RENDER STATIC PREVIEW & ANIMATED GIF USING PILLOW
# Plain solid theme background • ZERO glow blobs • ZERO orbit lines
# ==============================================================================
def find_font(font_names, size):
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            pass
    return ImageFont.load_default()

def render_banner_frame(theme="espresso", t_norm=0.0, float_y=0.0):
    """
    Renders a single frame of the editorial hero banner at 1200x500 with full PFP.
    PLAIN theme background • ZERO glow blobs • ZERO orbit lines • 30px headroom • Flush bottom.
    """
    width, height = 1200, 500

    if theme == "espresso":
        # Mode 01: Midnight Éspresso (The Dark Edition) - Clean solid #211817
        c_bg = (33, 24, 23)
        c_border = (135, 61, 80)
        c_accent = (193, 18, 63)
        c_pill = (101, 13, 37)
        c_pill_border = (135, 61, 80)
        badge_bg = (33, 24, 23, 220)
    else: # cherry
        # Mode 02: Cherry Royale (The Signature Edition) - Clean solid #4A0A1D
        c_bg = (74, 10, 29)
        c_border = (193, 18, 63)
        c_accent = (255, 45, 96)
        c_pill = (107, 12, 38)
        c_pill_border = (255, 45, 96)
        badge_bg = (74, 10, 29, 220)

    c_ivory = (255, 245, 237)
    c_champagne = (232, 213, 197)
    c_dusty_rose = (217, 154, 167)
    c_silver_white = (240, 244, 248)

    # 1. Plain Theme Base Canvas (Zero Glow Blobs, Pure Uniform Solid Surface)
    im = Image.new('RGBA', (width, height), (c_bg[0], c_bg[1], c_bg[2], 255))
    draw = ImageDraw.Draw(im)

    # 2. Outer Architectural Border (Clean 22px frame inset)
    draw.rounded_rectangle([22, 22, width - 22, height - 22], radius=12, outline=c_border, width=1)
    # Corner registration marks
    draw.line([(22, 40), (22, 22), (40, 22)], fill=c_accent, width=3)
    draw.line([(width - 22, 40), (width - 22, 22), (width - 40, 22)], fill=c_accent, width=3)
    draw.line([(22, height - 40), (22, height - 22), (40, height - 22)], fill=c_accent, width=3)
    draw.line([(width - 22, height - 40), (width - 22, height - 22), (width - 40, height - 22)], fill=c_accent, width=3)

    # 3. Master Full Portrait (Fitted with 30px headroom and flush bottom, high-res downscaled)
    # ZERO glow blobs behind portrait • ZERO orbit lines
    target_w, target_h = 385, 422
    cutout_resized = hires_cutout.resize((target_w, target_h), Image.Resampling.LANCZOS)

    pos_x = 745
    pos_y = 50 + int(float_y)

    im.paste(cutout_resized, (pos_x, pos_y), cutout_resized)
    draw = ImageDraw.Draw(im)

    # 4. Typography (Left Column)
    f_mono = find_font(['consolab.ttf', 'consola.ttf', 'cour.ttf'], 11)
    f_name = find_font(['georgiab.ttf', 'georgia.ttf', 'timesbd.ttf'], 44)
    f_italic = find_font(['georgiai.ttf', 'georgia.ttf', 'timesi.ttf'], 20)
    f_desc = find_font(['segoeui.ttf', 'arial.ttf'], 15)
    f_pill = find_font(['consolab.ttf', 'consola.ttf'], 12)
    f_meta = find_font(['segoeuib.ttf', 'arialbd.ttf'], 13)

    # Telemetry Badge (Top Left, aligned and clean)
    badge_x, badge_y = 68, 42
    draw.rounded_rectangle([badge_x, badge_y, badge_x + 180, badge_y + 24], radius=12, fill=badge_bg[:3], outline=c_border, width=1)
    draw.ellipse([badge_x + 10, badge_y + 8, badge_x + 18, badge_y + 16], fill=c_accent)
    draw.text((badge_x + 24, badge_y + 6), '18.5204° N, 73.8567° E', fill=c_champagne, font=f_mono)

    # Overline
    draw.rectangle([68, 80, 76, 88], fill=c_accent)
    draw.text((86, 78), "MADHURA LAKADE // PORTFOLIO ARCHIVE", fill=c_dusty_rose, font=f_mono)

    # Name in Georgia Bold
    draw.text((68, 108), "Madhura Lakade", fill=c_ivory, font=f_name)

    # Headline
    draw.text((68, 168), "Developer by passion. Creator by nature.", fill=c_champagne, font=f_italic)

    # Description
    draw.text((68, 206), "Building thoughtful digital experiences through technology,", fill=c_champagne, font=f_desc)
    draw.text((68, 228), "creativity and curiosity.", fill=c_champagne, font=f_desc)

    # Manifesto Strip (SHE BUILDS · SHE THINKS · SHE CREATES)
    pills = [
        ("SHE BUILDS", 68, 268, 146),
        ("SHE THINKS", 238, 268, 146),
        ("SHE CREATES", 408, 268, 156)
    ]
    for text, px, py, pw in pills:
        draw.rounded_rectangle([px, py, px + pw, py + 34], radius=6, fill=c_pill, outline=c_pill_border, width=1)
        draw.text((px + pw // 2, py + 9), text, fill=c_silver_white, font=f_pill, anchor="mt")

    # Diamond separators
    draw.polygon([(223, 285), (227, 281), (231, 285), (227, 289)], fill=c_accent)
    draw.polygon([(393, 285), (397, 281), (401, 285), (397, 289)], fill=c_accent)

    # Supporting Details Metadata Row
    draw.ellipse([68, 338, 76, 346], fill=c_accent)
    draw.text((86, 336), "TY B.Sc. COMPUTER SCIENCE", fill=c_champagne, font=f_meta)
    draw.text((298, 336), "•", fill=c_border, font=f_meta)
    draw.text((314, 336), "PUNE, INDIA", fill=c_champagne, font=f_meta)
    draw.text((420, 336), "•", fill=c_border, font=f_meta)
    draw.text((436, 336), "FULL-STACK & SYSTEMS", fill=c_champagne, font=f_meta)

    return im

def get_master_palette(theme, base_frame, hires_cutout):
    """
    Creates an optimal 256-color master palette on a plain solid background:
    - 230 colors reserved for the portrait & facial features
    - 26 colors for plain background, UI text, borders & badges
    Guarantees zero facial posterization and zero frame-to-frame flickering.
    """
    # 1. 230 colors dedicated to portrait face & body colors
    face = hires_cutout.crop((280, 140, 620, 500)).convert('RGB')
    face_p = face.quantize(colors=230, method=Image.Quantize.FASTOCTREE)

    # 2. 26 colors for plain background & UI text/accents
    ui_sample = base_frame.crop((20, 20, 600, 460)).convert('RGB')
    ui_p = ui_sample.quantize(colors=26, method=Image.Quantize.FASTOCTREE)

    master_p = face_p.getpalette()[:230*3] + ui_p.getpalette()[:26*3]
    master_p = master_p + [0] * (768 - len(master_p))

    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(master_p)
    return pal_img

def build_animated_gif(theme="espresso", output_path="assets/hero/hero-banner.gif", num_frames=36, fps=18):
    """
    Builds a silky, active 36-frame animated GIF (~2.0s loop).
    Smooth sinusoidal portrait floating motion • PLAIN theme background • NO glow blobs • NO orbit lines.
    """
    base_frame = render_banner_frame(theme=theme, t_norm=0.0, float_y=0.0)
    master_pal = get_master_palette(theme, base_frame, hires_cutout)

    frames = []

    for i in range(num_frames):
        t_norm = i / float(num_frames)

        # Gentle floating oscillation (amplitude: 2.8px)
        float_y = 2.8 * math.sin(t_norm * 2 * math.pi)

        frame_rgba = render_banner_frame(
            theme=theme,
            t_norm=t_norm,
            float_y=float_y
        )

        bg_rgb_color = (33, 24, 23) if theme == 'espresso' else (74, 10, 29)
        frame_rgb = Image.new('RGB', frame_rgba.size, bg_rgb_color)
        frame_rgb.paste(frame_rgba, (0, 0), frame_rgba)

        # Quantize using master palette with Dither.NONE for razor-sharp facial features
        frame_p = frame_rgb.quantize(palette=master_pal, dither=Image.Dither.NONE)
        frames.append(frame_p)

    duration_ms = int(1000 / fps)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True
    )
    print(f"Animated GIF saved: {output_path} ({len(frames)} frames, {duration_ms}ms/frame)")

def build_all():
    os.makedirs('assets/hero', exist_ok=True)

    print("1. Generating SVG Hero Banners with Plain Theme Backgrounds (No Glow Blobs, No Orbits)...")
    svg_esp = build_hero_svg("espresso")
    with open('assets/hero/hero-banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_esp)

    svg_cherry = build_hero_svg("cherry")
    with open('assets/hero/hero-banner-cherry.svg', 'w', encoding='utf-8') as f:
        f.write(svg_cherry)

    svg_light = build_hero_svg("light")
    with open('assets/hero/hero-banner-light.svg', 'w', encoding='utf-8') as f:
        f.write(svg_light)
    print("   [OK] SVGs generated: hero-banner.svg, hero-banner-cherry.svg, hero-banner-light.svg")

    print("2. Generating Static PNG Previews (True-Color Lossless Plain Background)...")
    preview_esp = render_banner_frame(theme="espresso", t_norm=0.0, float_y=0.0)
    preview_esp.save('assets/hero/hero-banner-preview.png', format='PNG', optimize=True)

    preview_cherry = render_banner_frame(theme="cherry", t_norm=0.0, float_y=0.0)
    preview_cherry.save('assets/hero/hero-banner-cherry-preview.png', format='PNG', optimize=True)
    print("   [OK] PNG previews saved: hero-banner-preview.png, hero-banner-cherry-preview.png")

    print("3. Generating Side-by-Side Comparison Sheet...")
    comp_w = 1200
    comp_h = 500 * 2 + 70
    comp_img = Image.new('RGB', (comp_w, comp_h), (18, 12, 14))
    comp_draw = ImageDraw.Draw(comp_img)

    f_title = find_font(['georgiab.ttf', 'georgia.ttf'], 22)
    f_sub = find_font(['consolab.ttf', 'consola.ttf'], 12)

    comp_draw.text((30, 16), "MODE 01 — MIDNIGHT ÉSPRESSO (The Dark Edition)", fill=(255, 245, 237), font=f_title)
    comp_draw.text((720, 22), "Quiet luxury. Limitless depth. Plain #211817", fill=(217, 154, 167), font=f_sub)
    comp_img.paste(preview_esp, (0, 50))

    offset_y = 50 + 500 + 20
    comp_draw.text((30, offset_y - 28), "MODE 02 — CHERRY ROYALE (The Signature Edition)", fill=(255, 245, 237), font=f_title)
    comp_draw.text((720, offset_y - 22), "Bold elegance. Unapologetic expression. Plain #4A0A1D", fill=(255, 163, 184), font=f_sub)
    comp_img.paste(preview_cherry, (0, offset_y))

    comp_img.save('assets/hero/hero-comparison.png', format='PNG', optimize=True)
    print("   [OK] Comparison sheet saved: assets/hero/hero-comparison.png")

    print("4. Generating Midnight Éspresso Animated GIF (Plain Theme, No Blobs, No Orbits)...")
    build_animated_gif(theme="espresso", output_path="assets/hero/hero-banner.gif", num_frames=36, fps=18)

    print("5. Generating Cherry Royale Animated GIF (Plain Theme, No Blobs, No Orbits)...")
    build_animated_gif(theme="cherry", output_path="assets/hero/hero-banner-cherry.gif", num_frames=36, fps=18)

if __name__ == "__main__":
    build_all()

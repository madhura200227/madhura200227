import base64
import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 1. Master Source Transparent Cutout (Full Portrait with Crossed Arms)
CUTOUT_PATH = 'assets/portrait/madhura-full-pfp-hires.png'
if not os.path.exists(CUTOUT_PATH):
    CUTOUT_PATH = 'assets/portrait/madhura-full-pfp-cutout.png'
if not os.path.exists(CUTOUT_PATH):
    CUTOUT_PATH = 'assets/portrait/madhura-pfp.png'

hires_cutout = Image.open(CUTOUT_PATH).convert('RGBA')

with open(CUTOUT_PATH, 'rb') as f:
    pfp_png_b64 = base64.b64encode(f.read()).decode('utf-8')

# Scaled fitted version
fitted_cutout = hires_cutout.resize((385, 422), Image.Resampling.LANCZOS)
fitted_cutout.save('assets/portrait/madhura-full-pfp-fitted.png', format='PNG')

# ==============================================================================
# EDGE BLENDED BASE CANVAS (SEAMLESS GITHUB INTEGRATION)
# Fades outer perimeter to GitHub's #0d1117 so cards never look like raw cutouts
# ==============================================================================
def create_edge_blended_canvas(width, height, c_inner, c_outer, inset=24):
    arr = np.zeros((height, width, 3), dtype=float)
    y_coords = np.arange(height)
    x_coords = np.arange(width)
    
    dist_top = y_coords[:, None]
    dist_bottom = (height - 1 - y_coords)[:, None]
    dist_left = x_coords[None, :]
    dist_right = (width - 1 - x_coords)[None, :]
    
    min_dist_y = np.minimum(dist_top, dist_bottom)
    min_dist_x = np.minimum(dist_left, dist_right)
    edge_dist = np.minimum(min_dist_x, min_dist_y)
    
    t = np.clip(edge_dist / float(inset), 0.0, 1.0)
    smooth = t * t * (3.0 - 2.0 * t)
    
    for ch in range(3):
        arr[:, :, ch] = c_outer[ch] * (1.0 - smooth) + c_inner[ch] * smooth
        
    return Image.fromarray(np.uint8(arr), mode='RGB').convert('RGBA')

# ==============================================================================
# SVG HERO BANNER COMPOSITION (Midnight Éspresso & Cherry Royale)
# PLAIN theme backgrounds • Clean, short, uncluttered layout • NO orbits
# ==============================================================================
def build_hero_svg(theme="cherry"):
    silver_white = "#F0F4F8"
    github_dark = "#0d1117"

    if theme == "cherry":
        # Mode 02: Cherry Royale (The Signature Edition - DEFAULT)
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
        dot_sep = "#C1123F"
    else:
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
        dot_sep = "#873D50"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="hbBorder_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      {border_stops}
    </linearGradient>
    <radialGradient id="hbBlend_{theme}" cx="50%" cy="50%" r="50%">
      <stop offset="85%" stop-color="{bg_color}" />
      <stop offset="100%" stop-color="{github_dark}" />
    </radialGradient>
  </defs>

  <style>
    .hb-name {{ font-family: 'Georgia', 'Playfair Display', serif; font-size: 46px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.2px; }}
    .hb-headline {{ font-family: 'Playfair Display', Georgia, serif; font-size: 21px; font-style: italic; fill: #E8D5C5; }}
    .hb-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; fill: #E8D5C5; letter-spacing: 0.2px; }}
    .hb-pillar-text {{ font-family: 'IBM Plex Mono', monospace; font-size: 11.5px; font-weight: 600; letter-spacing: 1.6px; fill: {silver_white}; }}
    .hb-info-bold {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; font-weight: 700; fill: #FFF5ED; }}
    .hb-info-reg {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; font-weight: 400; fill: #E8D5C5; }}
    .hb-status {{ font-family: 'IBM Plex Mono', monospace; font-size: 13.5px; font-weight: 500; fill: {silver_white}; letter-spacing: 0.6px; }}
  </style>

  <!-- Edge-Blended Canvas (Seamless Dissolve into GitHub #0d1117) -->
  <rect width="1200" height="500" rx="16" fill="url(#hbBlend_{theme})" />

  <!-- Outer Architectural Border (Clean 22px frame inset) -->
  <rect x="22" y="22" width="1156" height="456" rx="12" fill="{bg_color}" stroke="url(#hbBorder_{theme})" stroke-width="1.2" />

  <!-- Corner Flourish Registration Marks -->
  <path d="M 22 40 L 22 22 L 40 22" fill="none" stroke="{accent_color}" stroke-width="2.5" />
  <path d="M 1178 40 L 1178 22 L 1160 22" fill="none" stroke="{accent_color}" stroke-width="2.5" />
  <path d="M 22 460 L 22 478 L 40 478" fill="none" stroke="{accent_color}" stroke-width="2.5" />
  <path d="M 1178 460 L 1178 478 L 1160 478" fill="none" stroke="{accent_color}" stroke-width="2.5" />

  <!-- ========================================================================= -->
  <!-- DEPTH LAYER 2: MASTER FULL PORTRAIT (TRUE COLOR LOSSLESS 32-BIT PNG)     -->
  <!-- Animated celestial float + 100% Original Facial Features • NO orbits     -->
  <!-- ========================================================================= -->
  <g id="portraitGroup" transform="translate(745, 50)">
    <animateTransform attributeName="transform" type="translate"
      values="745 50; 745 47; 745 53; 745 50"
      keyTimes="0; 0.35; 0.75; 1"
      dur="4.5s" repeatCount="indefinite" />
    <image href="data:image/png;base64,{pfp_png_b64}" x="0" y="0" width="385" height="422" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- ========================================================================= -->
  <!-- CLEAN EDITORIAL TYPOGRAPHY & MANIFESTO STRIP (LEFT COLUMN)                -->
  <!-- Simple, readable, elegant, no repetitive text, no nested boxes            -->
  <!-- ========================================================================= -->
  <!-- 1. Name -->
  <text x="75" y="106" class="hb-name">Madhura Lakade</text>

  <!-- 2. Headline -->
  <text x="75" y="148" class="hb-headline">Developer by passion. Creator by nature.</text>

  <!-- 3. Description -->
  <text x="75" y="184" class="hb-desc">Building thoughtful digital experiences through technology,</text>
  <text x="75" y="208" class="hb-desc">creativity and curiosity.</text>

  <!-- 4. Tabular Manifesto Strip (SHE BUILDS · SHE THINKS · SHE CREATES) -->
  <g transform="translate(75, 246)">
    <rect x="0" y="0" width="142" height="32" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.2" />
    <text x="71" y="21" class="hb-pillar-text" text-anchor="middle">SHE BUILDS</text>

    <polygon points="151,16 155,12 159,16 155,20" fill="{diamond_fill}" />

    <rect x="168" y="0" width="142" height="32" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.2" />
    <text x="239" y="21" class="hb-pillar-text" text-anchor="middle">SHE THINKS</text>

    <polygon points="319,16 323,12 327,16 323,20" fill="{diamond_fill}" />

    <rect x="336" y="0" width="154" height="32" rx="6" fill="{pill_fill}" stroke="{pill_stroke}" stroke-width="1.2" />
    <text x="413" y="21" class="hb-pillar-text" text-anchor="middle">SHE CREATES</text>
  </g>

  <!-- 5. Clean Profile Details -->
  <!-- Line 1: Computer Science Student • Savitribai Phule Pune University -->
  <g transform="translate(75, 320)">
    <circle cx="3" cy="5" r="3.5" fill="{accent_color}" />
    <text x="16" y="10" class="hb-info-bold">Computer Science Student</text>
    <text x="218" y="10" class="hb-info-bold" fill="{dot_sep}">•</text>
    <text x="235" y="10" class="hb-info-reg">Savitribai Phule Pune University</text>
  </g>

  <!-- Line 2: 9.2+ CGPA • Pune, Maharashtra -->
  <g transform="translate(75, 356)">
    <circle cx="3" cy="5" r="3.5" fill="{accent_color}" />
    <text x="16" y="10" class="hb-info-bold">9.2+ CGPA</text>
    <text x="100" y="10" class="hb-info-bold" fill="{dot_sep}">•</text>
    <text x="116" y="10" class="hb-info-reg">Pune, Maharashtra</text>
  </g>

  <!-- Line 3: Available for Part-time & Remote Engineering -->
  <g transform="translate(75, 396)">
    <circle cx="4" cy="6" r="4.5" fill="#4ADE80">
      <animate attributeName="r" values="4;5.2;4" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="18" y="11" class="hb-status">Available for Part-time &amp; Remote Engineering</text>
  </g>
</svg>'''

# ==============================================================================
# RENDER STATIC PREVIEW & ANIMATED GIF USING PILLOW
# Plain solid theme background with GitHub edge-blend • ZERO glow blobs • ZERO orbits
# ==============================================================================
def find_font(font_names, size):
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            pass
    return ImageFont.load_default()

def render_banner_frame(theme="cherry", t_norm=0.0, float_y=0.0):
    width, height = 1200, 500
    c_github = (13, 17, 23) # #0d1117 (GitHub Dark Background)

    if theme == "cherry":
        # Mode 02: Cherry Royale (The Signature Edition - DEFAULT)
        c_bg = (74, 10, 29)            # Solid #4A0A1D
        c_border = (193, 18, 63)        # #C1123F
        c_accent = (255, 45, 96)        # #FF2D60
        c_pill = (107, 12, 38)          # #6B0C26
        c_pill_border = (255, 45, 96)
        c_diamond = (255, 45, 96)
        c_dot_sep = (193, 18, 63)
    else: # espresso
        # Mode 01: Midnight Éspresso (The Dark Edition)
        c_bg = (33, 24, 23)            # Solid #211817
        c_border = (135, 61, 80)        # #873D50
        c_accent = (193, 18, 63)        # #C1123F
        c_pill = (101, 13, 37)          # #650D25
        c_pill_border = (135, 61, 80)
        c_diamond = (193, 18, 63)
        c_dot_sep = (135, 61, 80)

    c_ivory = (255, 245, 237)
    c_champagne = (232, 213, 197)
    c_silver_white = (240, 244, 248)
    c_emerald = (74, 222, 128)

    # 1. Edge-Blended Base Canvas (Seamless transition to GitHub #0d1117)
    im = create_edge_blended_canvas(width, height, c_bg, c_github, inset=24)
    draw = ImageDraw.Draw(im)

    # 2. Outer Architectural Border (Clean 22px frame inset)
    draw.rounded_rectangle([22, 22, width - 22, height - 22], radius=12, fill=c_bg, outline=c_border, width=1)
    draw.line([(22, 40), (22, 22), (40, 22)], fill=c_accent, width=3)
    draw.line([(width - 22, 40), (width - 22, 22), (width - 40, 22)], fill=c_accent, width=3)
    draw.line([(22, height - 40), (22, height - 22), (40, height - 22)], fill=c_accent, width=3)
    draw.line([(width - 22, height - 40), (width - 22, height - 22), (width - 40, height - 22)], fill=c_accent, width=3)

    # 3. Master Full Portrait (Fitted with gentle floating motion)
    target_w, target_h = 385, 422
    cutout_resized = hires_cutout.resize((target_w, target_h), Image.Resampling.LANCZOS)
    pos_x = 745
    pos_y = 50 + int(float_y)
    im.paste(cutout_resized, (pos_x, pos_y), cutout_resized)
    draw = ImageDraw.Draw(im)

    # Fonts
    f_name = find_font(['georgiab.ttf', 'georgia.ttf'], 48)
    f_italic = find_font(['georgiai.ttf', 'georgia.ttf'], 21)
    f_desc = find_font(['segoeui.ttf', 'arial.ttf'], 16)
    f_pill = find_font(['consolab.ttf', 'consola.ttf'], 12)
    f_info_bold = find_font(['segoeuib.ttf', 'arialbd.ttf'], 15)
    f_info_reg = find_font(['segoeui.ttf', 'arial.ttf'], 15)
    f_mono_status = find_font(['consolab.ttf', 'consola.ttf'], 13)

    lx = 75

    # 1. Name
    draw.text((lx, 60), "Madhura Lakade", fill=c_ivory, font=f_name)

    # 2. Headline
    draw.text((lx, 126), "Developer by passion. Creator by nature.", fill=c_champagne, font=f_italic)

    # 3. Description
    draw.text((lx, 168), "Building thoughtful digital experiences through technology,", fill=c_champagne, font=f_desc)
    draw.text((lx, 194), "creativity and curiosity.", fill=c_champagne, font=f_desc)

    # 4. Tabular Manifesto Strip (SHE BUILDS · SHE THINKS · SHE CREATES)
    pills = [
        ("SHE BUILDS", lx, 242, 142),
        ("SHE THINKS", lx + 164, 242, 142),
        ("SHE CREATES", lx + 328, 242, 154)
    ]
    for text, px, py, pw in pills:
        draw.rounded_rectangle([px, py, px + pw, py + 32], radius=6, fill=c_pill, outline=c_pill_border, width=1)
        draw.text((px + pw // 2, py + 8), text, fill=c_silver_white, font=f_pill, anchor="mt")

    draw.polygon([(lx + 150, 258), (lx + 154, 254), (lx + 158, 258), (lx + 154, 262)], fill=c_diamond)
    draw.polygon([(lx + 314, 258), (lx + 318, 254), (lx + 322, 258), (lx + 318, 262)], fill=c_diamond)

    # 5. Clean Profile Details
    # Line 1: Computer Science Student • Savitribai Phule Pune University
    y_info1 = 312
    draw.ellipse([lx, y_info1 + 6, lx + 6, y_info1 + 12], fill=c_accent)
    draw.text((lx + 16, y_info1), "Computer Science Student", fill=c_ivory, font=f_info_bold)
    w1 = int(draw.textlength("Computer Science Student", font=f_info_bold))
    draw.text((lx + 16 + w1 + 12, y_info1), "•", fill=c_dot_sep, font=f_info_bold)
    draw.text((lx + 16 + w1 + 26, y_info1), "Savitribai Phule Pune University", fill=c_champagne, font=f_info_reg)

    # Line 2: 9.2+ CGPA • Pune, Maharashtra
    y_info2 = 348
    draw.ellipse([lx, y_info2 + 6, lx + 6, y_info2 + 12], fill=c_accent)
    draw.text((lx + 16, y_info2), "9.2+ CGPA", fill=c_ivory, font=f_info_bold)
    w2 = int(draw.textlength("9.2+ CGPA", font=f_info_bold))
    draw.text((lx + 16 + w2 + 12, y_info2), "•", fill=c_dot_sep, font=f_info_bold)
    draw.text((lx + 16 + w2 + 26, y_info2), "Pune, Maharashtra", fill=c_champagne, font=f_info_reg)

    # Line 3: Available for Part-time & Remote Engineering
    y_info3 = 392
    draw.ellipse([lx, y_info3 + 4, lx + 10, y_info3 + 14], fill=c_emerald)
    draw.text((lx + 20, y_info3), "Available for Part-time & Remote Engineering", fill=c_silver_white, font=f_mono_status)

    return im

def get_master_palette(theme, base_frame, hires_cutout):
    face = hires_cutout.crop((280, 140, 620, 500)).convert('RGB')
    face_p = face.quantize(colors=225, method=Image.Quantize.FASTOCTREE)

    ui_sample = base_frame.crop((20, 20, 700, 470)).convert('RGB')
    ui_p = ui_sample.quantize(colors=31, method=Image.Quantize.FASTOCTREE)

    master_p = face_p.getpalette()[:225*3] + ui_p.getpalette()[:31*3]
    master_p = master_p + [0] * (768 - len(master_p))

    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(master_p)
    return pal_img

def build_animated_gif(theme="cherry", output_path="assets/hero/hero-banner-cherry.gif", num_frames=36, fps=18):
    base_frame = render_banner_frame(theme=theme, t_norm=0.0, float_y=0.0)
    master_pal = get_master_palette(theme, base_frame, hires_cutout)

    frames = []

    for i in range(num_frames):
        t_norm = i / float(num_frames)
        float_y = 2.8 * math.sin(t_norm * 2 * math.pi)

        frame_rgba = render_banner_frame(
            theme=theme,
            t_norm=t_norm,
            float_y=float_y
        )

        bg_rgb_color = (13, 17, 23) # Seamless outer blend on GitHub
        frame_rgb = Image.new('RGB', frame_rgba.size, bg_rgb_color)
        frame_rgb.paste(frame_rgba, (0, 0), frame_rgba)

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

    print("1. Generating Clean SVG Hero Banners with GitHub Edge Blending...")
    svg_cherry = build_hero_svg("cherry")
    with open('assets/hero/hero-banner-cherry.svg', 'w', encoding='utf-8') as f:
        f.write(svg_cherry)

    svg_esp = build_hero_svg("espresso")
    with open('assets/hero/hero-banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_esp)

    svg_light = build_hero_svg("light")
    with open('assets/hero/hero-banner-light.svg', 'w', encoding='utf-8') as f:
        f.write(svg_light)
    print("   [OK] SVGs generated: hero-banner-cherry.svg, hero-banner.svg, hero-banner-light.svg")

    print("2. Generating Static PNG Previews with GitHub Edge Blending...")
    preview_cherry = render_banner_frame(theme="cherry", t_norm=0.0, float_y=0.0)
    preview_cherry.save('assets/hero/hero-banner-cherry-preview.png', format='PNG', optimize=True)

    preview_esp = render_banner_frame(theme="espresso", t_norm=0.0, float_y=0.0)
    preview_esp.save('assets/hero/hero-banner-preview.png', format='PNG', optimize=True)
    print("   [OK] PNG previews saved: hero-banner-cherry-preview.png, hero-banner-preview.png")

    print("3. Generating Side-by-Side Comparison Sheet...")
    comp_w = 1200
    comp_h = 500 * 2 + 70
    comp_img = Image.new('RGB', (comp_w, comp_h), (13, 17, 23)) # GitHub dark
    comp_draw = ImageDraw.Draw(comp_img)

    f_title = find_font(['georgiab.ttf', 'georgia.ttf'], 22)
    f_sub = find_font(['consolab.ttf', 'consola.ttf'], 12)

    comp_draw.text((30, 16), "MODE 02 — CHERRY ROYALE (Seamless GitHub Edge Blend)", fill=(255, 245, 237), font=f_title)
    comp_draw.text((700, 22), "Bold elegance. Unapologetic expression. Dissolves into #0d1117", fill=(255, 163, 184), font=f_sub)
    comp_img.paste(preview_cherry, (0, 50))

    offset_y = 50 + 500 + 20
    comp_draw.text((30, offset_y - 28), "MODE 01 — MIDNIGHT ÉSPRESSO (Seamless GitHub Edge Blend)", fill=(255, 245, 237), font=f_title)
    comp_draw.text((700, offset_y - 22), "Quiet luxury. Limitless depth. Dissolves into #0d1117", fill=(217, 154, 167), font=f_sub)
    comp_img.paste(preview_esp, (0, offset_y))

    comp_img.save('assets/hero/hero-comparison.png', format='PNG', optimize=True)
    print("   [OK] Comparison sheet saved: assets/hero/hero-comparison.png")

    print("4. Generating Cherry Royale Animated GIF (DEFAULT with GitHub Edge Blend)...")
    build_animated_gif(theme="cherry", output_path="assets/hero/hero-banner-cherry.gif", num_frames=36, fps=18)

    print("5. Generating Midnight Éspresso Animated GIF (with GitHub Edge Blend)...")
    build_animated_gif(theme="espresso", output_path="assets/hero/hero-banner.gif", num_frames=36, fps=18)

if __name__ == "__main__":
    build_all()

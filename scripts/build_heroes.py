import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 1. Master Cutout
CUTOUT_PATH = 'assets/portrait/madhura-full-pfp-hires.png'
if not os.path.exists(CUTOUT_PATH):
    CUTOUT_PATH = 'assets/portrait/madhura-full-pfp-cutout.png'

hires_cutout = Image.open(CUTOUT_PATH).convert('RGBA')

def find_font(font_names, size):
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            pass
    return ImageFont.load_default()

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

def render_banner_frame(theme="cherry", t_norm=0.0, float_y=0.0):
    width, height = 1200, 500
    c_github = (13, 17, 23) # #0d1117 (GitHub Dark Background)

    if theme == "cherry":
        c_bg = (74, 10, 29)             # Solid #4A0A1D
        c_border = (193, 18, 63)         # #C1123F
        c_accent = (255, 45, 96)         # #FF2D60
        c_pill = (107, 12, 38)           # #6B0C26
        c_pill_border = (255, 45, 96)
        c_diamond = (255, 45, 96)
        c_dot_sep = (255, 45, 96)
    else: # espresso
        c_bg = (33, 24, 23)             # Solid #211817
        c_border = (135, 61, 80)         # #873D50
        c_accent = (193, 18, 63)         # #C1123F
        c_pill = (101, 13, 37)           # #650D25
        c_pill_border = (135, 61, 80)
        c_diamond = (193, 18, 63)
        c_dot_sep = (193, 18, 63)

    # Crystal Clear, High-Contrast Typography Palette (NO muddy brownish tint)
    c_pure_white = (255, 255, 255)
    c_bright_champagne = (250, 242, 236)
    c_silver_white = (255, 255, 255)

    # 1. Edge-Blended Base Canvas
    im = create_edge_blended_canvas(width, height, c_bg, c_github, inset=24)
    draw = ImageDraw.Draw(im)

    # 2. Outer Architectural Border
    draw.rounded_rectangle([22, 22, width - 22, height - 22], radius=12, fill=c_bg, outline=c_border, width=1)
    draw.line([(22, 40), (22, 22), (40, 22)], fill=c_accent, width=3)
    draw.line([(width - 22, 40), (width - 22, 22), (width - 40, 22)], fill=c_accent, width=3)
    draw.line([(22, height - 40), (22, height - 22), (40, height - 22)], fill=c_accent, width=3)
    draw.line([(width - 22, height - 40), (width - 22, height - 22), (width - 40, height - 22)], fill=c_accent, width=3)

    # 3. Master Full Portrait (Gentle floating motion)
    target_w, target_h = 385, 422
    cutout_resized = hires_cutout.resize((target_w, target_h), Image.Resampling.LANCZOS)
    pos_x = 745
    pos_y = 50 + int(float_y)
    im.paste(cutout_resized, (pos_x, pos_y), cutout_resized)
    draw = ImageDraw.Draw(im)

    # Fonts - High legibility, crisp weights
    f_name = find_font(['georgiab.ttf', 'georgia.ttf'], 48)
    f_italic = find_font(['georgiai.ttf', 'georgia.ttf'], 22)
    f_desc = find_font(['segoeuib.ttf', 'segoeui.ttf', 'arial.ttf'], 16)
    f_pill = find_font(['consolab.ttf', 'consola.ttf'], 12)
    f_info_bold = find_font(['segoeuib.ttf', 'arialbd.ttf'], 15)
    f_info_reg = find_font(['segoeui.ttf', 'arial.ttf'], 15)
    f_mono_status = find_font(['consolab.ttf', 'consola.ttf'], 13)
    f_goals = find_font([r'C:\Windows\Fonts\GOTHICB.TTF', 'GOTHICB.TTF', 'gothicb.ttf', 'segoeuib.ttf'], 19)

    lx = 75

    # 1. Name - Pure White
    draw.text((lx, 60), "Madhura Lakade", fill=c_pure_white, font=f_name)

    # 2. Headline - Crisp Italic
    draw.text((lx, 126), "Developer by passion. Creator by nature.", fill=c_bright_champagne, font=f_italic)

    # 3. Description - High legibility
    draw.text((lx, 168), "Building thoughtful digital experiences through technology,", fill=c_bright_champagne, font=f_desc)
    draw.text((lx, 194), "creativity and curiosity.", fill=c_bright_champagne, font=f_desc)

    # 4. Tabular Manifesto Strip (SHE BUILDS · SHE THINKS · SHE CREATES)
    pills = [
        ("SHE BUILDS", lx, 242, 142),
        ("SHE THINKS", lx + 164, 242, 142),
        ("SHE CREATES", lx + 328, 242, 154)
    ]
    for text, px, py, pw in pills:
        draw.rounded_rectangle([px, py, px + pw, py + 32], radius=6, fill=c_pill, outline=c_pill_border, width=1)
        draw.text((px + pw // 2, py + 8), text, fill=c_pure_white, font=f_pill, anchor="mt")

    draw.polygon([(lx + 150, 258), (lx + 154, 254), (lx + 158, 258), (lx + 154, 262)], fill=c_diamond)
    draw.polygon([(lx + 314, 258), (lx + 318, 254), (lx + 322, 258), (lx + 318, 262)], fill=c_diamond)

    # 5. Clean Profile Details (NO GREEN DOTS - ALL ACCENT BULLETS)
    # Line 1: Computer Science Student • Savitribai Phule Pune University
    y_info1 = 312
    draw.ellipse([lx, y_info1 + 6, lx + 6, y_info1 + 12], fill=c_accent)
    draw.text((lx + 16, y_info1), "Computer Science Student", fill=c_pure_white, font=f_info_bold)
    w1 = int(draw.textlength("Computer Science Student", font=f_info_bold))
    draw.text((lx + 16 + w1 + 12, y_info1), "•", fill=c_dot_sep, font=f_info_bold)
    draw.text((lx + 16 + w1 + 26, y_info1), "Savitribai Phule Pune University", fill=c_bright_champagne, font=f_info_reg)

    # Line 2: 9.2+ CGPA • Pune, Maharashtra
    y_info2 = 348
    draw.ellipse([lx, y_info2 + 6, lx + 6, y_info2 + 12], fill=c_accent)
    draw.text((lx + 16, y_info2), "9.2+ CGPA", fill=c_pure_white, font=f_info_bold)
    w2 = int(draw.textlength("9.2+ CGPA", font=f_info_bold))
    draw.text((lx + 16 + w2 + 12, y_info2), "•", fill=c_dot_sep, font=f_info_bold)
    draw.text((lx + 16 + w2 + 26, y_info2), "Pune, Maharashtra", fill=c_bright_champagne, font=f_info_reg)

    # Line 3: Available for Part-time & Remote Engineering (NO GREEN DOT - ACCENT BULLET)
    y_info3 = 392
    draw.ellipse([lx, y_info3 + 5, lx + 6, y_info3 + 11], fill=c_accent)
    draw.text((lx + 16, y_info3), "Available for Part-time & Remote Engineering", fill=c_pure_white, font=f_mono_status)

    # Line 4: @goalsgettergoddess_ (Geometric Bold in Century Gothic)
    y_info4 = 430
    draw.ellipse([lx, y_info4 + 5, lx + 6, y_info4 + 11], fill=c_accent)
    draw.text((lx + 16, y_info4), "@goalsgettergoddess_", fill=c_pure_white, font=f_goals)

    return im

def build_hero_svg(theme="cherry"):
    silver_white = "#FFFFFF"
    github_dark = "#0d1117"

    if theme == "cherry":
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
        dot_sep = "#FF2D60"
    else:
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

    import base64
    with open(CUTOUT_PATH, 'rb') as f:
        pfp_png_b64 = base64.b64encode(f.read()).decode('utf-8')

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
    .hb-name {{ font-family: 'Georgia', 'Playfair Display', serif; font-size: 48px; font-weight: 700; fill: #FFFFFF; letter-spacing: 0.2px; }}
    .hb-headline {{ font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-style: italic; fill: #FAF2EC; }}
    .hb-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 16px; font-weight: 500; fill: #FAF2EC; letter-spacing: 0.2px; }}
    .hb-pillar-text {{ font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 700; letter-spacing: 1.6px; fill: #FFFFFF; }}
    .hb-info-bold {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; font-weight: 700; fill: #FFFFFF; }}
    .hb-info-reg {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; font-weight: 400; fill: #FAF2EC; }}
    .hb-status {{ font-family: 'IBM Plex Mono', monospace; font-size: 14px; font-weight: 600; fill: #FFFFFF; letter-spacing: 0.6px; }}
    .hb-goals {{ font-family: 'Century Gothic', 'Outfit', 'Poppins', 'Montserrat', -apple-system, sans-serif; font-size: 19px; font-weight: 700; fill: #FFFFFF; letter-spacing: 0.5px; }}
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

  <!-- DEPTH LAYER 2: MASTER FULL PORTRAIT -->
  <g id="portraitGroup" transform="translate(745, 50)">
    <animateTransform attributeName="transform" type="translate"
      values="745 50; 745 47; 745 53; 745 50"
      keyTimes="0; 0.35; 0.75; 1"
      dur="4.5s" repeatCount="indefinite" />
    <image href="data:image/png;base64,{pfp_png_b64}" x="0" y="0" width="385" height="422" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- CLEAN EDITORIAL TYPOGRAPHY & MANIFESTO STRIP (LEFT COLUMN) -->
  <text x="75" y="106" class="hb-name">Madhura Lakade</text>
  <text x="75" y="148" class="hb-headline">Developer by passion. Creator by nature.</text>
  <text x="75" y="184" class="hb-desc">Building thoughtful digital experiences through technology,</text>
  <text x="75" y="208" class="hb-desc">creativity and curiosity.</text>

  <!-- Tabular Manifesto Strip -->
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

  <!-- Clean Profile Details (NO GREEN DOTS) -->
  <!-- Line 1 -->
  <g transform="translate(75, 320)">
    <circle cx="3" cy="5" r="3.5" fill="{accent_color}" />
    <text x="16" y="10" class="hb-info-bold">Computer Science Student</text>
    <text x="218" y="10" class="hb-info-bold" fill="{dot_sep}">•</text>
    <text x="235" y="10" class="hb-info-reg">Savitribai Phule Pune University</text>
  </g>

  <!-- Line 2 -->
  <g transform="translate(75, 356)">
    <circle cx="3" cy="5" r="3.5" fill="{accent_color}" />
    <text x="16" y="10" class="hb-info-bold">9.2+ CGPA</text>
    <text x="100" y="10" class="hb-info-bold" fill="{dot_sep}">•</text>
    <text x="116" y="10" class="hb-info-reg">Pune, Maharashtra</text>
  </g>

  <!-- Line 3 (NO GREEN DOT - ACCENT BULLET) -->
  <g transform="translate(75, 396)">
    <circle cx="3" cy="5" r="3.5" fill="{accent_color}" />
    <text x="16" y="10" class="hb-status">Available for Part-time &amp; Remote Engineering</text>
  </g>

  <!-- Line 4: @goalsgettergoddess_ -->
  <g transform="translate(75, 432)">
    <circle cx="3" cy="5" r="3.5" fill="{accent_color}" />
    <text x="16" y="10" class="hb-goals">@goalsgettergoddess_</text>
  </g>
</svg>'''

def get_master_palette(theme, base_frame, hires_cutout):
    # Lock in 120 dedicated colors for left text & UI to guarantee 100% crystal clear readability
    ui_sample = base_frame.crop((20, 20, 740, 475)).convert('RGB')
    ui_p = ui_sample.quantize(colors=110, method=Image.Quantize.FASTOCTREE)

    face = hires_cutout.crop((280, 140, 620, 500)).convert('RGB')
    face_p = face.quantize(colors=135, method=Image.Quantize.FASTOCTREE)

    # Core locked colors: pure white, bright champagne, accent, background, github dark
    key_colors = [
        255, 255, 255, # Pure White
        250, 242, 236, # Bright Champagne
        255, 45, 96,   # Cherry Accent
        193, 18, 63,   # Deep Red Accent
        135, 61, 80,   # Border Accent
        74, 10, 29,    # Cherry Base
        33, 24, 23,    # Espresso Base
        13, 17, 23,    # GitHub Dark
        0, 0, 0,
        255, 245, 237,
        232, 213, 197
    ]

    master_p = key_colors + ui_p.getpalette()[:100*3] + face_p.getpalette()[:135*3]
    master_p = master_p[:768]
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

        bg_rgb_color = (13, 17, 23)
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

    print("1. Generating Clean SVG Hero Banners...")
    svg_cherry = build_hero_svg("cherry")
    with open('assets/hero/hero-banner-cherry.svg', 'w', encoding='utf-8') as f:
        f.write(svg_cherry)

    svg_esp = build_hero_svg("espresso")
    with open('assets/hero/hero-banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_esp)

    svg_light = build_hero_svg("light")
    with open('assets/hero/hero-banner-light.svg', 'w', encoding='utf-8') as f:
        f.write(svg_light)
    print("   [OK] SVGs generated")

    print("2. Generating Static PNG Previews...")
    preview_cherry = render_banner_frame(theme="cherry", t_norm=0.0, float_y=0.0)
    preview_cherry.save('assets/hero/hero-banner-cherry-preview.png', format='PNG', optimize=True)

    preview_esp = render_banner_frame(theme="espresso", t_norm=0.0, float_y=0.0)
    preview_esp.save('assets/hero/hero-banner-preview.png', format='PNG', optimize=True)
    print("   [OK] PNG previews saved")

    print("3. Generating Cherry Royale Animated GIF (Crystal Clear Text)...")
    build_animated_gif("cherry", "assets/hero/hero-banner-cherry.gif")

    print("4. Generating Midnight Éspresso Animated GIF (Crystal Clear Text)...")
    build_animated_gif("espresso", "assets/hero/hero-banner.gif")

if __name__ == '__main__':
    build_all()

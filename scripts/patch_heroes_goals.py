with open('scripts/build_heroes.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update SVG CSS
target_css = ".hb-status {{ font-family: 'IBM Plex Mono', monospace; font-size: 13.5px; font-weight: 500; fill: {silver_white}; letter-spacing: 0.6px; }}"
repl_css = """.hb-status {{ font-family: 'IBM Plex Mono', monospace; font-size: 13.5px; font-weight: 500; fill: {silver_white}; letter-spacing: 0.6px; }}
    .hb-goals {{ font-family: 'Century Gothic', 'Outfit', 'Poppins', 'Montserrat', -apple-system, sans-serif; font-size: 17px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.4px; }}"""

# 2. Update SVG Line 4
target_svg_line = """  <!-- Line 3: Available for Part-time & Remote Engineering -->
  <g transform="translate(75, 396)">
    <circle cx="4" cy="6" r="4.5" fill="#4ADE80">
      <animate attributeName="r" values="4;5.2;4" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="18" y="11" class="hb-status">Available for Part-time &amp; Remote Engineering</text>
  </g>
</svg>'''"""

repl_svg_line = """  <!-- Line 3: Available for Part-time & Remote Engineering -->
  <g transform="translate(75, 396)">
    <circle cx="4" cy="6" r="4.5" fill="#4ADE80">
      <animate attributeName="r" values="4;5.2;4" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="18" y="11" class="hb-status">Available for Part-time &amp; Remote Engineering</text>
  </g>

  <!-- Line 4: @goalsgettergoddess_ (Geometric Bold in Century Gothic format) -->
  <g transform="translate(75, 432)">
    <circle cx="4" cy="6" r="3.5" fill="{accent_color}" />
    <text x="18" y="11" class="hb-goals">@goalsgettergoddess_</text>
  </g>
</svg>'''"""

# 3. Update Pillow fonts
target_pillow_fonts = "f_mono_status = find_font(['consolab.ttf', 'consola.ttf'], 13)"
repl_pillow_fonts = """f_mono_status = find_font(['consolab.ttf', 'consola.ttf'], 13)
    f_goals = find_font([r'C:\\Windows\\Fonts\\GOTHICB.TTF', 'GOTHICB.TTF', 'gothicb.ttf', 'segoeuib.ttf', 'arialbd.ttf'], 18)"""

# 4. Update Pillow Line 4
target_pillow_line = """    # Line 3: Available for Part-time & Remote Engineering
    y_info3 = 392
    draw.ellipse([lx, y_info3 + 4, lx + 10, y_info3 + 14], fill=c_emerald)
    draw.text((lx + 20, y_info3), "Available for Part-time & Remote Engineering", fill=c_silver_white, font=f_mono_status)"""

repl_pillow_line = """    # Line 3: Available for Part-time & Remote Engineering
    y_info3 = 392
    draw.ellipse([lx, y_info3 + 4, lx + 10, y_info3 + 14], fill=c_emerald)
    draw.text((lx + 20, y_info3), "Available for Part-time & Remote Engineering", fill=c_silver_white, font=f_mono_status)

    # Line 4: @goalsgettergoddess_ (Geometric Bold in Century Gothic format)
    y_info4 = 430
    draw.ellipse([lx + 2, y_info4 + 5, lx + 8, y_info4 + 11], fill=c_accent)
    draw.text((lx + 20, y_info4), "@goalsgettergoddess_", fill=c_ivory, font=f_goals)"""

if target_css in text and target_svg_line in text and target_pillow_fonts in text and target_pillow_line in text:
    text = text.replace(target_css, repl_css)
    text = text.replace(target_svg_line, repl_svg_line)
    text = text.replace(target_pillow_fonts, repl_pillow_fonts)
    text = text.replace(target_pillow_line, repl_pillow_line)
    with open('scripts/build_heroes.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated scripts/build_heroes.py successfully with @goalsgettergoddess_')
else:
    print('Could not find all targets in scripts/build_heroes.py')
    print('target_css found:', target_css in text)
    print('target_svg_line found:', target_svg_line in text)
    print('target_pillow_fonts found:', target_pillow_fonts in text)
    print('target_pillow_line found:', target_pillow_line in text)


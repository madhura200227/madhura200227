with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Title
target_title = "<title>Madhura Lakade — GitHub Profile Architecture & Live Backend Engine</title>"
repl_title = "<title>Madhura Lakade — Interactive Portfolio Studio & Architecture</title>"

# 2. Update Dock
target_dock = """  <!-- Fixed Bottom Status Dock -->
  <div class="status-dock">
    <div class="status-dot"></div>
    <span>Full-Stack Profile Engine &nbsp;•&nbsp; <strong>Madhura Lakade</strong> &nbsp;•&nbsp; <span id="dockAnimationStatus" style="color:var(--accent-cherry);">60 FPS LIVE ANIMATIONS ACTIVE</span></span>
  </div>"""

repl_dock = """  <!-- Fixed Bottom Status Dock -->
  <div class="status-dock">
    <div class="status-dot"></div>
    <span>Interactive Portfolio Studio &nbsp;•&nbsp; <strong>Madhura Lakade</strong> &nbsp;•&nbsp; <strong style="font-family:'Century Gothic', 'Outfit', 'Poppins', sans-serif; letter-spacing:0.5px;">@goalsgettergoddess_</strong> &nbsp;•&nbsp; <span id="dockAnimationStatus" style="color:var(--accent-cherry);">60 FPS LIVE ANIMATIONS ACTIVE</span></span>
  </div>"""

# 3. Update status text fallback
target_stat = "'ENGINE: LIVE (GITHUB PAGES)'"
repl_stat = "'STUDIO: LIVE (GITHUB PAGES)'"

if target_title in text and target_dock in text:
    text = text.replace(target_title, repl_title)
    text = text.replace(target_dock, repl_dock)
    text = text.replace(target_stat, repl_stat)
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated preview.html & index.html successfully')
else:
    print('Targets not found')
    print('target_title:', target_title in text)
    print('target_dock:', target_dock in text)


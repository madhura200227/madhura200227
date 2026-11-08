import os

def create_theme_pills():
    os.makedirs('assets/icons', exist_ok=True)

    # 1. Cherry Active Pill (NO GREEN DOT - Theme Accent Dot #FF2D60)
    svg_cherry_active = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="32" viewBox="0 0 200 32">
  <defs>
    <linearGradient id="gCherryAct" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4A0A1D" />
      <stop offset="100%" stop-color="#650D25" />
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="198" height="30" rx="15" fill="url(#gCherryAct)" stroke="#FF2D60" stroke-width="1.4" />
  <circle cx="16" cy="16" r="4" fill="#FF2D60" />
  <circle cx="16" cy="16" r="6.5" fill="none" stroke="#FF2D60" stroke-width="0.8" opacity="0.6" />
  <text x="28" y="20" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="700" fill="#FFFFFF" letter-spacing="1">CHERRY ROYALE</text>
  <rect x="142" y="8" width="46" height="16" rx="8" fill="#FF2D60" />
  <text x="148" y="19.5" font-family="'IBM Plex Mono', monospace" font-size="8.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.5">ACTIVE</text>
</svg>'''

    # 2. Espresso Inactive Pill (Click to switch)
    svg_espresso_inactive = '''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="32" viewBox="0 0 220 32">
  <rect x="1" y="1" width="218" height="30" rx="15" fill="#211817" stroke="#873D50" stroke-width="1.2" />
  <text x="16" y="20" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" fill="#FAF2EC" letter-spacing="0.8">☕ MIDNIGHT ÉSPRESSO</text>
  <path d="M 198 13 L 204 16 L 198 19" fill="none" stroke="#D99AA7" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''

    # 3. Cherry Inactive Pill (Click to switch)
    svg_cherry_inactive = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="32" viewBox="0 0 200 32">
  <rect x="1" y="1" width="198" height="30" rx="15" fill="#3a0818" stroke="#C1123F" stroke-width="1.2" />
  <text x="16" y="20" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" fill="#FAF2EC" letter-spacing="0.8">🍒 CHERRY ROYALE</text>
  <path d="M 178 13 L 184 16 L 178 19" fill="none" stroke="#FF2D60" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''

    # 4. Espresso Active Pill (NO GREEN DOT - Theme Accent Dot #C1123F)
    svg_espresso_active = '''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="32" viewBox="0 0 220 32">
  <defs>
    <linearGradient id="gEspressoAct" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#211817" />
      <stop offset="100%" stop-color="#2b1218" />
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="218" height="30" rx="15" fill="url(#gEspressoAct)" stroke="#C1123F" stroke-width="1.4" />
  <circle cx="16" cy="16" r="4" fill="#C1123F" />
  <circle cx="16" cy="16" r="6.5" fill="none" stroke="#C1123F" stroke-width="0.8" opacity="0.6" />
  <text x="28" y="20" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="700" fill="#FFFFFF" letter-spacing="1">MIDNIGHT ÉSPRESSO</text>
  <rect x="162" y="8" width="46" height="16" rx="8" fill="#C1123F" />
  <text x="168" y="19.5" font-family="'IBM Plex Mono', monospace" font-size="8.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.5">ACTIVE</text>
</svg>'''

    # 5. Live Showcase Pill
    svg_live_engine = '''<svg xmlns="http://www.w3.org/2000/svg" width="180" height="32" viewBox="0 0 180 32">
  <rect x="1" y="1" width="178" height="30" rx="15" fill="#1b1215" stroke="#FF2D60" stroke-width="1.2" stroke-dasharray="3 2" />
  <text x="16" y="20" font-family="'IBM Plex Mono', monospace" font-size="10.5" font-weight="700" fill="#FF809B" letter-spacing="0.8">✦ LIVE SHOWCASE</text>
  <path d="M 160 13 L 165 16 L 160 19" fill="none" stroke="#FF2D60" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''

    files = {
        'assets/icons/theme-cherry-active.svg': svg_cherry_active,
        'assets/icons/theme-espresso-inactive.svg': svg_espresso_inactive,
        'assets/icons/theme-cherry-inactive.svg': svg_cherry_inactive,
        'assets/icons/theme-espresso-active.svg': svg_espresso_active,
        'assets/icons/theme-live-engine.svg': svg_live_engine
    }

    for path, content in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    print('Generated updated theme pills with zero green dots!')

if __name__ == '__main__':
    create_theme_pills()

def generate_readme_espresso():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Swap the theme toggle header
    old_toggle = '''<p align="center">
  <a href="README.md" title="Cherry Royale Mode (Active)"><img src="assets/icons/theme-cherry-active.svg" height="30" alt="Cherry Royale Mode (Active)" /></a>
  &nbsp;
  <a href="README-espresso.md" title="Switch to Midnight Éspresso Mode"><img src="assets/icons/theme-espresso-inactive.svg" height="30" alt="Switch to Midnight Éspresso" /></a>
  &nbsp;
  <a href="https://madhura200227.github.io/madhura200227/" title="Launch Interactive Live Web Engine"><img src="assets/icons/theme-live-engine.svg" height="30" alt="Live Interactive Web Engine" /></a>
</p>'''

    new_toggle = '''<p align="center">
  <a href="README.md" title="Switch to Cherry Royale Mode"><img src="assets/icons/theme-cherry-inactive.svg" height="30" alt="Switch to Cherry Royale" /></a>
  &nbsp;
  <a href="README-espresso.md" title="Midnight Éspresso Mode (Active)"><img src="assets/icons/theme-espresso-active.svg" height="30" alt="Midnight Éspresso Mode (Active)" /></a>
  &nbsp;
  <a href="https://madhura200227.github.io/madhura200227/?theme=espresso" title="Launch Interactive Live Web Engine"><img src="assets/icons/theme-live-engine.svg" height="30" alt="Live Interactive Web Engine" /></a>
</p>'''

    espresso_content = content.replace(old_toggle, new_toggle)

    # 2. Swap all -cherry asset names
    asset_replacements = [
        ('hero-banner-cherry.gif', 'hero-banner.gif'),
        ('live-portfolio-badge-cherry.svg', 'live-portfolio-badge.svg'),
        ('connect-linkedin-cherry.svg', 'connect-linkedin.svg'),
        ('connect-email-cherry.svg', 'connect-email.svg'),
        ('connect-github-cherry.svg', 'connect-github.svg'),
        ('section-divider-cherry.svg', 'section-divider.svg'),
        ('procure-flow-cherry.svg', 'procure-flow.svg'),
        ('kesslerx-cherry.svg', 'kesslerx.svg'),
        ('infraguard-cherry.svg', 'infraguard.svg'),
        ('github-stats-cherry.svg', 'github-stats.svg'),
        ('languages-cherry.svg', 'languages.svg'),
        ('snake-cherry.svg', 'snake.svg'),
        ('signature-cherry.svg', 'signature.svg'),
        ('logoColor=ff2d6f', 'logoColor=c1123f'),
        ('badge/Python-4a0a1f', 'badge/Python-211817'),
        ('badge/Java-4a0a1f', 'badge/Java-211817'),
        ('badge/JavaScript-4a0a1f', 'badge/JavaScript-211817'),
        ('badge/TypeScript-4a0a1f', 'badge/TypeScript-211817'),
        ('badge/SQL-4a0a1f', 'badge/SQL-211817'),
        ('badge/C-4a0a1f', 'badge/C-211817'),
        ('badge/HTML5-4a0a1f', 'badge/HTML5-211817'),
        ('badge/CSS3-4a0a1f', 'badge/CSS3-211817'),
        ('badge/React-4a0a1f', 'badge/React-211817'),
        ('badge/Redux_Toolkit-4a0a1f', 'badge/Redux_Toolkit-211817'),
        ('badge/React_Query-4a0a1f', 'badge/React_Query-211817'),
        ('badge/React_Router-4a0a1f', 'badge/React_Router-211817'),
        ('badge/React_Hook_Form-4a0a1f', 'badge/React_Hook_Form-211817'),
        ('badge/Tailwind_CSS-4a0a1f', 'badge/Tailwind_CSS-211817'),
        ('badge/Vite-4a0a1f', 'badge/Vite-211817'),
        ('badge/CesiumJS-4a0a1f', 'badge/CesiumJS-211817'),
        ('badge/Node.js-4a0a1f', 'badge/Node.js-211817'),
        ('badge/Express-4a0a1f', 'badge/Express-211817'),
        ('badge/FastAPI-4a0a1f', 'badge/FastAPI-211817'),
        ('badge/REST_APIs-4a0a1f', 'badge/REST_APIs-211817'),
        ('badge/WebSockets-4a0a1f', 'badge/WebSockets-211817'),
        ('badge/JWT_Auth-4a0a1f', 'badge/JWT_Auth-211817'),
        ('badge/PostgreSQL-4a0a1f', 'badge/PostgreSQL-211817'),
        ('badge/MySQL-4a0a1f', 'badge/MySQL-211817'),
        ('badge/Neon-4a0a1f', 'badge/Neon-211817'),
        ('badge/Supabase-4a0a1f', 'badge/Supabase-211817'),
        ('badge/Firebase-4a0a1f', 'badge/Firebase-211817'),
        ('badge/Row--Level_Security-4a0a1f', 'badge/Row--Level_Security-211817'),
        ('badge/TOTP_MFA-4a0a1f', 'badge/TOTP_MFA-211817'),
        ('badge/Git-4a0a1f', 'badge/Git-211817'),
        ('badge/GitHub-4a0a1f', 'badge/GitHub-211817'),
        ('badge/Selenium-4a0a1f', 'badge/Selenium-211817'),
        ('badge/BeautifulSoup-4a0a1f', 'badge/BeautifulSoup-211817'),
        ('badge/Google_Workspace-4a0a1f', 'badge/Google_Workspace-211817'),
    ]

    for old, new in asset_replacements:
        espresso_content = espresso_content.replace(old, new)

    with open('README-espresso.md', 'w', encoding='utf-8') as f:
        f.write(espresso_content)

    print('Generated README-espresso.md successfully!')

if __name__ == '__main__':
    generate_readme_espresso()


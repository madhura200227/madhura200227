import os

# ==============================================================================
# 1. PROCURE FLOW (Espresso & Cherry) - Mathematically Calibrated
# ==============================================================================
def get_procure_flow(theme="espresso"):
    if theme == "espresso":
        bg_start = "#1b1214"
        bg_mid = "#211817"
        bg_end = "#2e111a"
        card_bg = "#2a141a"
        border = "#873D50"
        accent = "#C1123F"
        accent_bright = "#C1123F"
        pill_bg = "#650D25"
        stack_box_bg = "#1e1316"
        tag_bg = "#2a141a"
    else: # cherry mode: rich wine/cherry red surfaces, zero murky black
        bg_start = "#2c0612"
        bg_mid = "#3a0818"
        bg_end = "#4e0b20"
        card_bg = "#450a1c"
        border = "#C1123F"
        accent = "#C1123F"
        accent_bright = "#FF2D60"
        pill_bg = "#6b0c26"
        stack_box_bg = "#340816"
        tag_bg = "#450a1c"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 370" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="pfBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="50%" stop-color="{bg_mid}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>
  </defs>

  <style>
    .pf-meta {{ font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 12px; font-weight: 500; letter-spacing: 1.5px; fill: #D99AA7; }}
    .pf-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 32px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.5px; }}
    .pf-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; fill: #E8D5C5; }}
    .pf-stage-title {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 14px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.3px; }}
    .pf-stage-sub {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; font-weight: 600; fill: #D99AA7; letter-spacing: 1px; }}
    .pf-stage-text {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 12px; fill: #E8D5C5; }}
    .pf-tag {{ font-family: 'IBM Plex Mono', monospace; font-size: 11.5px; font-weight: 500; fill: #FFF5ED; }}
  </style>

  <rect width="840" height="370" rx="12" fill="url(#pfBg_{theme})" stroke="{border}" stroke-width="1.3" />
  <rect x="0" y="0" width="840" height="3.5" rx="1.5" fill="{accent_bright}" />

  <!-- Corner Brackets -->
  <path d="M 16 28 L 16 16 L 28 16" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 824 28 L 824 16 L 812 16" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 16 342 L 16 354 L 28 354" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 824 342 L 824 354 L 812 354" fill="none" stroke="{accent_bright}" stroke-width="2" />

  <!-- Header Section -->
  <g transform="translate(36, 36)">
    <rect x="0" y="-8" width="6" height="6" fill="{accent_bright}" />
    <text x="14" y="-2" class="pf-meta">PROJECT 01 // ENTERPRISE WORKFLOW</text>
    <text x="0" y="30" class="pf-title">PROCURE FLOW</text>
    <g transform="translate(528, 6)">
      <rect x="0" y="0" width="240" height="26" rx="13" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <circle cx="16" cy="13" r="4" fill="{accent_bright}" />
      <text x="28" y="17" class="pf-meta" fill="#FFF5ED">INSTITUTIONAL PLATFORM</text>
    </g>
    <text x="0" y="60" class="pf-desc">Procurement lifecycle &amp; approval platform for S.P. College with PostgreSQL RLS &amp; MFA.</text>
  </g>

  <!-- 3 Workflow Stages -->
  <g transform="translate(36, 126)">
    <!-- Stage 1 -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="224" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <circle cx="28" cy="28" r="14" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="28" y="32" text-anchor="middle" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="700" fill="#FFF5ED">01</text>
      <text x="52" y="32" class="pf-stage-title">Requisition Init</text>
      <text x="20" y="62" class="pf-stage-sub">DEPARTMENT PORTAL</text>
      <text x="20" y="86" class="pf-stage-text">• Digital Purchase Requests</text>
      <text x="20" y="104" class="pf-stage-text">• Budget Category Allocation</text>
    </g>

    <!-- Flow Arrow 1 -->
    <g transform="translate(230, 60)">
      <line x1="0" y1="0" x2="28" y2="0" stroke="{accent_bright}" stroke-width="2" />
      <polygon points="28,-4 36,0 28,4" fill="{accent_bright}" />
    </g>

    <!-- Stage 2: Security & RLS Highlight -->
    <g transform="translate(272, 0)">
      <rect x="0" y="0" width="224" height="126" rx="8" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.5" />
      <circle cx="28" cy="28" r="14" fill="{accent_bright}" />
      <path d="M 28 20 L 33 22 L 33 28 Q 33 33 28 35 Q 23 33 23 28 L 23 22 Z" fill="#FFF5ED" />
      <text x="52" y="32" class="pf-stage-title">Policy &amp; Security</text>
      <text x="20" y="62" class="pf-stage-sub" fill="#FFF5ED">POSTGRESQL RLS ENFORCED</text>
      <text x="20" y="86" class="pf-stage-text">• Row-Level Security Rules</text>
      <text x="20" y="104" class="pf-stage-text">• TOTP-based Multi-Factor Auth</text>
    </g>

    <!-- Flow Arrow 2 -->
    <g transform="translate(502, 60)">
      <line x1="0" y1="0" x2="28" y2="0" stroke="{accent_bright}" stroke-width="2" />
      <polygon points="28,-4 36,0 28,4" fill="{accent_bright}" />
    </g>

    <!-- Stage 3 -->
    <g transform="translate(544, 0)">
      <rect x="0" y="0" width="224" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <circle cx="28" cy="28" r="14" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="28" y="32" text-anchor="middle" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="700" fill="#FFF5ED">03</text>
      <text x="52" y="32" class="pf-stage-title">Multi-Tier Sign-Off</text>
      <text x="20" y="62" class="pf-stage-sub">AUDITABLE SETTLEMENT</text>
      <text x="20" y="86" class="pf-stage-text">• Hierarchical Approvals</text>
      <text x="20" y="104" class="pf-stage-text">• Neon PostgreSQL Sync</text>
    </g>
  </g>

  <!-- Bottom Stack Strip: Perfectly Fitted (Total width: 614px inside 768px box) -->
  <g transform="translate(36, 282)">
    <rect x="0" y="0" width="768" height="52" rx="8" fill="{stack_box_bg}" stroke="{border}" stroke-width="1.2" />
    <text x="18" y="31" class="pf-meta" fill="#D99AA7">STACK</text>
    <g transform="translate(75, 12)">
      <rect x="0" y="0" width="54" height="28" rx="5" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="27" y="19" class="pf-tag" text-anchor="middle">React</text>

      <rect x="62" y="0" width="64" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="94" y="19" class="pf-tag" text-anchor="middle">Node.js</text>

      <rect x="134" y="0" width="88" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="178" y="19" class="pf-tag" text-anchor="middle">PostgreSQL</text>

      <rect x="230" y="0" width="50" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="255" y="19" class="pf-tag" text-anchor="middle">Neon</text>

      <rect x="288" y="0" width="46" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="311" y="19" class="pf-tag" text-anchor="middle">Vite</text>

      <rect x="342" y="0" width="94" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="389" y="19" class="pf-tag" text-anchor="middle">Tailwind CSS</text>

      <rect x="444" y="0" width="94" height="28" rx="5" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <text x="491" y="19" class="pf-tag" fill="#FFF5ED" text-anchor="middle">Postgres RLS</text>

      <rect x="546" y="0" width="68" height="28" rx="5" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <text x="580" y="19" class="pf-tag" fill="#FFF5ED" text-anchor="middle">TOTP MFA</text>
    </g>
  </g>
</svg>'''


# ==============================================================================
# 2. KESSLERX (Espresso & Cherry) - Zero Text Collision Guaranteed
# ==============================================================================
def get_kesslerx(theme="espresso"):
    if theme == "espresso":
        bg_start = "#1b1214"
        bg_mid = "#211817"
        bg_end = "#2e111a"
        card_bg = "#2a141a"
        border = "#873D50"
        accent = "#C1123F"
        accent_bright = "#C1123F"
        pill_bg = "#650D25"
        stack_box_bg = "#1e1316"
        tag_bg = "#2a141a"
        globe_core = "#650D25"
    else: # cherry mode: rich wine/cherry red surfaces
        bg_start = "#2c0612"
        bg_mid = "#3a0818"
        bg_end = "#4e0b20"
        card_bg = "#450a1c"
        border = "#C1123F"
        accent = "#C1123F"
        accent_bright = "#FF2D60"
        pill_bg = "#6b0c26"
        stack_box_bg = "#340816"
        tag_bg = "#450a1c"
        globe_core = "#780e2b"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 370" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="kxBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="50%" stop-color="{bg_mid}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>

    <radialGradient id="kxGlobe_{theme}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{globe_core}" stop-opacity="0.9" />
      <stop offset="70%" stop-color="{card_bg}" stop-opacity="0.6" />
      <stop offset="100%" stop-color="{bg_start}" stop-opacity="0" />
    </radialGradient>
  </defs>

  <style>
    .kx-meta {{ font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 12px; font-weight: 500; letter-spacing: 1.5px; fill: #D99AA7; }}
    .kx-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 32px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.5px; }}
    .kx-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; fill: #E8D5C5; }}
    .kx-card-title {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 14px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.3px; }}
    .kx-card-sub {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; font-weight: 600; fill: #D99AA7; letter-spacing: 1px; }}
    .kx-card-text {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 12px; fill: #E8D5C5; }}
    .kx-tag {{ font-family: 'IBM Plex Mono', monospace; font-size: 11.5px; font-weight: 500; fill: #FFF5ED; }}
  </style>

  <rect width="840" height="370" rx="12" fill="url(#kxBg_{theme})" stroke="{border}" stroke-width="1.3" />
  <rect x="0" y="0" width="840" height="3.5" rx="1.5" fill="{accent_bright}" />

  <!-- Corner Brackets -->
  <path d="M 16 28 L 16 16 L 28 16" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 824 28 L 824 16 L 812 16" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 16 342 L 16 354 L 28 354" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 824 342 L 824 354 L 812 354" fill="none" stroke="{accent_bright}" stroke-width="2" />

  <!-- Clean Header with Zero Overlap: Overline contains 'PROJECT 02 //', Title is pure 'KESSLERX' -->
  <g transform="translate(36, 36)">
    <rect x="0" y="-8" width="6" height="6" fill="{accent_bright}" />
    <text x="14" y="-2" class="kx-meta">PROJECT 02 // ORBITAL INTELLIGENCE</text>
    <text x="0" y="30" class="kx-title">KESSLERX</text>
    <g transform="translate(538, 6)">
      <rect x="0" y="0" width="230" height="26" rx="13" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <circle cx="16" cy="13" r="4" fill="{accent_bright}" />
      <text x="28" y="17" class="kx-meta" fill="#FFF5ED">AEROSPACE WEB APP</text>
    </g>
    <text x="0" y="60" class="kx-desc">Orbital debris &amp; satellite monitoring for space situational awareness. Presented at Avishkar.</text>
  </g>

  <!-- 3 Interactive Panels -->
  <g transform="translate(36, 126)">
    <!-- Panel 1: Data Ingestion -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="234" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <circle cx="28" cy="28" r="14" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="28" y="32" text-anchor="middle" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="700" fill="#FFF5ED">01</text>
      <text x="52" y="32" class="kx-card-title">Data Ingestion</text>
      <text x="20" y="62" class="kx-card-sub">SPATIOTEMPORAL QUERY</text>
      <text x="20" y="86" class="kx-card-text">• FastAPI REST endpoints</text>
      <text x="20" y="104" class="kx-card-text">• React Query caching layer</text>
    </g>

    <!-- Panel 2: CesiumJS 3D Orbital Engine -->
    <g transform="translate(254, 0)">
      <rect x="0" y="0" width="260" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <circle cx="130" cy="54" r="30" fill="url(#kxGlobe_{theme})" stroke="{border}" stroke-width="1.2" />
      <ellipse cx="130" cy="54" rx="84" ry="24" fill="none" stroke="{accent_bright}" stroke-width="1.3" stroke-dasharray="4 3" transform="rotate(-15 130 54)" />
      <circle cx="195" cy="42" r="3.2" fill="#FFF5ED" />
      <ellipse cx="130" cy="54" rx="76" ry="32" fill="none" stroke="#B88979" stroke-width="1.1" transform="rotate(35 130 54)" />
      <circle cx="85" cy="36" r="2.8" fill="#D99AA7" />
      <text x="130" y="106" text-anchor="middle" class="kx-card-sub" fill="#FFF5ED">CESIUMJS 3D ENGINE</text>
    </g>

    <!-- Panel 3: Event Streaming -->
    <g transform="translate(534, 0)">
      <rect x="0" y="0" width="234" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <circle cx="28" cy="28" r="14" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="28" y="32" text-anchor="middle" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="700" fill="#FFF5ED">03</text>
      <text x="52" y="32" class="kx-card-title">Event Streaming</text>
      <text x="20" y="62" class="kx-card-sub">WEBSOCKETS PIPELINE</text>
      <text x="20" y="86" class="kx-card-text">• Live orbital state delivery</text>
      <text x="20" y="104" class="kx-card-text">• Redux Toolkit state sync</text>
    </g>
  </g>

  <!-- Bottom Stack Strip: Perfectly Fitted (Total width: 610px inside 768px box) -->
  <g transform="translate(36, 282)">
    <rect x="0" y="0" width="768" height="52" rx="8" fill="{stack_box_bg}" stroke="{border}" stroke-width="1.2" />
    <text x="18" y="31" class="kx-meta" fill="#D99AA7">STACK</text>
    <g transform="translate(75, 12)">
      <rect x="0" y="0" width="54" height="28" rx="5" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="27" y="19" class="kx-tag" text-anchor="middle">React</text>

      <rect x="62" y="0" width="82" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="103" y="19" class="kx-tag" text-anchor="middle">TypeScript</text>

      <rect x="152" y="0" width="102" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="203" y="19" class="kx-tag" text-anchor="middle">Redux Toolkit</text>

      <rect x="262" y="0" width="92" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="308" y="19" class="kx-tag" text-anchor="middle">React Query</text>

      <rect x="362" y="0" width="76" height="28" rx="5" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <text x="400" y="19" class="kx-tag" fill="#FFF5ED" text-anchor="middle">CesiumJS</text>

      <rect x="446" y="0" width="66" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="479" y="19" class="kx-tag" text-anchor="middle">FastAPI</text>

      <rect x="520" y="0" width="90" height="28" rx="5" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <text x="565" y="19" class="kx-tag" fill="#FFF5ED" text-anchor="middle">WebSockets</text>
    </g>
  </g>
</svg>'''


# ==============================================================================
# 3. INFRAGUARD AI (Espresso & Cherry) - Zero Tag Overflow Guaranteed
# ==============================================================================
def get_infraguard(theme="espresso"):
    if theme == "espresso":
        bg_start = "#1b1214"
        bg_mid = "#211817"
        bg_end = "#2e111a"
        card_bg = "#2a141a"
        border = "#873D50"
        accent = "#C1123F"
        accent_bright = "#C1123F"
        pill_bg = "#650D25"
        stack_box_bg = "#1e1316"
        tag_bg = "#2a141a"
    else: # cherry mode: rich wine/cherry red surfaces
        bg_start = "#2c0612"
        bg_mid = "#3a0818"
        bg_end = "#4e0b20"
        card_bg = "#450a1c"
        border = "#C1123F"
        accent = "#C1123F"
        accent_bright = "#FF2D60"
        pill_bg = "#6b0c26"
        stack_box_bg = "#340816"
        tag_bg = "#450a1c"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 370" width="100%" height="auto" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="igBg_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="50%" stop-color="{bg_mid}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>

    <linearGradient id="igWave_{theme}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{accent_bright}" stop-opacity="0.32" />
      <stop offset="100%" stop-color="{accent_bright}" stop-opacity="0.0" />
    </linearGradient>
  </defs>

  <style>
    .ig-meta {{ font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 12px; font-weight: 500; letter-spacing: 1.5px; fill: #D99AA7; }}
    .ig-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 32px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.5px; }}
    .ig-desc {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 15px; fill: #E8D5C5; }}
    .ig-card-title {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 14px; font-weight: 700; fill: #FFF5ED; letter-spacing: 0.3px; }}
    .ig-card-sub {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; font-weight: 600; fill: #D99AA7; letter-spacing: 1px; }}
    .ig-card-text {{ font-family: 'Inter', -apple-system, sans-serif; font-size: 12px; fill: #E8D5C5; }}
    .ig-tag {{ font-family: 'IBM Plex Mono', monospace; font-size: 11.5px; font-weight: 500; fill: #FFF5ED; }}
  </style>

  <rect width="840" height="370" rx="12" fill="url(#igBg_{theme})" stroke="{border}" stroke-width="1.3" />
  <rect x="0" y="0" width="840" height="3.5" rx="1.5" fill="{accent_bright}" />

  <!-- Corner Brackets -->
  <path d="M 16 28 L 16 16 L 28 16" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 824 28 L 824 16 L 812 16" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 16 342 L 16 354 L 28 354" fill="none" stroke="{accent_bright}" stroke-width="2" />
  <path d="M 824 342 L 824 354 L 812 354" fill="none" stroke="{accent_bright}" stroke-width="2" />

  <!-- Clean Header -->
  <g transform="translate(36, 36)">
    <rect x="0" y="-8" width="6" height="6" fill="{accent_bright}" />
    <text x="14" y="-2" class="ig-meta">PROJECT 03 // PREDICTIVE RESILIENCE</text>
    <text x="0" y="30" class="ig-title">INFRAGUARD AI</text>
    <g transform="translate(528, 6)">
      <rect x="0" y="0" width="240" height="26" rx="13" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <circle cx="16" cy="13" r="4" fill="{accent_bright}" />
      <text x="28" y="17" class="ig-meta" fill="#FFF5ED">RESILIENCE PLATFORM</text>
    </g>
    <text x="0" y="60" class="ig-desc">Failure prediction &amp; structural monitoring alerts for roads, bridges and pipelines.</text>
  </g>

  <!-- Dual Display Panels -->
  <g transform="translate(36, 126)">
    <!-- Left Display: Sensor Waveform -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="430" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <text x="18" y="22" class="ig-card-sub">STRUCTURAL VIBRATION TELEMETRY</text>
      <line x1="18" y1="46" x2="412" y2="46" stroke="{border}" stroke-width="1" stroke-dasharray="3 3" />
      <text x="412" y="42" text-anchor="end" font-family="'IBM Plex Mono', monospace" font-size="10" fill="#D99AA7">ANOMALY THRESHOLD</text>
      <line x1="18" y1="80" x2="412" y2="80" stroke="{border}" stroke-width="1" stroke-opacity="0.3" />

      <path d="M 18 100 Q 60 98 100 84 T 180 90 T 260 70 T 310 36 T 350 64 T 412 50 L 412 114 L 18 114 Z" fill="url(#igWave_{theme})" />
      <path d="M 18 100 Q 60 98 100 84 T 180 90 T 260 70 T 310 36 T 350 64 T 412 50" fill="none" stroke="{accent_bright}" stroke-width="2" stroke-linecap="round" />
      <circle cx="310" cy="36" r="4.5" fill="#FFF5ED" stroke="{accent_bright}" stroke-width="2" />
      <text x="310" y="24" text-anchor="middle" font-family="'IBM Plex Mono', monospace" font-size="10" font-weight="600" fill="#FFF5ED">SPIKE DETECTED</text>
    </g>

    <!-- Right Display: Analytical Core -->
    <g transform="translate(448, 0)">
      <rect x="0" y="0" width="320" height="126" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1.2" />
      <circle cx="28" cy="28" r="14" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="28" y="32" text-anchor="middle" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="700" fill="#FFF5ED">AI</text>
      <text x="52" y="32" class="ig-card-title">Diagnostic Engine</text>
      <text x="20" y="60" class="ig-card-sub">PREDICTIVE CAPABILITIES</text>
      <text x="20" y="82" class="ig-card-text">• Sensor Telemetry Ingestion</text>
      <text x="20" y="99" class="ig-card-text">• Degradation Trend Modeling</text>
      <text x="20" y="116" class="ig-card-text">• Automated Maintenance Alerts</text>
    </g>
  </g>

  <!-- Bottom Stack Strip: Perfectly Fitted (Total width: 598px inside 768px box - ZERO Overflow) -->
  <g transform="translate(36, 282)">
    <rect x="0" y="0" width="768" height="52" rx="8" fill="{stack_box_bg}" stroke="{border}" stroke-width="1.2" />
    <text x="18" y="31" class="ig-meta" fill="#D99AA7">STACK</text>
    <g transform="translate(75, 12)">
      <rect x="0" y="0" width="54" height="28" rx="5" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="27" y="19" class="ig-tag" text-anchor="middle">React</text>

      <rect x="62" y="0" width="58" height="28" rx="5" fill="{pill_bg}" stroke="{accent_bright}" stroke-width="1.2" />
      <text x="91" y="19" class="ig-tag" fill="#FFF5ED" text-anchor="middle">Python</text>

      <rect x="128" y="0" width="80" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="168" y="19" class="ig-tag" text-anchor="middle">REST APIs</text>

      <rect x="216" y="0" width="128" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="280" y="19" class="ig-tag" text-anchor="middle">Failure Prediction</text>

      <rect x="352" y="0" width="140" height="28" rx="5" fill="{tag_bg}" stroke="{border}" stroke-width="1" />
      <text x="422" y="19" class="ig-tag" text-anchor="middle">Structural Monitoring</text>

      <rect x="500" y="0" width="98" height="28" rx="5" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="549" y="19" class="ig-tag" text-anchor="middle">Alert Dispatch</text>
    </g>
  </g>
</svg>'''


# ==============================================================================
# 4. CONNECT BUTTONS (Espresso & Cherry) - 100% Unified Styling & Dimensions
# ==============================================================================
def get_connect_button(platform, theme="espresso"):
    if theme == "espresso":
        bg = "#2b1218"
        border = "#873D50"
        arrow_col = "#D99AA7"
    else: # cherry mode: rich burgundy-wine fill with vivid cherry border
        bg = "#4a0b1f"
        border = "#FF2D60"
        arrow_col = "#E8D5C5"

    label = platform.upper()
    
    # Path for each icon (crisp white vector paths)
    if platform == "linkedin":
        icon_svg = '''
        <path d="M14 6a4 4 0 0 1 4 4v7h-3v-7a1.5 1.5 0 0 0-1.5-1.5 1.5 1.5 0 0 0-1.5 1.5v7h-3v-7a4 4 0 0 1 4-4z" fill="none" stroke="#FFF5ED" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        <rect x="2" y="7" width="3" height="10" fill="#FFF5ED"/>
        <circle cx="3.5" cy="3" r="1.6" fill="#FFF5ED"/>'''
    elif platform == "email":
        icon_svg = '''
        <rect x="1" y="2" width="16" height="13" rx="2" fill="none" stroke="#FFF5ED" stroke-width="1.6"/>
        <polyline points="1,4 9,10 17,4" fill="none" stroke="#FFF5ED" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'''
    else: # github
        icon_svg = '''
        <path d="M7 15c-3.8 1.1-3.8-1.9-5.3-2.3m10.6 4.6v-3a2.6 2.6 0 0 0-.7-2c2.4-.3 4.9-1.2 4.9-5.4a4.2 4.2 0 0 0-1.1-2.9 3.9 3.9 0 0 0-.1-2.9s-.9-.3-3 1.1a10.3 10.3 0 0 0-5.4 0c-2.1-1.4-3-1.1-3-1.1a3.9 3.9 0 0 0-.1 2.9 4.2 4.2 0 0 0-1.1 2.9c0 4.2 2.5 5.1 4.9 5.4a2.6 2.6 0 0 0-.7 2v3" fill="none" stroke="#FFF5ED" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="170" height="38" viewBox="0 0 170 38">
  <rect width="170" height="38" rx="6" fill="{bg}" stroke="{border}" stroke-width="1.3" />
  <g transform="translate(15, 10)">
    {icon_svg}
  </g>
  <text x="44" y="23" font-family="'IBM Plex Mono', 'SF Mono', monospace" font-size="12" font-weight="600" fill="#FFF5ED" letter-spacing="1.5">{label}</text>
  <path d="M 148 16 L 153 19 L 148 22" fill="none" stroke="{arrow_col}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''


# ==============================================================================
# 5. WRITE ALL FILES
# ==============================================================================
os.makedirs("assets/projects", exist_ok=True)
os.makedirs("assets/icons", exist_ok=True)

# Procure Flow
with open("assets/projects/procure-flow.svg", "w", encoding="utf-8") as f:
    f.write(get_procure_flow("espresso"))
with open("assets/projects/procure-flow-cherry.svg", "w", encoding="utf-8") as f:
    f.write(get_procure_flow("cherry"))

# KesslerX
with open("assets/projects/kesslerx.svg", "w", encoding="utf-8") as f:
    f.write(get_kesslerx("espresso"))
with open("assets/projects/kesslerx-cherry.svg", "w", encoding="utf-8") as f:
    f.write(get_kesslerx("cherry"))

# InfraGuard AI
with open("assets/projects/infraguard.svg", "w", encoding="utf-8") as f:
    f.write(get_infraguard("espresso"))
with open("assets/projects/infraguard-cherry.svg", "w", encoding="utf-8") as f:
    f.write(get_infraguard("cherry"))

# Connect Buttons (Espresso)
with open("assets/icons/connect-linkedin.svg", "w", encoding="utf-8") as f:
    f.write(get_connect_button("linkedin", "espresso"))
with open("assets/icons/connect-email.svg", "w", encoding="utf-8") as f:
    f.write(get_connect_button("email", "espresso"))
with open("assets/icons/connect-github.svg", "w", encoding="utf-8") as f:
    f.write(get_connect_button("github", "espresso"))

# Connect Buttons (Cherry)
with open("assets/icons/connect-linkedin-cherry.svg", "w", encoding="utf-8") as f:
    f.write(get_connect_button("linkedin", "cherry"))
with open("assets/icons/connect-email-cherry.svg", "w", encoding="utf-8") as f:
    f.write(get_connect_button("email", "cherry"))
with open("assets/icons/connect-github-cherry.svg", "w", encoding="utf-8") as f:
    f.write(get_connect_button("github", "cherry"))

print("All projects & buttons built cleanly for both Espresso & Cherry Red modes!")

import os
import base64
from PIL import Image

# Directories
git_root = r'd:/Github_Profile/princekr77'
git_assets = os.path.join(git_root, 'assets')
git_projects = os.path.join(git_assets, 'projects')
prev_brain = r'C:/Users/hp/.gemini/antigravity/brain/5c05c378-917b-4f19-bde5-0f49a86fe810'
desk_build = r'C:/Users/hp/Desktop/PRINCE_EXE_BUILD'
desk_projects = os.path.join(desk_build, 'projects')

os.makedirs(git_assets, exist_ok=True)
os.makedirs(git_projects, exist_ok=True)
os.makedirs(desk_build, exist_ok=True)
os.makedirs(desk_projects, exist_ok=True)

# Helper to read base64
def get_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def save_svg(filenames, content):
    for fn in filenames:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        print(f"Saved: {os.path.basename(fn)} ({len(content)} bytes)")

# Load assets
avatar_b64 = get_b64(os.path.join(prev_brain, 'avatar_box_full.png'))
castle_b64 = get_b64(os.path.join(prev_brain, 'fantasy_castle.png'))

proj_b64 = {}
for p_name in ['silent-city', 'monster-hunter', 'sword-warrior', 'legends-tretayug', 'triathlon', 'vr-puzzle']:
    img_path = os.path.join(git_projects, f"{p_name}.png")
    if os.path.exists(img_path):
        proj_b64[p_name] = get_b64(img_path)
    else:
        # fallback to prev_brain
        proj_b64[p_name] = get_b64(os.path.join(prev_brain, f"{p_name}.png"))

# Common SVG defs (gradients & filters)
def common_defs(prefix):
    return f'''
    <linearGradient id="{prefix}_bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#040914"/>
      <stop offset="50%" stop-color="#061226"/>
      <stop offset="100%" stop-color="#081A38"/>
    </linearGradient>
    <linearGradient id="{prefix}_border" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="50%" stop-color="#0080FF"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>
    <linearGradient id="{prefix}_cyan_text" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="100%" stop-color="#43C6FF"/>
    </linearGradient>
    <linearGradient id="{prefix}_gold_badge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFE57F"/>
      <stop offset="50%" stop-color="#FFB800"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="{prefix}_gold_bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#241604"/>
      <stop offset="100%" stop-color="#0D0701"/>
    </linearGradient>
    <linearGradient id="{prefix}_wave_blue" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#0080FF" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="{prefix}_wave_orange" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FF8C00" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#FF3E00" stop-opacity="0.05"/>
    </linearGradient>
    <filter id="{prefix}_glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="{prefix}_softglow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="{prefix}_grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#00F0FF" stroke-width="0.5" opacity="0.07"/>
    </pattern>
    '''

# ==============================================================================
# 1. CARD 1: HERO & STATUS BANNER (card1-intro.svg, header.svg)
# ==============================================================================
card1_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 310" width="100%" height="auto">
  <defs>
    {common_defs('c1')}
    <linearGradient id="c1_fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#040914" stop-opacity="1"/>
      <stop offset="35%" stop-color="#040914" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#040914" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="c1_frame_clip">
      <path d="M 24 10 L 926 10 L 942 26 L 942 294 L 926 302 L 24 302 L 8 294 L 8 26 Z"/>
    </clipPath>
  </defs>

  <!-- Outer HUD Frame -->
  <path d="M 24 10 L 926 10 L 942 26 L 942 294 L 926 302 L 24 302 L 8 294 L 8 26 Z" fill="url(#c1_bg)" stroke="#1677FF" stroke-width="1.8" filter="url(#c1_softglow)"/>
  <path d="M 24 10 L 926 10 L 942 26 L 942 294 L 926 302 L 24 302 L 8 294 L 8 26 Z" fill="url(#c1_grid)"/>

  <!-- Right Fantasy Artwork with blend -->
  <g clip-path="url(#c1_frame_clip)">
    <image href="data:image/png;base64,{castle_b64}" x="570" y="10" width="372" height="292" preserveAspectRatio="xMidYMid slice" opacity="0.9" />
    <rect x="560" y="10" width="120" height="292" fill="url(#c1_fade)"/>
  </g>

  <!-- Corner Brackets -->
  <path d="M 8 40 L 8 16 L 36 10" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 10 L 942 16 L 942 40" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 8 270 L 8 294 L 36 302" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 302 L 942 294 L 942 270" stroke="#00F0FF" stroke-width="3" fill="none"/>

  <!-- Top System Bar -->
  <g transform="translate(24, 28)">
    <!-- Controller Icon -->
    <path d="M 4 8 C 4 4 7 1 11 1 L 21 1 C 25 1 28 4 28 8 L 29 14 C 30 18 28 21 24 21 L 22 21 L 19 17 L 13 17 L 10 21 L 8 21 C 4 21 2 18 3 14 Z" fill="none" stroke="#00F0FF" stroke-width="1.8"/>
    <circle cx="11" cy="9" r="1.5" fill="#00F0FF"/>
    <circle cx="21" cy="9" r="1.5" fill="#00F0FF"/>
    <text x="36" y="15" font-family="'Orbitron', ui-monospace, 'Consolas', monospace" font-size="13" font-weight="900" fill="#FFFFFF" letter-spacing="2">PRINCE.EXE</text>
  </g>

  <!-- System Online Pill -->
  <g transform="translate(805, 20)">
    <rect x="0" y="0" width="122" height="22" rx="11" fill="#031A0F" stroke="#00FF66" stroke-width="1.2"/>
    <circle cx="14" cy="11" r="4.5" fill="#00FF66" filter="url(#c1_softglow)"/>
    <text x="26" y="15" font-family="'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="900" fill="#00FF66" letter-spacing="1.2">SYSTEM ONLINE</text>
  </g>

  <!-- Left: Holographic Avatar HUD Box -->
  <g transform="translate(32, 54)">
    <image href="data:image/png;base64,{avatar_b64}" x="0" y="0" width="250" height="222" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- Center Hero Information -->
  <g transform="translate(305, 78)">
    <!-- Main Title -->
    <text x="0" y="44" font-family="'Impact', 'Arial Black', sans-serif" font-size="44" font-weight="900" fill="#FFFFFF" letter-spacing="2" filter="url(#c1_softglow)">PRINCE GUPTA</text>
    
    <!-- Subtitle with arrow -->
    <g transform="translate(0, 68)">
      <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="20" font-style="italic" font-weight="bold" fill="url(#c1_cyan_text)" letter-spacing="1.5">UNITY GAME DEVELOPER <tspan fill="#00F0FF">&gt;</tspan></text>
    </g>

    <!-- Tagline -->
    <text x="0" y="96" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#A9C9EA" font-weight="500">Building worlds. Creating mechanics. Bringing games to life.</text>

    <!-- Tech Badges Row -->
    <g transform="translate(0, 122)">
      <!-- Unity Badge -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="92" height="32" rx="7" fill="#081730" stroke="#1677FF" stroke-width="1.2"/>
        <path d="M 12 16 L 20 8 L 26 12 L 20 16 L 26 20 L 20 24 Z" fill="#FFFFFF"/>
        <text x="32" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Unity</text>
      </g>

      <!-- C# Badge -->
      <g transform="translate(102, 0)">
        <rect x="0" y="0" width="76" height="32" rx="7" fill="#081730" stroke="#1677FF" stroke-width="1.2"/>
        <rect x="10" y="7" width="18" height="18" rx="4" fill="#68217A"/>
        <text x="14" y="20" font-family="Arial, sans-serif" font-size="11" font-weight="900" fill="#FFFFFF">C#</text>
        <text x="36" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">C#</text>
      </g>

      <!-- Blender Badge -->
      <g transform="translate(188, 0)">
        <rect x="0" y="0" width="102" height="32" rx="7" fill="#081730" stroke="#1677FF" stroke-width="1.2"/>
        <circle cx="20" cy="16" r="8" fill="#E87D0D"/>
        <circle cx="20" cy="16" r="4" fill="#081730"/>
        <circle cx="20" cy="16" r="2" fill="#FFFFFF"/>
        <text x="36" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Blender</text>
      </g>

      <!-- GitHub Badge -->
      <g transform="translate(300, 0)">
        <rect x="0" y="0" width="96" height="32" rx="7" fill="#081730" stroke="#1677FF" stroke-width="1.2"/>
        <path d="M 18 9 C 13.6 9 10 12.6 10 17 C 10 20.5 12.3 23.5 15.5 24.6 C 15.9 24.7 16 24.4 16 24.2 L 16 22.8 C 13.8 23.3 13.3 21.8 13.3 21.8 C 12.9 20.9 12.4 20.6 12.4 20.6 C 11.7 20.1 12.5 20.1 12.5 20.1 C 13.3 20.2 13.7 20.9 13.7 20.9 C 14.4 22.1 15.5 21.8 16 21.5 C 16.1 21 16.3 20.6 16.5 20.4 C 14.7 20.2 12.8 19.5 12.8 16.4 C 12.8 15.5 13.1 14.8 13.7 14.2 C 13.6 14 13.3 13.2 13.8 12.1 C 13.8 12.1 14.5 11.9 16.1 13 C 16.8 12.8 17.5 12.7 18.2 12.7 C 18.9 12.7 19.6 12.8 20.3 13 C 21.9 11.9 22.6 12.1 22.6 12.1 C 23.1 13.2 22.8 14 22.7 14.2 C 23.3 14.8 23.6 15.5 23.6 16.4 C 23.6 19.5 21.7 20.2 19.9 20.4 C 20.2 20.6 20.5 21.1 20.5 21.9 L 20.5 24.2 C 20.5 24.4 20.6 24.7 21 24.6 C 24.2 23.5 26.5 20.5 26.5 17 C 26.5 12.6 22.9 9 18.5 9 Z" fill="#FFFFFF"/>
        <text x="36" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">GitHub</text>
      </g>
    </g>
  </g>
</svg>'''

save_svg([os.path.join(git_assets, 'card1-intro.svg'), os.path.join(git_assets, 'header.svg'),
          os.path.join(desk_build, 'card1-intro.svg'), os.path.join(desk_build, 'header.svg')], card1_svg)

# ==============================================================================
# 2. CARD 2: PLAYER PROFILE & OBJECTIVE (card2-about.svg, player-profile.svg)
# ==============================================================================
card2_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 300" width="100%" height="auto">
  <defs>
    {common_defs('c2')}
  </defs>

  <!-- Outer HUD Frame -->
  <path d="M 24 10 L 926 10 L 942 26 L 942 284 L 926 292 L 24 292 L 8 284 L 8 26 Z" fill="url(#c2_bg)" stroke="#1677FF" stroke-width="1.8" filter="url(#c2_softglow)"/>
  <path d="M 24 10 L 926 10 L 942 26 L 942 284 L 926 292 L 24 292 L 8 284 L 8 26 Z" fill="url(#c2_grid)"/>

  <!-- Corner Brackets -->
  <path d="M 8 36 L 8 16 L 36 10" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 10 L 942 16 L 942 36" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 8 264 L 8 284 L 36 292" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 292 L 942 284 L 942 264" stroke="#00F0FF" stroke-width="3" fill="none"/>

  <!-- Header -->
  <g transform="translate(36, 42)">
    <!-- Trophy Icon -->
    <path d="M 2 4 L 18 4 C 18 9 14 14 10 14 C 6 14 2 9 2 4 Z M 10 14 L 10 18 M 5 18 L 15 18 M 2 6 L 0 6 C 0 9 2 11 4 11 L 4 9 M 18 6 L 20 6 C 20 9 18 11 16 11 L 16 9" fill="none" stroke="#00F0FF" stroke-width="2"/>
    <text x="28" y="15" font-family="'Impact', 'Arial Black', sans-serif" font-size="19" font-weight="900" fill="#00F0FF" letter-spacing="1.5">PLAYER PROFILE <tspan fill="#1677FF">&gt;&gt;</tspan></text>
  </g>

  <!-- Left Column: Character Data Attributes -->
  <g transform="translate(40, 84)">
    <!-- Name -->
    <g transform="translate(0, 0)">
      <text x="0" y="16" font-size="14">👤</text>
      <text x="26" y="15" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="700" fill="#7C95B6">Name</text>
      <text x="135" y="15" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="700" fill="#FFFFFF">: Prince Gupta</text>
    </g>

    <!-- Education -->
    <g transform="translate(0, 32)">
      <text x="0" y="16" font-size="14">🎓</text>
      <text x="26" y="15" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="700" fill="#7C95B6">Education</text>
      <text x="135" y="15" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="700" fill="#FFFFFF">: B.Tech Computer Science</text>
    </g>

    <!-- Institution -->
    <g transform="translate(0, 64)">
      <text x="0" y="16" font-size="14">🏛️</text>
      <text x="26" y="15" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="700" fill="#7C95B6">Institution</text>
      <text x="135" y="15" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="700" fill="#FFFFFF">: KIET Group of Institutions</text>
    </g>

    <!-- Role -->
    <g transform="translate(0, 96)">
      <text x="0" y="16" font-size="14">🎮</text>
      <text x="26" y="15" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="700" fill="#7C95B6">Role</text>
      <text x="135" y="15" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="800" fill="#00F0FF">: Unity Game Developer</text>
    </g>

    <!-- Focus -->
    <g transform="translate(0, 128)">
      <text x="0" y="16" font-size="14">🕹️</text>
      <text x="26" y="15" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="700" fill="#7C95B6">Focus</text>
      <text x="135" y="15" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="700" fill="#FFFFFF">: 2D &amp; 3D Game Dev, Gameplay Systems</text>
    </g>

    <!-- Location -->
    <g transform="translate(0, 160)">
      <text x="0" y="16" font-size="14">📍</text>
      <text x="26" y="15" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="700" fill="#7C95B6">Base Loc</text>
      <text x="135" y="15" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="700" fill="#A9C9EA">: UP, India · Open for Global Roles</text>
    </g>
  </g>

  <!-- Vertical Divider with Tech Pulse -->
  <line x1="495" y1="65" x2="495" y2="265" stroke="#1677FF" stroke-width="1.2" opacity="0.5"/>
  <circle cx="495" cy="165" r="3.5" fill="#00F0FF" filter="url(#c2_softglow)"/>

  <!-- Right Column: Current Objective & Status Capsules -->
  <g transform="translate(525, 75)">
    <!-- Sub-Panel: Current Objective -->
    <rect x="0" y="0" width="385" height="110" rx="8" fill="#08152B" stroke="#1677FF" stroke-width="1.4"/>
    
    <!-- Target icon & header -->
    <g transform="translate(18, 16)">
      <circle cx="8" cy="8" r="7" fill="none" stroke="#00F0FF" stroke-width="1.8"/>
      <circle cx="8" cy="8" r="3.5" fill="#00F0FF"/>
      <text x="24" y="13" font-family="'Impact', 'Arial Black', sans-serif" font-size="15" font-weight="900" fill="#00F0FF" letter-spacing="1">CURRENT OBJECTIVE</text>
    </g>

    <!-- Objective Text -->
    <text x="18" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" fill="#FFFFFF" font-weight="500">Developing engaging gameplay experiences</text>
    <text x="18" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" fill="#FFFFFF" font-weight="500">and exploring new technologies in game development.</text>

    <!-- Secondary Meta Pills -->
    <g transform="translate(0, 126)">
      <!-- Pill 1: Level -->
      <rect x="0" y="0" width="185" height="28" rx="6" fill="#0B1A35" stroke="#0080FF" stroke-width="1.2"/>
      <text x="10" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#00F0FF">⚔️ LEVEL 22 GAME DEV</text>

      <!-- Pill 2: Class -->
      <rect x="195" y="0" width="190" height="28" rx="6" fill="#0B1A35" stroke="#0080FF" stroke-width="1.2"/>
      <text x="10" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#00F0FF">🛡️ GAMEPLAY ARCHITECT</text>
    </g>

    <g transform="translate(0, 162)">
      <!-- Pill 3: Lead -->
      <rect x="0" y="0" width="385" height="28" rx="6" fill="#0B1A35" stroke="#00FF66" stroke-width="1.2"/>
      <text x="12" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#00FF66">⚡ LEAD &amp; INTERN · AKIYAM SOLUTIONS · QUEST ACTIVE</text>
    </g>
  </g>
</svg>'''

save_svg([os.path.join(git_assets, 'card2-about.svg'), os.path.join(git_assets, 'player-profile.svg'),
          os.path.join(desk_build, 'card2-about.svg'), os.path.join(desk_build, 'player-profile.svg')], card2_svg)

# ==============================================================================
# 3. CARD 3: SKILL TREE & TECH MATRIX (card3-stack.svg, skill-tree.svg)
# ==============================================================================
card3_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 440" width="100%" height="auto">
  <defs>
    {common_defs('c3')}
    <radialGradient id="c3_core_glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#0066FF" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#040914" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Outer HUD Frame -->
  <path d="M 24 10 L 926 10 L 942 26 L 942 424 L 926 432 L 24 432 L 8 424 L 8 26 Z" fill="url(#c3_bg)" stroke="#1677FF" stroke-width="1.8" filter="url(#c3_softglow)"/>
  <path d="M 24 10 L 926 10 L 942 26 L 942 424 L 926 432 L 24 432 L 8 424 L 8 26 Z" fill="url(#c3_grid)"/>

  <!-- Corner Brackets -->
  <path d="M 8 36 L 8 16 L 36 10" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 10 L 942 16 L 942 36" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 8 404 L 8 424 L 36 432" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 432 L 942 424 L 942 404" stroke="#00F0FF" stroke-width="3" fill="none"/>

  <!-- Header -->
  <g transform="translate(36, 42)">
    <circle cx="8" cy="8" r="6" fill="none" stroke="#00F0FF" stroke-width="2"/>
    <circle cx="8" cy="8" r="2.5" fill="#00F0FF"/>
    <text x="26" y="15" font-family="'Impact', 'Arial Black', sans-serif" font-size="19" font-weight="900" fill="#00F0FF" letter-spacing="1.5">SKILL TREE <tspan fill="#1677FF">&gt;&gt;</tspan></text>
  </g>

  <!-- Header Right: Level Up Your Skills -->
  <text x="914" y="42" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="900" fill="#00F0FF" letter-spacing="2" text-anchor="end">LEVEL UP YOUR SKILLS</text>

  <!-- CIRCUIT CONNECTING TRACES -->
  <g stroke="#00F0FF" stroke-width="2" fill="none" opacity="0.85" filter="url(#c3_softglow)">
    <!-- Left Branches to Center (475, 245) -->
    <path d="M 270 132 L 350 132 L 395 210 L 415 228"/>
    <path d="M 270 202 L 360 202 L 410 236"/>
    <path d="M 270 272 L 360 272 L 410 254"/>
    <path d="M 270 342 L 350 342 L 395 280 L 415 262"/>

    <!-- Right Branches to Center (475, 245) -->
    <path d="M 680 132 L 600 132 L 555 210 L 535 228"/>
    <path d="M 680 202 L 590 202 L 540 236"/>
    <path d="M 680 272 L 590 272 L 540 254"/>
    <path d="M 680 342 L 600 342 L 555 280 L 535 262"/>

    <!-- Junction Dots -->
    <circle cx="350" cy="132" r="3" fill="#00F0FF"/>
    <circle cx="360" cy="202" r="3" fill="#00F0FF"/>
    <circle cx="360" cy="272" r="3" fill="#00F0FF"/>
    <circle cx="350" cy="342" r="3" fill="#00F0FF"/>

    <circle cx="600" cy="132" r="3" fill="#00F0FF"/>
    <circle cx="590" cy="202" r="3" fill="#00F0FF"/>
    <circle cx="590" cy="272" r="3" fill="#00F0FF"/>
    <circle cx="600" cy="342" r="3" fill="#00F0FF"/>
  </g>

  <!-- CENTER REACTOR CORE -->
  <g transform="translate(475, 245)">
    <circle cx="0" cy="0" r="105" fill="url(#c3_core_glow)"/>
    <circle cx="0" cy="0" r="76" fill="none" stroke="#00F0FF" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.7"/>
    <circle cx="0" cy="0" r="68" fill="none" stroke="#0080FF" stroke-width="2.5"/>
    <circle cx="0" cy="0" r="58" fill="#051530" stroke="#00F0FF" stroke-width="3" filter="url(#c3_glow)"/>

    <!-- Unity 3D Emblem inside Core -->
    <g transform="translate(-24, -36)">
      <path d="M 24 8 L 38 16 L 38 32 L 24 40 L 10 32 L 10 16 Z" fill="none" stroke="#00F0FF" stroke-width="2"/>
      <path d="M 24 8 L 24 40 M 10 16 L 38 32 M 38 16 L 10 32" stroke="#00F0FF" stroke-width="1.5"/>
      <path d="M 24 16 L 31 20 L 31 28 L 24 32 L 17 28 L 17 20 Z" fill="#FFFFFF"/>
    </g>

    <text x="0" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">UNITY</text>
    <text x="0" y="38" font-family="'Orbitron', Consolas, monospace" font-size="9" font-weight="900" fill="#00F0FF" text-anchor="middle" letter-spacing="1.5">GAME DEVELOPMENT</text>
  </g>

  <!-- LEFT 4 SKILL NODES -->
  <!-- Node 1: C# Programming -->
  <g transform="translate(50, 110)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <path d="M 22 10 L 34 16 L 34 28 L 22 34 L 10 28 L 10 16 Z" fill="#68217A" stroke="#B14FC5" stroke-width="1.5"/>
    <text x="22" y="26" font-family="Arial, sans-serif" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle">C#</text>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">C# Programming</text>
  </g>

  <!-- Node 2: Game Mechanics -->
  <g transform="translate(50, 180)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <rect x="0" y="0" width="24" height="20" rx="6" fill="#0B2347" stroke="#00F0FF" stroke-width="1.2"/>
      <circle cx="7" cy="10" r="1.5" fill="#00F0FF"/>
      <circle cx="17" cy="10" r="1.5" fill="#00F0FF"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Game Mechanics</text>
  </g>

  <!-- Node 3: AI Systems -->
  <g transform="translate(50, 250)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <circle cx="12" cy="10" r="9" fill="#0B2347" stroke="#00F0FF" stroke-width="1.2"/>
      <path d="M 8 10 C 8 7 16 7 16 10 C 16 13 8 13 8 10 Z" fill="none" stroke="#00F0FF" stroke-width="1"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">AI Systems</text>
  </g>

  <!-- Node 4: Physics -->
  <g transform="translate(50, 320)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <ellipse cx="12" cy="10" rx="9" ry="4" fill="none" stroke="#00F0FF" stroke-width="1.2" transform="rotate(30 12 10)"/>
      <ellipse cx="12" cy="10" rx="9" ry="4" fill="none" stroke="#00F0FF" stroke-width="1.2" transform="rotate(-30 12 10)"/>
      <circle cx="12" cy="10" r="2" fill="#00F0FF"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Physics</text>
  </g>

  <!-- RIGHT 4 SKILL NODES -->
  <!-- Node 5: Animation -->
  <g transform="translate(680, 110)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <circle cx="12" cy="5" r="2.5" fill="#00F0FF"/>
      <path d="M 8 10 L 12 8 L 15 11 L 18 10 M 12 11 L 10 17 L 7 19 M 12 11 L 14 15 L 17 17" stroke="#00F0FF" stroke-width="1.5" fill="none"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Animation</text>
  </g>

  <!-- Node 6: UI Systems -->
  <g transform="translate(680, 180)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <rect x="2" y="2" width="20" height="13" rx="2" fill="#0B2347" stroke="#00F0FF" stroke-width="1.2"/>
      <line x1="8" y1="18" x2="16" y2="18" stroke="#00F0FF" stroke-width="1.4"/>
      <line x1="12" y1="15" x2="12" y2="18" stroke="#00F0FF" stroke-width="1.4"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">UI Systems</text>
  </g>

  <!-- Node 7: VR Development -->
  <g transform="translate(680, 250)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <rect x="2" y="4" width="20" height="12" rx="4" fill="#0B2347" stroke="#00F0FF" stroke-width="1.2"/>
      <circle cx="8" cy="10" r="2.5" fill="#00F0FF"/>
      <circle cx="16" cy="10" r="2.5" fill="#00F0FF"/>
      <path d="M 6 4 C 6 1 18 1 18 4" stroke="#00F0FF" stroke-width="1" fill="none"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">VR Development</text>
  </g>

  <!-- Node 8: Level Design -->
  <g transform="translate(680, 320)">
    <rect x="0" y="0" width="220" height="44" rx="8" fill="#081730" stroke="#00F0FF" stroke-width="1.6"/>
    <g transform="translate(14, 12)">
      <path d="M 12 2 L 21 7 L 21 16 L 12 21 L 3 16 L 3 7 Z" fill="#0B2347" stroke="#00F0FF" stroke-width="1.2"/>
      <path d="M 12 2 L 12 21 M 3 7 L 12 12 L 21 7" stroke="#00F0FF" stroke-width="1"/>
    </g>
    <text x="46" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Level Design</text>
  </g>
</svg>'''

save_svg([os.path.join(git_assets, 'card3-stack.svg'), os.path.join(git_assets, 'skill-tree.svg'),
          os.path.join(desk_build, 'card3-stack.svg'), os.path.join(desk_build, 'skill-tree.svg')], card3_svg)

# ==============================================================================
# 4. CARD 4: MISSION SELECT — GAME PORTFOLIO (card4-missions.svg, mission-header.svg)
# ==============================================================================
mission_header_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 56" width="100%" height="auto">
  <defs>
    {common_defs('mh')}
  </defs>

  <path d="M 20 8 L 930 8 L 944 22 L 944 42 L 930 52 L 20 52 L 6 42 L 6 22 Z" fill="url(#mh_bg)" stroke="#1677FF" stroke-width="1.6"/>
  
  <g transform="translate(28, 16)">
    <circle cx="12" cy="12" r="10" fill="none" stroke="#00F0FF" stroke-width="2"/>
    <circle cx="12" cy="12" r="4" fill="#00F0FF"/>
    <line x1="12" y1="0" x2="12" y2="6" stroke="#00F0FF" stroke-width="2"/>
    <line x1="12" y1="18" x2="12" y2="24" stroke="#00F0FF" stroke-width="2"/>
    <line x1="0" y1="12" x2="6" y2="12" stroke="#00F0FF" stroke-width="2"/>
    <line x1="18" y1="12" x2="24" y2="12" stroke="#00F0FF" stroke-width="2"/>
    <text x="36" y="19" font-family="'Impact', 'Arial Black', sans-serif" font-size="19" font-weight="900" fill="#00F0FF" letter-spacing="1.5">MISSION SELECT — GAME PORTFOLIO</text>
  </g>

  <text x="920" y="35" font-family="'Orbitron', Consolas, monospace" font-size="13" font-weight="900" fill="#00F0FF" letter-spacing="1.5" text-anchor="end">EXPLORE MY PROJECTS</text>
</svg>'''

save_svg([os.path.join(git_assets, 'mission-header.svg'), os.path.join(desk_build, 'mission-header.svg')], mission_header_svg)

projects_data = [
    {
        'id': 'silent-city',
        'title': 'The Silent City',
        'subtitle': '3D Endless Runner',
        'desc': 'A post-apocalyptic runner in a frozen world.',
        'tech': 'Unity • C# • Android',
        'x': 25, 'y': 70
    },
    {
        'id': 'monster-hunter',
        'title': 'Monster Hunter',
        'subtitle': '3D Action Game',
        'desc': 'Fight, survive and conquer.',
        'tech': 'Unity • C# • PC Action',
        'x': 485, 'y': 70
    },
    {
        'id': 'sword-warrior',
        'title': 'Sword Warrior',
        'subtitle': '2D Action Game',
        'desc': 'A thrilling combat adventure.',
        'tech': 'Unity • C# • Android',
        'x': 25, 'y': 215
    },
    {
        'id': 'legends-tretayug',
        'title': 'Legends of Tretayug',
        'subtitle': 'Roguelike Action',
        'desc': 'A mythological roguelike journey.',
        'tech': 'Unity • C# • Team Lead',
        'x': 485, 'y': 215
    },
    {
        'id': 'triathlon',
        'title': 'Triathlon: Endurance',
        'subtitle': '3D Sports Game',
        'desc': 'Run. Swim. Cycle.',
        'tech': 'Unity • C# • PC / Windows',
        'x': 25, 'y': 360
    },
    {
        'id': 'vr-puzzle',
        'title': 'VR Shape Puzzle',
        'subtitle': 'VR Experience',
        'desc': 'Interact. Solve. Explore.',
        'tech': 'Unity 6 • Meta XR • OpenXR',
        'x': 485, 'y': 360
    }
]

card4_items_svg = []
for p in projects_data:
    b64_img = proj_b64[p['id']]
    item = f'''
    <g transform="translate({p['x']}, {p['y']})">
      <path d="M 12 0 L 428 0 L 440 12 L 440 118 L 428 130 L 12 130 L 0 118 L 0 12 Z" fill="#081426" stroke="#1677FF" stroke-width="1.6"/>
      <path d="M 0 24 L 0 12 L 12 0 L 24 0" stroke="#00F0FF" stroke-width="2.5" fill="none"/>
      <path d="M 416 130 L 428 130 L 440 118 L 440 106" stroke="#00F0FF" stroke-width="2.5" fill="none"/>

      <rect x="10" y="10" width="160" height="110" rx="6" fill="#030A16" stroke="#00F0FF" stroke-width="1.2"/>
      <image href="data:image/png;base64,{b64_img}" x="11" y="11" width="158" height="108" preserveAspectRatio="xMidYMid slice" rx="5"/>

      <g transform="translate(182, 22)">
        <text x="0" y="14" font-family="'Impact', 'Arial Black', sans-serif" font-size="16" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">{p['title']}</text>
        <text x="0" y="34" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="800" fill="#00F0FF">{p['subtitle']}</text>
        <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#A9C9EA">{p['desc']}</text>
        <text x="0" y="80" font-family="'Orbitron', Consolas, monospace" font-size="10" font-weight="700" fill="#7C95B6">{p['tech']}</text>
      </g>

      <g transform="translate(400, 92)">
        <circle cx="16" cy="16" r="14" fill="#0B2245" stroke="#00F0FF" stroke-width="1.5"/>
        <path d="M 12 16 L 20 16 M 16 12 L 20 16 L 16 20" stroke="#00F0FF" stroke-width="2" fill="none"/>
      </g>
    </g>
    '''
    card4_items_svg.append(item)

card4_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 515" width="100%" height="auto">
  <defs>
    {common_defs('c4')}
  </defs>

  <rect x="0" y="0" width="950" height="515" rx="10" fill="url(#c4_bg)"/>

  <g transform="translate(0, 0)">
    <path d="M 20 8 L 930 8 L 944 22 L 944 46 L 930 56 L 20 56 L 6 46 L 6 22 Z" fill="#08162E" stroke="#1677FF" stroke-width="1.6"/>
    <g transform="translate(28, 20)">
      <circle cx="10" cy="10" r="9" fill="none" stroke="#00F0FF" stroke-width="2"/>
      <circle cx="10" cy="10" r="3.5" fill="#00F0FF"/>
      <line x1="10" y1="0" x2="10" y2="5" stroke="#00F0FF" stroke-width="2"/>
      <line x1="10" y1="15" x2="10" y2="20" stroke="#00F0FF" stroke-width="2"/>
      <line x1="0" y1="10" x2="5" y2="10" stroke="#00F0FF" stroke-width="2"/>
      <line x1="15" y1="10" x2="20" y2="10" stroke="#00F0FF" stroke-width="2"/>
      <text x="32" y="17" font-family="'Impact', 'Arial Black', sans-serif" font-size="18" font-weight="900" fill="#00F0FF" letter-spacing="1.5">MISSION SELECT — GAME PORTFOLIO</text>
    </g>
    <text x="920" y="37" font-family="'Orbitron', Consolas, monospace" font-size="12" font-weight="900" fill="#00F0FF" letter-spacing="1.5" text-anchor="end">EXPLORE MY PROJECTS</text>
  </g>

  {''.join(card4_items_svg)}
</svg>'''

save_svg([os.path.join(git_assets, 'card4-missions.svg'), os.path.join(desk_build, 'card4-missions.svg')], card4_svg)

for p in projects_data:
    b64_img = proj_b64[p['id']]
    indiv_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 135" width="100%" height="auto">
  <defs>
    {common_defs('p_' + p['id'])}
  </defs>

  <path d="M 12 4 L 448 4 L 458 14 L 458 121 L 448 131 L 12 131 L 2 121 L 2 14 Z" fill="url(#p_{p['id']}_bg)" stroke="#1677FF" stroke-width="1.6"/>
  <path d="M 2 24 L 2 14 L 12 4 L 22 4" stroke="#00F0FF" stroke-width="2.5" fill="none"/>
  <path d="M 438 131 L 448 131 L 458 121 L 458 111" stroke="#00F0FF" stroke-width="2.5" fill="none"/>

  <rect x="12" y="12" width="165" height="111" rx="6" fill="#030A16" stroke="#00F0FF" stroke-width="1.2"/>
  <image href="data:image/png;base64,{b64_img}" x="13" y="13" width="163" height="109" preserveAspectRatio="xMidYMid slice" rx="5"/>

  <g transform="translate(190, 24)">
    <text x="0" y="15" font-family="'Impact', 'Arial Black', sans-serif" font-size="16.5" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">{p['title']}</text>
    <text x="0" y="36" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="800" fill="#00F0FF">{p['subtitle']}</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#A9C9EA">{p['desc']}</text>
    <text x="0" y="84" font-family="'Orbitron', Consolas, monospace" font-size="10.5" font-weight="700" fill="#7C95B6">{p['tech']}</text>
  </g>

  <g transform="translate(418, 92)">
    <circle cx="16" cy="16" r="14" fill="#0B2245" stroke="#00F0FF" stroke-width="1.5"/>
    <path d="M 12 16 L 20 16 M 16 12 L 20 16 L 16 20" stroke="#00F0FF" stroke-width="2" fill="none"/>
  </g>
</svg>'''
    save_svg([os.path.join(git_projects, f"{p['id']}.svg"), os.path.join(desk_projects, f"{p['id']}.svg")], indiv_svg)

# ==============================================================================
# 5. CARD 5: ACHIEVEMENTS & PLAYER STATISTICS (card4-numbers.svg, achievements.svg, stats.svg)
# ==============================================================================
achievements_stats_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 250" width="100%" height="auto">
  <defs>
    {common_defs('as')}
  </defs>

  <!-- LEFT PANEL: ACHIEVEMENTS UNLOCKED -->
  <g transform="translate(8, 6)">
    <path d="M 18 0 L 460 0 L 474 14 L 474 224 L 460 238 L 18 238 L 4 224 L 4 14 Z" fill="url(#as_bg)" stroke="#1677FF" stroke-width="1.6"/>
    <path d="M 4 28 L 4 14 L 18 0 L 32 0" stroke="#00F0FF" stroke-width="2.5" fill="none"/>
    <path d="M 446 238 L 460 238 L 474 224 L 474 210" stroke="#00F0FF" stroke-width="2.5" fill="none"/>

    <g transform="translate(24, 30)">
      <path d="M 2 4 L 18 4 C 18 9 14 14 10 14 C 6 14 2 9 2 4 Z M 10 14 L 10 18 M 5 18 L 15 18 M 2 6 L 0 6 C 0 9 2 11 4 11 L 4 9 M 18 6 L 20 6 C 20 9 18 11 16 11 L 16 9" fill="none" stroke="#FFB800" stroke-width="2"/>
      <text x="28" y="15" font-family="'Impact', 'Arial Black', sans-serif" font-size="16.5" font-weight="900" fill="#FFFFFF" letter-spacing="1">ACHIEVEMENTS UNLOCKED</text>
    </g>

    <!-- 4 GOLDEN HEXAGON BADGES -->
    <!-- Badge 1: Game Dev Intern -->
    <g transform="translate(62, 110)">
      <path d="M 0 -32 L 28 -16 L 28 16 L 0 32 L -28 16 L -28 -16 Z" fill="url(#as_gold_bg)" stroke="url(#as_gold_badge)" stroke-width="2.5" filter="url(#as_softglow)"/>
      <path d="M 0 -26 L 22 -13 L 22 13 L 0 26 L -22 13 L -22 -13 Z" fill="none" stroke="#FFE57F" stroke-width="1" opacity="0.6"/>
      <g transform="translate(-12, -10)">
        <rect x="0" y="0" width="24" height="18" rx="5" fill="#3D2802" stroke="#FFB800" stroke-width="1.2"/>
        <circle cx="7" cy="9" r="1.5" fill="#FFB800"/>
        <circle cx="17" cy="9" r="1.5" fill="#FFB800"/>
      </g>
      <text x="0" y="52" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">GAME DEV</text>
      <text x="0" y="65" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">INTERN</text>
    </g>

    <!-- Badge 2: Team Lead -->
    <g transform="translate(178, 110)">
      <path d="M 0 -32 L 28 -16 L 28 16 L 0 32 L -28 16 L -28 -16 Z" fill="url(#as_gold_bg)" stroke="url(#as_gold_badge)" stroke-width="2.5" filter="url(#as_softglow)"/>
      <path d="M 0 -26 L 22 -13 L 22 13 L 0 26 L -22 13 L -22 -13 Z" fill="none" stroke="#FFE57F" stroke-width="1" opacity="0.6"/>
      <g transform="translate(-12, -10)">
        <circle cx="8" cy="5" r="3" fill="#FFB800"/>
        <circle cx="16" cy="5" r="3" fill="#FFB800"/>
        <path d="M 4 16 C 4 12 12 12 12 16 M 12 16 C 12 12 20 12 20 16" fill="none" stroke="#FFB800" stroke-width="1.4"/>
      </g>
      <text x="0" y="52" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">TEAM LEAD</text>
      <text x="0" y="65" font-family="-apple-system, sans-serif" font-size="8" font-weight="600" fill="#FFE57F" text-anchor="middle">(Akiyam)</text>
    </g>

    <!-- Badge 3: Gameplay Systems Dev -->
    <g transform="translate(296, 110)">
      <path d="M 0 -32 L 28 -16 L 28 16 L 0 32 L -28 16 L -28 -16 Z" fill="url(#as_gold_bg)" stroke="url(#as_gold_badge)" stroke-width="2.5" filter="url(#as_softglow)"/>
      <path d="M 0 -26 L 22 -13 L 22 13 L 0 26 L -22 13 L -22 -13 Z" fill="none" stroke="#FFE57F" stroke-width="1" opacity="0.6"/>
      <path d="M 0 -10 L 3 -3 L 10 -2 L 5 3 L 7 10 L 0 6 L -7 10 L -5 3 L -10 -2 L -3 -3 Z" fill="#FFB800"/>
      <text x="0" y="52" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">GAMEPLAY</text>
      <text x="0" y="65" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">SYSTEMS DEV</text>
    </g>

    <!-- Badge 4: VR Dev Specialist -->
    <g transform="translate(414, 110)">
      <path d="M 0 -32 L 28 -16 L 28 16 L 0 32 L -28 16 L -28 -16 Z" fill="url(#as_gold_bg)" stroke="url(#as_gold_badge)" stroke-width="2.5" filter="url(#as_softglow)"/>
      <path d="M 0 -26 L 22 -13 L 22 13 L 0 26 L -22 13 L -22 -13 Z" fill="none" stroke="#FFE57F" stroke-width="1" opacity="0.6"/>
      <g transform="translate(-12, -9)">
        <rect x="2" y="4" width="20" height="11" rx="4" fill="#3D2802" stroke="#FFB800" stroke-width="1.2"/>
        <circle cx="8" cy="9.5" r="2" fill="#FFB800"/>
        <circle cx="16" cy="9.5" r="2" fill="#FFB800"/>
      </g>
      <text x="0" y="52" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">VR DEV</text>
      <text x="0" y="65" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#FFD700" text-anchor="middle">SPECIALIST</text>
    </g>
  </g>

  <!-- RIGHT PANEL: PLAYER STATISTICS -->
  <g transform="translate(496, 6)">
    <path d="M 18 0 L 432 0 L 446 14 L 446 224 L 432 238 L 18 238 L 4 224 L 4 14 Z" fill="url(#as_bg)" stroke="#1677FF" stroke-width="1.6"/>
    <path d="M 4 28 L 4 14 L 18 0 L 32 0" stroke="#00F0FF" stroke-width="2.5" fill="none"/>
    <path d="M 418 238 L 432 238 L 446 224 L 446 210" stroke="#00F0FF" stroke-width="2.5" fill="none"/>

    <g transform="translate(24, 30)">
      <path d="M 2 16 L 6 10 L 11 13 L 18 4" stroke="#00F0FF" stroke-width="2" fill="none"/>
      <text x="28" y="15" font-family="'Impact', 'Arial Black', sans-serif" font-size="16.5" font-weight="900" fill="#FFFFFF" letter-spacing="1">PLAYER STATISTICS</text>
    </g>

    <text x="424" y="30" font-family="'Orbitron', Consolas, monospace" font-size="11" font-weight="800" fill="#00F0FF" text-anchor="end">GitHub Analytics</text>

    <!-- STAT 1: Total Commits -->
    <g transform="translate(24, 60)">
      <rect x="0" y="0" width="124" height="154" rx="8" fill="#061226" stroke="#1677FF" stroke-width="1.2"/>
      <text x="12" y="24" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#7C95B6">Total Commits</text>
      
      <text x="12" y="60" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF">323</text>
      <text x="68" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#00FF66">↑ 12%</text>

      <path d="M 4 146 L 4 115 Q 24 95, 44 110 T 84 92 T 120 78 L 120 146 Z" fill="url(#as_wave_blue)"/>
      <path d="M 4 115 Q 24 95, 44 110 T 84 92 T 120 78" fill="none" stroke="#00F0FF" stroke-width="2"/>
    </g>

    <!-- STAT 2: Repositories -->
    <g transform="translate(162, 60)">
      <rect x="0" y="0" width="124" height="154" rx="8" fill="#061226" stroke="#1677FF" stroke-width="1.2"/>
      <text x="12" y="24" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#7C95B6">Repositories</text>
      
      <text x="12" y="60" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF">18</text>
      <text x="56" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#00FF66">↑ 8%</text>

      <path d="M 8 146 L 8 125 L 28 125 L 28 110 L 52 110 L 52 95 L 76 95 L 76 80 L 100 80 L 100 68 L 116 68 L 116 146 Z" fill="url(#as_wave_blue)"/>
      <path d="M 8 125 L 28 125 L 28 110 L 52 110 L 52 95 L 76 95 L 76 80 L 100 80 L 100 68 L 116 68" fill="none" stroke="#00F0FF" stroke-width="2"/>
    </g>

    <!-- STAT 3: Contribution Streak -->
    <g transform="translate(300, 60)">
      <rect x="0" y="0" width="128" height="154" rx="8" fill="#061226" stroke="#FF6B00" stroke-width="1.2"/>
      <text x="10" y="24" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#7C95B6">Dev Streak</text>
      
      <text x="10" y="60" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF">42</text>
      <text x="46" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FF8C00">Days 🔥</text>

      <path d="M 4 146 L 4 130 Q 18 118, 30 126 T 55 98 T 80 114 T 100 70 T 124 82 L 124 146 Z" fill="url(#as_wave_orange)"/>
      <path d="M 4 130 Q 18 118, 30 126 T 55 98 T 80 114 T 100 70 T 124 82" fill="none" stroke="#FF8C00" stroke-width="2"/>
    </g>
  </g>
</svg>'''

save_svg([os.path.join(git_assets, 'card4-numbers.svg'), os.path.join(git_assets, 'achievements.svg'),
          os.path.join(git_assets, 'stats.svg'), os.path.join(desk_build, 'card4-numbers.svg'),
          os.path.join(desk_build, 'achievements.svg'), os.path.join(desk_build, 'stats.svg')], achievements_stats_svg)

# ==============================================================================
# 6. CARD 6: CALL TO ACTION & FOOTER (card5-connect.svg, contact.svg, footer.svg)
# ==============================================================================
card5_connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 250" width="100%" height="auto">
  <defs>
    {common_defs('c5')}
  </defs>

  <!-- Outer Frame -->
  <path d="M 24 10 L 926 10 L 942 26 L 942 234 L 926 242 L 24 242 L 8 234 L 8 26 Z" fill="url(#c5_bg)" stroke="#1677FF" stroke-width="1.8" filter="url(#c5_softglow)"/>
  <path d="M 24 10 L 926 10 L 942 26 L 942 234 L 926 242 L 24 242 L 8 234 L 8 26 Z" fill="url(#c5_grid)"/>

  <!-- Corner Brackets -->
  <path d="M 8 36 L 8 16 L 36 10" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 10 L 942 16 L 942 36" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 8 214 L 8 234 L 36 242" stroke="#00F0FF" stroke-width="3" fill="none"/>
  <path d="M 914 242 L 942 234 L 942 214" stroke="#00F0FF" stroke-width="3" fill="none"/>

  <!-- Top Hero Pitch -->
  <g transform="translate(36, 40)">
    <g transform="translate(0, 4)">
      <circle cx="24" cy="24" r="26" fill="#0B1F3D" stroke="#00F0FF" stroke-width="2" filter="url(#c5_softglow)"/>
      <path d="M 24 10 L 34 16 L 34 28 L 24 34 L 14 28 L 14 16 Z" fill="#FFFFFF"/>
      <path d="M 24 10 L 24 34 M 14 16 L 34 28 M 34 16 L 14 28" stroke="#0B1F3D" stroke-width="1.5"/>
    </g>

    <text x="68" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" letter-spacing="1">HAVE A GAME IDEA? LET'S BUILD IT.</text>
    <text x="68" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#A9C9EA">Always open to game development opportunities, collaboration and creative challenges.</text>
  </g>

  <!-- 4 GAMING TERMINAL BUTTONS -->
  <g transform="translate(36, 122)">
    <!-- Button 1: GitHub -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="205" height="52" rx="8" fill="#081730" stroke="#1677FF" stroke-width="1.4"/>
      <path d="M 22 17 C 18.7 17 16 19.7 16 23 C 16 25.7 17.7 27.9 20.1 28.7 C 20.4 28.8 20.5 28.6 20.5 28.4 L 20.5 27.3 C 18.8 27.7 18.5 26.5 18.5 26.5 C 18.2 25.8 17.8 25.6 17.8 25.6 C 17.3 25.2 17.9 25.2 17.9 25.2 C 18.5 25.3 18.8 25.8 18.8 25.8 C 19.3 26.7 20.2 26.5 20.6 26.3 C 20.7 25.9 20.8 25.6 21 25.4 C 19.6 25.2 18.1 24.7 18.1 22.4 C 18.1 21.7 18.3 21.2 18.8 20.7 C 18.7 20.5 18.5 19.9 18.9 19.1 C 18.9 19.1 19.4 18.9 20.6 19.8 C 21.1 19.7 21.7 19.6 22.2 19.6 C 22.7 19.6 23.3 19.7 23.8 19.8 C 25 18.9 25.5 19.1 25.5 19.1 C 25.9 19.9 25.7 20.5 25.6 20.7 C 26.1 21.2 26.3 21.7 26.3 22.4 C 26.3 24.7 24.8 25.2 23.4 25.4 C 23.6 25.6 23.8 26 23.8 26.6 L 23.8 28.4 C 23.8 28.6 23.9 28.8 24.2 28.7 C 26.6 27.9 28.3 25.7 28.3 23 C 28.3 19.7 25.6 17 22.2 17 Z" fill="#FFFFFF"/>
      <text x="44" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="14" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">GitHub</text>
      <text x="44" y="40" font-family="-apple-system, sans-serif" font-size="11" fill="#7C95B6">Explore My Work</text>
    </g>

    <!-- Button 2: LinkedIn -->
    <g transform="translate(225, 0)">
      <rect x="0" y="0" width="205" height="52" rx="8" fill="#081730" stroke="#1677FF" stroke-width="1.4"/>
      <rect x="18" y="16" width="18" height="18" rx="3" fill="#0077B5"/>
      <text x="21" y="29" font-family="Arial, sans-serif" font-size="12" font-weight="900" fill="#FFFFFF">in</text>
      <text x="46" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="14" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">LinkedIn</text>
      <text x="46" y="40" font-family="-apple-system, sans-serif" font-size="11" fill="#7C95B6">Let's Connect</text>
    </g>

    <!-- Button 3: Portfolio (Itch.io) -->
    <g transform="translate(450, 0)">
      <rect x="0" y="0" width="205" height="52" rx="8" fill="#081730" stroke="#1677FF" stroke-width="1.4"/>
      <circle cx="28" cy="26" r="9" fill="#FA5C5C"/>
      <text x="23" y="30" font-size="11">🎮</text>
      <text x="46" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="14" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">Portfolio</text>
      <text x="46" y="40" font-family="-apple-system, sans-serif" font-size="11" fill="#7C95B6">View My Games</text>
    </g>

    <!-- Button 4: Email -->
    <g transform="translate(675, 0)">
      <rect x="0" y="0" width="205" height="52" rx="8" fill="#081730" stroke="#1677FF" stroke-width="1.4"/>
      <rect x="16" y="18" width="20" height="15" rx="3" fill="#EA4335"/>
      <path d="M 17 19 L 26 26 L 35 19" stroke="#FFFFFF" stroke-width="1.5" fill="none"/>
      <text x="44" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="14" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">Email</text>
      <text x="44" y="40" font-family="-apple-system, sans-serif" font-size="11" fill="#7C95B6">Contact Me</text>
    </g>
  </g>

  <!-- Player Status Indicator -->
  <g transform="translate(805, 185)">
    <circle cx="8" cy="8" r="4" fill="#00FF66" filter="url(#c5_softglow)"/>
    <text x="18" y="12" font-family="'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="900" fill="#00FF66" letter-spacing="1">PLAYER STATUS: ONLINE</text>
  </g>

  <!-- Bottom Ticker -->
  <text x="475" y="222" font-family="'Orbitron', Consolas, monospace" font-size="11" font-weight="800" fill="#43C6FF" letter-spacing="2.5" text-anchor="middle">POWERED BY UNITY  •  BUILT WITH C#  •  DRIVEN BY CREATIVITY</text>
</svg>'''

save_svg([os.path.join(git_assets, 'card5-connect.svg'), os.path.join(git_assets, 'contact.svg'),
          os.path.join(git_assets, 'footer.svg'), os.path.join(desk_build, 'card5-connect.svg'),
          os.path.join(desk_build, 'contact.svg'), os.path.join(desk_build, 'footer.svg')], card5_connect_svg)

print("ALL GAMIFIED SVGS GENERATED SUCCESSFULLY!")

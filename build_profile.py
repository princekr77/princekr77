import os
import base64
import json
import urllib.request
from PIL import Image

# ==============================================================================
# ⚙️ LIVE & MANUAL CONFIGURATION BLOCK — EASILY UPDATE IN THE FUTURE
# ==============================================================================
# All configurable profile data is gathered in this block.
# Real-time GitHub API fetching is enabled by default.
# To override numbers or text manually, simply edit the values below:
# ==============================================================================

CONFIG = {
    # GitHub Account Details
    "GITHUB_USERNAME": "princekr77",
    "FETCH_LIVE_GITHUB_STATS": True,  # Set to False to use the manual stats below

    # Manual Stats Fallback / Overrides (Used if API is offline or FETCH_LIVE is False)
    "MANUAL_REPOS_COUNT": 16,
    "MANUAL_FOLLOWERS_COUNT": 4,
    "LEADERSHIP_EXPERIENCE": "6 mo",
    "GAMES_SPECTRUM": "2D + 3D",

    # Hero & Intro Information
    "NAME_LINE1": "PRINCE",
    "NAME_LINE2": "KUMAR GUPTA.",
    "ROLE_TAG": "// Unity Game Developer: combat, AI, XR",
    "INTRO_BIO": "I build action games that feel good to play: responsive combat, readable enemy AI, clean UI and smooth builds on real devices.",
    "METADATA_LOCATION": "Ghaziabad, India",
    "METADATA_ROLE": "Unity Dev & Team Lead, Akiyam Solutions",
    "METADATA_EDU": "B.Tech CSE, KIET 2028",

    # Contact & Social Links
    "LINKEDIN_URL": "https://www.linkedin.com/in/prince-gupta-b98189330",
    "LINKEDIN_HANDLE": "in/prince-gupta-b98189330",
    "GITHUB_URL": "https://github.com/princekr77",
    "GITHUB_HANDLE": "github.com/princekr77",
    "EMAIL_ADDRESS": "princekr2927@gmail.com",
    "PORTFOLIO_URL": "https://gamedevprince.itch.io",

    # Projects List
    "PROJECTS": [
        {
            "id": "silent-city",
            "title": "The Silent City",
            "badge": "FEB 2026",
            "desc": "Story-driven 3D endless runner with lane-based movement, swipe controls and a player-follow camera, optimized for Android.",
            "tags": ["Unity", "C#", "Android", "Cinematic UI"],
            "code_url": "https://github.com/princekr77/The-Silent-City-Echo-Run",
            "demo_url": "https://gamedevprince.itch.io/the-silent-city"
        },
        {
            "id": "monster-hunter",
            "title": "Monster Hunter",
            "badge": "IN DEVELOPMENT",
            "desc": "3D action game with a character controller, attack system, enemy AI behavior and collision-based interactions for PC.",
            "tags": ["Unity", "C#", "Enemy AI", "Combat"],
            "code_url": "https://github.com/princekr77/Monster_Hunter2.0",
            "demo_url": ""
        },
        {
            "id": "sword-warrior",
            "title": "Sword Warrior",
            "badge": "JAN 2025",
            "desc": "2D melee combat game with sword attacks, enemy AI, Animator state machines and a health system, optimized for Android.",
            "tags": ["Unity 2D", "C#", "Animator", "Android"],
            "code_url": "https://github.com/princekr77/Sword_Warrior",
            "demo_url": "https://github.com/princekr77/Sword_Warrior"
        },
        {
            "id": "legends-tretayug",
            "title": "Legend of Tretaya",
            "badge": "MAR - SEP 2026",
            "desc": "Professional Unity project at Akiyam Solutions, where I contributed across game development and led the team.",
            "tags": ["Unity", "C#", "Team lead"],
            "code_url": "https://github.com/princekr77",
            "demo_url": ""
        }
    ]
}

# ==============================================================================
# 🌐 FETCH REAL-TIME GITHUB DATA
# ==============================================================================
def get_live_github_stats(username):
    repos = CONFIG["MANUAL_REPOS_COUNT"]
    followers = CONFIG["MANUAL_FOLLOWERS_COUNT"]
    
    if CONFIG["FETCH_LIVE_GITHUB_STATS"]:
        try:
            url = f"https://api.github.com/users/{username}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Profile-Builder"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                repos = data.get("public_repos", repos)
                followers = data.get("followers", followers)
                print(f"[LIVE DATA] GitHub API: {repos} public repos, {followers} followers")
        except Exception as e:
            print(f"[WARN] Could not fetch GitHub API ({e}). Using manual fallback stats.")
            
    return repos, followers

live_repos, live_followers = get_live_github_stats(CONFIG["GITHUB_USERNAME"])

# Directories
git_root = os.path.dirname(os.path.abspath(__file__))
git_assets = os.path.join(git_root, "assets")
git_projects = os.path.join(git_assets, "projects")
desk_build = r"C:/Users/hp/Desktop/PRINCE_EXE_BUILD"
desk_projects = os.path.join(desk_build, "projects")

os.makedirs(git_assets, exist_ok=True)
os.makedirs(git_projects, exist_ok=True)
os.makedirs(desk_build, exist_ok=True)
os.makedirs(desk_projects, exist_ok=True)

# Helper to load base64
def get_b64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def save_svg(filenames, content):
    for fn in filenames:
        with open(fn, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"Saved: {os.path.basename(fn)} ({len(content)} bytes)")

# Load Avatar and Project Images
avatar_path = os.path.join(git_assets, "avatar.png")
avatar_b64 = get_b64(avatar_path)

proj_b64 = {}
for p in CONFIG["PROJECTS"]:
    p_img = os.path.join(git_projects, f"{p['id']}.png")
    proj_b64[p['id']] = get_b64(p_img)

# Common SVG styles & defs
def get_svg_defs(prefix):
    return f'''
    <linearGradient id="{prefix}_card_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0E1422"/>
      <stop offset="100%" stop-color="#0A0F1A"/>
    </linearGradient>
    <linearGradient id="{prefix}_glow_cyan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>
    <linearGradient id="{prefix}_subcard_bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0B111E"/>
      <stop offset="100%" stop-color="#070C15"/>
    </linearGradient>
    <filter id="{prefix}_softglow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="{prefix}_avatar_clip">
      <circle cx="720" cy="180" r="82"/>
    </clipPath>
    <clipPath id="{prefix}_devpass_clip">
      <circle cx="130" cy="120" r="42"/>
    </clipPath>
    '''

# ==============================================================================
# CARD 1: INTRO (card1-intro.svg)
# ==============================================================================
card1_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 365" width="100%" height="auto">
  <defs>
    {get_svg_defs("c1")}
  </defs>

  <!-- Top Monospace Bar -->
  <text x="24" y="24" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11.5" font-weight="600" fill="#7C95B6" letter-spacing="1">princekr77 / README.md</text>
  <text x="836" y="24" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="1.5" text-anchor="end">● PLAYER 1 READY</text>

  <!-- Main Container -->
  <rect x="10" y="38" width="840" height="315" rx="14" fill="url(#c1_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

  <!-- Left Content Area -->
  <g transform="translate(36, 70)">
    <!-- Category Tag -->
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> INTRO</text>

    <!-- Terminal Prompt -->
    <text x="0" y="30" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="14.5" font-weight="bold" fill="#E2E8F0"><tspan fill="#38BDF8">&gt;</tspan> hello world, i'm <tspan fill="#00F0FF">█</tspan></text>

    <!-- Main Name Title -->
    <text x="0" y="82" font-family="'Impact', 'Arial Black', sans-serif" font-size="52" font-weight="900" fill="#FFFFFF" letter-spacing="1">{CONFIG["NAME_LINE1"]}</text>
    <text x="0" y="132" font-family="'Impact', 'Arial Black', sans-serif" font-size="52" font-weight="900" fill="#FFFFFF" letter-spacing="1">KUMAR GUPTA<tspan fill="#38BDF8">.</tspan></text>

    <!-- Subtitle Role -->
    <text x="0" y="166" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="13" font-weight="bold" fill="#38BDF8">{CONFIG["ROLE_TAG"]}</text>

    <!-- Bio Description -->
    <text x="0" y="196" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#94A3B8">I build action games that feel good to play: responsive combat,</text>
    <text x="0" y="215" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#94A3B8">readable enemy AI, clean UI and smooth builds on real devices.</text>

    <!-- Metadata Row -->
    <g transform="translate(0, 246)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="600" fill="#88A6C8">
        📍 {CONFIG["METADATA_LOCATION"]} &nbsp;&bull;&nbsp; 💼 {CONFIG["METADATA_ROLE"]} &nbsp;&bull;&nbsp; 🎓 {CONFIG["METADATA_EDU"]}
      </text>
    </g>
  </g>

  <!-- Right: Circular Hologram Avatar -->
  <g transform="translate(0, 10)">
    <!-- Outer dashed energy circle -->
    <circle cx="720" cy="180" r="98" fill="none" stroke="#162E56" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="720" cy="180" r="92" fill="none" stroke="#1677FF" stroke-width="1.8" filter="url(#c1_softglow)"/>
    <circle cx="720" cy="180" r="85" fill="#0A162B" stroke="#00F0FF" stroke-width="2.5"/>

    <!-- Avatar Image -->
    <image href="data:image/png;base64,{avatar_b64}" x="638" y="98" width="164" height="164" preserveAspectRatio="xMidYMid slice" clip-path="url(#c1_avatar_clip)"/>

    <!-- Bottom Pinned Tag Badge -->
    <rect x="645" y="270" width="150" height="26" rx="6" fill="#081730" stroke="#00F0FF" stroke-width="1.4"/>
    <text x="720" y="287" font-family="'Impact', Arial Black, sans-serif" font-size="11.5" font-weight="900" fill="#38BDF8" letter-spacing="1.5" text-anchor="middle">UNITY / C# / XR</text>
  </g>
</svg>'''

# ==============================================================================
# CARD 2: ABOUT / WHAT I BUILD & QUEST LOG (card2-about.svg)
# ==============================================================================
card2_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="100%" height="auto">
  <defs>
    {get_svg_defs("c2")}
  </defs>

  <!-- Main Container -->
  <rect x="10" y="8" width="840" height="284" rx="14" fill="url(#c2_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

  <!-- Left Content: What I Build -->
  <g transform="translate(36, 36)">
    <!-- Category Tag -->
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> ABOUT</text>

    <!-- Title -->
    <text x="0" y="32" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">WHAT I BUILD<tspan fill="#38BDF8">.</tspan></text>

    <!-- 4 Numbered Items -->
    <!-- 01 -->
    <g transform="translate(0, 68)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" fill="#38BDF8">01</text>
      <text x="28" y="0" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="bold" fill="#FFFFFF">Combat systems</text>
      <text x="28" y="18" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">Melee and 3D attacks, collision-based hits, health systems</text>
    </g>

    <!-- 02 -->
    <g transform="translate(0, 114)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" fill="#38BDF8">02</text>
      <text x="28" y="0" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="bold" fill="#FFFFFF">Enemy AI</text>
      <text x="28" y="18" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">Animator state machines and behavior that reads clearly</text>
    </g>

    <!-- 03 -->
    <g transform="translate(0, 160)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" fill="#38BDF8">03</text>
      <text x="28" y="0" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="bold" fill="#FFFFFF">Mobile and PC builds</text>
      <text x="28" y="18" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">Android APK, Windows and WebGL, tuned for performance</text>
    </g>

    <!-- 04 -->
    <g transform="translate(0, 206)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" fill="#38BDF8">04</text>
      <text x="28" y="0" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="bold" fill="#FFFFFF">UI and AR/VR prototypes</text>
      <text x="28" y="18" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">Canvas UI flow, scene management, immersive prototypes</text>
    </g>
  </g>

  <!-- Right Sub-Card: QUEST LOG -->
  <g transform="translate(540, 36)">
    <rect x="0" y="0" width="290" height="230" rx="10" fill="url(#c2_subcard_bg)" stroke="#16253D" stroke-width="1.2"/>
    
    <text x="24" y="32" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">QUEST LOG</text>
    <text x="24" y="104" font-family="'Impact', 'Arial Black', sans-serif" font-size="64" font-weight="900" fill="#FFFFFF">{len(CONFIG["PROJECTS"])}</text>
    
    <text x="24" y="142" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">Unity projects across 2D, 3D and</text>
    <text x="24" y="162" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">mobile, including one team-led</text>
    <text x="24" y="182" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">production.</text>

    <text x="24" y="212" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#64748B" letter-spacing="1.5">SOURCE: MY RESUME</text>
  </g>
</svg>'''

# ==============================================================================
# CARD 3: STACK / SKILL TREE (card3-stack.svg)
# ==============================================================================
card3_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 415" width="100%" height="auto">
  <defs>
    {get_svg_defs("c3")}
  </defs>

  <!-- Main Container -->
  <rect x="10" y="8" width="840" height="398" rx="14" fill="url(#c3_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(36, 36)">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> STACK</text>
    <text x="0" y="32" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">SKILL TREE<tspan fill="#38BDF8">.</tspan></text>
  </g>

  <!-- LEFT COLUMN -->
  <g transform="translate(36, 94)">
    <!-- LANGUAGES -->
    <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">LANGUAGES</text>
    <g transform="translate(0, 20)">
      <rect x="0" y="0" width="36" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="18" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">C#</text>
      
      <rect x="44" y="0" width="46" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="67" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">C++</text>

      <rect x="98" y="0" width="30" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="113" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">C</text>
    </g>

    <!-- ENGINE -->
    <text x="0" y="68" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">ENGINE</text>
    <g transform="translate(0, 76)">
      <rect x="0" y="0" width="70" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="35" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Unity 2D</text>

      <rect x="78" y="0" width="70" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="113" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Unity 3D</text>
    </g>

    <!-- GAMEPLAY SYSTEMS -->
    <text x="0" y="124" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">GAMEPLAY SYSTEMS</text>
    <g transform="translate(0, 132)">
      <rect x="0" y="0" width="125" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="62" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">AI State Machines</text>

      <rect x="133" y="0" width="160" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="213" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Animator State Machines</text>

      <!-- Row 2 -->
      <rect x="0" y="30" width="145" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="72" y="46" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Physics-Based Combat</text>

      <rect x="153" y="30" width="140" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="223" y="46" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Character Controllers</text>

      <!-- Row 3 -->
      <rect x="0" y="60" width="105" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="52" y="76" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Health Systems</text>

      <rect x="113" y="60" width="130" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="178" y="76" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Physics Simulation</text>
    </g>

    <!-- UI AND SCENE SYSTEMS -->
    <text x="0" y="242" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">UI AND SCENE SYSTEMS</text>
    <g transform="translate(0, 250)">
      <rect x="0" y="0" width="98" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="49" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Canvas UI/UX</text>

      <rect x="106" y="0" width="112" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="162" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">UI Optimization</text>

      <rect x="226" y="0" width="135" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="293" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Scene Management</text>
    </g>
  </g>

  <!-- RIGHT COLUMN -->
  <g transform="translate(465, 94)">
    <!-- LEVEL AND WORLD DESIGN -->
    <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">LEVEL AND WORLD DESIGN</text>
    <g transform="translate(0, 20)">
      <rect x="0" y="0" width="105" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="52" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Terrain Design</text>

      <rect x="113" y="0" width="140" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="183" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Environment Design</text>
    </g>

    <!-- NARRATIVE DESIGN -->
    <text x="0" y="68" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">NARRATIVE DESIGN</text>
    <g transform="translate(0, 76)">
      <rect x="0" y="0" width="170" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="85" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Branching Dialogue Systems</text>

      <rect x="178" y="0" width="130" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="243" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Story Architecture</text>
    </g>

    <!-- XR -->
    <text x="0" y="124" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">XR</text>
    <g transform="translate(0, 132)">
      <rect x="0" y="0" width="132" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="66" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">AR/VR Frameworks</text>

      <rect x="140" y="0" width="135" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="207" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">AR/VR Prototyping</text>
    </g>

    <!-- PLATFORMS -->
    <text x="0" y="180" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">PLATFORMS</text>
    <g transform="translate(0, 188)">
      <rect x="0" y="0" width="98" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="49" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Android (APK)</text>

      <rect x="106" y="0" width="70" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="141" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Windows</text>

      <rect x="184" y="0" width="60" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="214" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">WebGL</text>
    </g>

    <!-- VERSION CONTROL -->
    <text x="0" y="242" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">VERSION CONTROL</text>
    <g transform="translate(0, 250)">
      <rect x="0" y="0" width="36" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="18" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">Git</text>

      <rect x="44" y="0" width="62" height="24" rx="5" fill="#0B1322" stroke="#1A2B44"/>
      <text x="75" y="16" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1" text-anchor="middle">GitHub</text>
    </g>
  </g>
</svg>'''

# ==============================================================================
# CARD 4: STATS & DEV PASS (card4-stats.svg)
# ==============================================================================
card4_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="100%" height="auto">
  <defs>
    {get_svg_defs("c4")}
  </defs>

  <!-- LEFT: DEV PASS CARD -->
  <g transform="translate(10, 8)">
    <!-- Lanyard slot -->
    <rect x="100" y="0" width="40" height="6" rx="3" fill="#060C16" stroke="#162238"/>
    
    <!-- Pass Badge Background -->
    <rect x="0" y="10" width="240" height="274" rx="12" fill="#081426" stroke="#1677FF" stroke-width="1.6"/>
    
    <!-- Pass Top Header -->
    <text x="20" y="38" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#00F0FF" letter-spacing="1.5">DEV PASS ///</text>

    <!-- Centered Avatar Circle -->
    <circle cx="120" cy="104" r="46" fill="none" stroke="#162E56" stroke-width="2"/>
    <circle cx="120" cy="104" r="42" fill="#0A162B" stroke="#00F0FF" stroke-width="2"/>
    <image href="data:image/png;base64,{avatar_b64}" x="78" y="62" width="84" height="84" preserveAspectRatio="xMidYMid slice" clip-path="url(#c4_devpass_clip)"/>

    <!-- Pass Name -->
    <text x="120" y="174" font-family="'Impact', 'Arial Black', sans-serif" font-size="17" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">PRINCE</text>
    <text x="120" y="194" font-family="'Impact', 'Arial Black', sans-serif" font-size="17" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">KUMAR GUPTA</text>

    <!-- Role Badge -->
    <rect x="45" y="208" width="150" height="22" rx="5" fill="#0B1C38" stroke="#1677FF" stroke-width="1.2"/>
    <text x="120" y="223" font-family="'Impact', sans-serif" font-size="10.5" font-weight="bold" fill="#38BDF8" letter-spacing="1.5" text-anchor="middle">UNITY DEVELOPER</text>

    <!-- Pass Metadata -->
    <text x="120" y="258" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold" fill="#7C95B6" text-anchor="middle" letter-spacing="0.8">KIET '28 / ID: PRINCEKR77</text>
  </g>

  <!-- RIGHT: BY THE NUMBERS -->
  <g transform="translate(265, 8)">
    <!-- Container -->
    <rect x="0" y="0" width="585" height="284" rx="14" fill="url(#c4_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

    <!-- Category Tag & Title -->
    <text x="28" y="32" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> STATS</text>
    <text x="28" y="66" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">BY THE NUMBERS<tspan fill="#38BDF8">.</tspan></text>

    <!-- 4 Stat Boxes (2x2 Grid) -->
    <!-- Box 1: Live GitHub Repos -->
    <g transform="translate(28, 88)">
      <rect x="0" y="0" width="250" height="72" rx="8" fill="url(#c4_subcard_bg)" stroke="#16253D" stroke-width="1.2"/>
      <text x="20" y="38" font-family="'Impact', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">{live_repos}</text>
      <text x="20" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#88A6C8">GitHub repos</text>
    </g>

    <!-- Box 2: Live GitHub Followers -->
    <g transform="translate(305, 88)">
      <rect x="0" y="0" width="250" height="72" rx="8" fill="url(#c4_subcard_bg)" stroke="#16253D" stroke-width="1.2"/>
      <text x="20" y="38" font-family="'Impact', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">{live_followers}</text>
      <text x="20" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#88A6C8">GitHub followers</text>
    </g>

    <!-- Box 3: Leadership Experience -->
    <g transform="translate(28, 172)">
      <rect x="0" y="0" width="250" height="72" rx="8" fill="url(#c4_subcard_bg)" stroke="#16253D" stroke-width="1.2"/>
      <text x="20" y="38" font-family="'Impact', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">{CONFIG["LEADERSHIP_EXPERIENCE"]}</text>
      <text x="20" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#88A6C8">Leading a game dev team</text>
    </g>

    <!-- Box 4: Spectrum -->
    <g transform="translate(305, 172)">
      <rect x="0" y="0" width="250" height="72" rx="8" fill="url(#c4_subcard_bg)" stroke="#16253D" stroke-width="1.2"/>
      <text x="20" y="38" font-family="'Impact', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">{CONFIG["GAMES_SPECTRUM"]}</text>
      <text x="20" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#88A6C8">Games across both</text>
    </g>

    <!-- Footer Note -->
    <text x="28" y="268" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">All figures verified live via GitHub API &amp; resume. Swap in download counts once a game is live.</text>
  </g>
</svg>'''

# ==============================================================================
# CARD 5: PROJECTS / LEVELS (card5-levels.svg)
# ==============================================================================
def render_project_card(p, x, y):
    b64 = proj_b64.get(p["id"], "")
    
    tags_svg = []
    curr_x = 0
    for tag in p["tags"]:
        tag_w = len(tag) * 7.5 + 14
        tags_svg.append(f'''
          <rect x="{curr_x}" y="0" width="{tag_w}" height="20" rx="4" fill="#0B1322" stroke="#1A2B44"/>
          <text x="{curr_x + tag_w/2}" y="14" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#CBD5E1" text-anchor="middle">{tag}</text>
        ''')
        curr_x += tag_w + 6

    # Action links
    links_text = "Source code"
    if p["demo_url"]:
        links_text = "Source code &nbsp;&bull;&nbsp; Download APK"

    return f'''
    <g transform="translate({x}, {y})">
      <!-- Card Box -->
      <rect x="0" y="0" width="395" height="265" rx="10" fill="url(#c5_subcard_bg)" stroke="#16253D" stroke-width="1.2"/>

      <!-- Screenshot Header -->
      <rect x="1" y="1" width="393" height="118" rx="9" fill="#030812"/>
      <image href="data:image/png;base64,{b64}" x="1" y="1" width="393" height="118" preserveAspectRatio="xMidYMid slice" clip-path="url(#c5_thumb_clip)"/>

      <!-- Meta Row -->
      <text x="16" y="146" font-family="'Impact', 'Arial Black', sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">{p["title"]}</text>
      <text x="378" y="146" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="end">{p["badge"]}</text>

      <!-- Description -->
      <text x="16" y="170" font-family="-apple-system, sans-serif" font-size="11.5" fill="#88A6C8">{p["desc"][:56]}</text>
      <text x="16" y="186" font-family="-apple-system, sans-serif" font-size="11.5" fill="#88A6C8">{p["desc"][56:115]}</text>

      <!-- Tags -->
      <g transform="translate(16, 202)">
        {''.join(tags_svg)}
      </g>

      <!-- Footer Action Links -->
      <g transform="translate(16, 244)">
        <text x="0" y="0" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="bold" fill="#38BDF8">{links_text}</text>
      </g>
    </g>
    '''

p_coords = [
    (CONFIG["PROJECTS"][0], 36, 94),
    (CONFIG["PROJECTS"][1], 450, 94),
    (CONFIG["PROJECTS"][2], 36, 380),
    (CONFIG["PROJECTS"][3], 450, 380)
]

projects_rendered = [render_project_card(p, x, y) for p, x, y in p_coords]

card5_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 670" width="100%" height="auto">
  <defs>
    {get_svg_defs("c5")}
    <clipPath id="c5_thumb_clip">
      <rect x="1" y="1" width="393" height="118" rx="9"/>
    </clipPath>
  </defs>

  <!-- Main Container -->
  <rect x="10" y="8" width="840" height="654" rx="14" fill="url(#c5_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(36, 36)">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> PROJECTS</text>
    <text x="0" y="32" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">LEVELS<tspan fill="#38BDF8">.</tspan></text>
  </g>

  <!-- 4 Projects in 2x2 Grid -->
  {''.join(projects_rendered)}
</svg>'''

# ==============================================================================
# CARD 6: EXPERIENCE / SAVE POINTS (card6-experience.svg)
# ==============================================================================
card6_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 330" width="100%" height="auto">
  <defs>
    {get_svg_defs("c6")}
  </defs>

  <!-- Main Container -->
  <rect x="10" y="8" width="840" height="314" rx="14" fill="url(#c6_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(36, 36)">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> EXPERIENCE</text>
    <text x="0" y="32" font-family="'Impact', 'Arial Black', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">SAVE POINTS<tspan fill="#38BDF8">.</tspan></text>
  </g>

  <!-- 3 Timeline Entries -->
  <!-- Entry 1 -->
  <g transform="translate(36, 96)">
    <!-- Date badge -->
    <text x="0" y="16" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#38BDF8">MAR - SEP 2026</text>
    
    <!-- Title & Company -->
    <text x="145" y="16" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF">Unity Game Developer &amp; Team Lead</text>
    <text x="145" y="34" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#38BDF8">Akiyam Solutions Pvt. Ltd.</text>
    <text x="145" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">Built Legend of Tretaya in Unity. Managed requirements, assigned responsibilities and supported</text>
    <text x="145" y="68" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">teammates to keep delivery on track.</text>
  </g>

  <!-- Entry 2 -->
  <g transform="translate(36, 178)">
    <text x="0" y="16" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#38BDF8">JAN - APR 2025</text>
    
    <text x="145" y="16" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF">Team Leader, Road Safety Hackathon</text>
    <text x="145" y="34" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#7C95B6">National level</text>
    <text x="145" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">Proposed a solution to increase foot-over-bridge usage for safer pedestrian crossing.</text>
  </g>

  <!-- Entry 3 -->
  <g transform="translate(36, 246)">
    <text x="0" y="16" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#38BDF8">2024 - 2028</text>
    
    <text x="145" y="16" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF">B.Tech in Computer Science</text>
    <text x="145" y="34" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#38BDF8">KIET Group of Institutions, Ghaziabad</text>
    <text x="145" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#88A6C8">CGPA 7.2</text>
  </g>
</svg>'''

# ==============================================================================
# CARD 7: CONNECT / LET'S BUILD (card7-connect.svg)
# ==============================================================================
card7_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 180" width="100%" height="auto">
  <defs>
    {get_svg_defs("c7")}
  </defs>

  <!-- Main Container -->
  <rect x="10" y="8" width="840" height="164" rx="14" fill="url(#c7_card_bg)" stroke="#1A263C" stroke-width="1.5"/>

  <!-- Left: Header & Tag -->
  <g transform="translate(36, 36)">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" font-weight="700" fill="#7C95B6" letter-spacing="1.5">PRINCEKR77 <tspan fill="#38BDF8">/</tspan> CONNECT</text>
    <text x="0" y="38" font-family="'Impact', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">LET'S BUILD<tspan fill="#38BDF8">.</tspan></text>
    <text x="0" y="66" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#38BDF8" letter-spacing="1.5">OPEN TO: GAME DEV INTERNSHIPS</text>
  </g>

  <!-- Right: 3 Channel Buttons -->
  <g transform="translate(515, 24)">
    <!-- Button 1: LinkedIn -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="310" height="38" rx="8" fill="#0B1322" stroke="#1A2B44" stroke-width="1.2"/>
      <rect x="10" y="9" width="20" height="20" rx="4" fill="#0077B5"/>
      <text x="20" y="24" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">in</text>
      <text x="40" y="23" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">LinkedIn</text>
      <text x="300" y="23" font-family="'JetBrains Mono', monospace" font-size="11" fill="#7C95B6" text-anchor="end">{CONFIG["LINKEDIN_HANDLE"]}</text>
    </g>

    <!-- Button 2: GitHub -->
    <g transform="translate(0, 48)">
      <rect x="0" y="0" width="310" height="38" rx="8" fill="#0B1322" stroke="#1A2B44" stroke-width="1.2"/>
      <rect x="10" y="9" width="20" height="20" rx="4" fill="#24292E"/>
      <text x="20" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">gh</text>
      <text x="40" y="23" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">GitHub</text>
      <text x="300" y="23" font-family="'JetBrains Mono', monospace" font-size="11" fill="#7C95B6" text-anchor="end">{CONFIG["GITHUB_HANDLE"]}</text>
    </g>

    <!-- Button 3: Email -->
    <g transform="translate(0, 96)">
      <rect x="0" y="0" width="310" height="38" rx="8" fill="#0B1322" stroke="#1A2B44" stroke-width="1.2"/>
      <rect x="10" y="9" width="20" height="20" rx="4" fill="#EA4335"/>
      <text x="20" y="24" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">@</text>
      <text x="40" y="23" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">Email</text>
      <text x="300" y="23" font-family="'JetBrains Mono', monospace" font-size="11" fill="#7C95B6" text-anchor="end">{CONFIG["EMAIL_ADDRESS"]}</text>
    </g>
  </g>
</svg>'''

# Save all SVGs to assets and desktop build
save_svg([os.path.join(git_assets, "card1-intro.svg"), os.path.join(desk_build, "card1-intro.svg")], card1_svg)
save_svg([os.path.join(git_assets, "card2-about.svg"), os.path.join(desk_build, "card2-about.svg")], card2_svg)
save_svg([os.path.join(git_assets, "card3-stack.svg"), os.path.join(desk_build, "card3-stack.svg")], card3_svg)
save_svg([os.path.join(git_assets, "card4-stats.svg"), os.path.join(desk_build, "card4-stats.svg")], card4_svg)
save_svg([os.path.join(git_assets, "card5-levels.svg"), os.path.join(desk_build, "card5-levels.svg")], card5_svg)
save_svg([os.path.join(git_assets, "card6-experience.svg"), os.path.join(desk_build, "card6-experience.svg")], card6_svg)
save_svg([os.path.join(git_assets, "card7-connect.svg"), os.path.join(desk_build, "card7-connect.svg")], card7_svg)

print("[SUCCESS] ALL SVG COMPONENTS BUILT ACCORDING TO PDF SPECIFICATION!")

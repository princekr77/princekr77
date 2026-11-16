"""
==============================================================================
🎮 PRINCE GUPTA - GITHUB PROFILE BUILDER
==============================================================================
This script generates pixel-perfect SVG profile cards identical to the master
Figma / PDF design, with dynamic real-time data fetched from GitHub API.

Highlight Block:
All configurable settings and manual stats are located directly below.
==============================================================================
"""

import os
import sys
import io
import json
import base64
import urllib.request
from PIL import Image, ImageDraw, ImageFont

# ==============================================================================
# 🎮 CONFIGURATION & MANUAL HIGHLIGHTED VALUES
# ==============================================================================
# You can easily edit any manual text or fallback values right here in the future:
GITHUB_USERNAME = "princekr77"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}"

# Fallback values if offline or GitHub API rate-limited
FALLBACK_STATS = {
    "repos": 16,
    "followers": 4
}

# Manual Stats shown in Box 3 and Box 4 of Card 4 (from Resume)
MANUAL_STATS = {
    "team_lead_duration": "6 mo",
    "team_lead_label": "Leading a game dev team",
    "game_dimensions": "2D + 3D",
    "game_dimensions_label": "Games across both"
}

# Project URLs for README interactive links
PROJECT_LINKS = {
    "silent_city_repo": "https://github.com/princekr77",
    "silent_city_apk": "https://github.com/princekr77",
    "monster_hunter_repo": "https://github.com/princekr77",
    "sword_warrior_repo": "https://github.com/princekr77",
    "sword_warrior_apk": "https://github.com/princekr77",
    "legend_of_tretaya": "https://github.com/princekr77",
    "linkedin": "https://linkedin.com/in/prince-gupta-b98189330",
    "email": "mailto:princekr2927@gmail.com",
    "github": f"https://github.com/{GITHUB_USERNAME}"
}
# ==============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
DESKTOP_BUILD = r"C:\Users\hp\Desktop\PRINCE_EXE_BUILD"

# Exact discovered Y pixel coordinates in master high-res design (2880 x 11472)
CARD_SLICES = [
    ("card1-intro", 100, 1600),
    ("card2-about", 1605, 3010),
    ("card3-stack", 3015, 4580),
    ("card4-stats", 4585, 5890),
    ("card5-levels", 5895, 8815),
    ("card6-experience", 8820, 10410),
    ("card7-connect", 10415, 11305)
]


def fetch_live_github_stats():
    """Fetch live public repository and follower counts from GitHub API."""
    stats = FALLBACK_STATS.copy()
    try:
        req = urllib.request.Request(
            GITHUB_API_URL,
            headers={"User-Agent": "PrinceProfileBuilder/2.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                stats["repos"] = data.get("public_repos", stats["repos"])
                stats["followers"] = data.get("followers", stats["followers"])
                print(f"[LIVE DATA] Successfully fetched: {stats['repos']} Repos, {stats['followers']} Followers")
    except Exception as e:
        print(f"[WARNING] GitHub API fetch failed ({e}). Using fallback: {stats}")
    return stats


def get_font(font_name, size, is_bold=False):
    """Load font safely across Windows and Linux environments."""
    possible_paths = [
        os.path.join(FONTS_DIR, font_name),
        os.path.join(r"C:\Windows\Fonts", font_name),
        os.path.join(r"C:\Windows\Fonts", "segoeuib.ttf" if is_bold else "segoeui.ttf"),
        os.path.join(r"C:\Windows\Fonts", "arialbd.ttf" if is_bold else "arial.ttf"),
        f"/usr/share/fonts/truetype/dejavu/{'DejaVuSans-Bold.ttf' if is_bold else 'DejaVuSans.ttf'}",
        f"/usr/share/fonts/truetype/liberation/{'LiberationSans-Bold.ttf' if is_bold else 'LiberationSans-Regular.ttf'}"
    ]
    for p in possible_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def render_card4_with_live_data(template_img, live_stats):
    """Dynamically render live GitHub stats onto Box 1 and Box 2 of Card 4."""
    img = template_img.copy()
    draw = ImageDraw.Draw(img)

    # 1. Erase old static Box 1 text ('4' and 'Unity projects built')
    # Background color of box container is #0F1221 -> RGB(15, 18, 33)
    draw.rectangle([1015, 440, 1800, 680], fill=(15, 18, 33))

    # 2. Erase old static Box 2 text ('3' and 'Platforms: Android, PC, WebGL')
    draw.rectangle([1880, 440, 2620, 680], fill=(15, 18, 33))

    # 3. Load Fonts
    font_number = get_font("segoeuib.ttf", 135, is_bold=True)
    font_label = get_font("segoeui.ttf", 44, is_bold=False)

    num_color = (242, 244, 255)  # Crisp white/off-white
    label_color = (168, 174, 192)  # High-contrast muted cyber blue

    # 4. Draw Box 1: Live GitHub Repos
    repos_str = str(live_stats["repos"])
    draw.text((1031, 455), repos_str, fill=num_color, font=font_number)
    draw.text((1031, 610), "GitHub repos", fill=label_color, font=font_label)

    # 5. Draw Box 2: Live GitHub Followers
    followers_str = str(live_stats["followers"])
    draw.text((1896, 455), followers_str, fill=num_color, font=font_number)
    draw.text((1896, 610), "GitHub followers", fill=label_color, font=font_label)

    return img


def create_svg_card(pil_image, output_svg_path):
    """Convert PIL image to ultra-crisp SVG card with embedded JPEG base64."""
    w, h = pil_image.size
    buffer = io.BytesIO()
    pil_image.save(buffer, format="JPEG", quality=95, optimize=True)
    b64_data = base64.b64encode(buffer.getvalue()).decode("ascii")

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="100%" height="auto">
  <image href="data:image/jpeg;base64,{b64_data}" xlink:href="data:image/jpeg;base64,{b64_data}" width="{w}" height="{h}" />
</svg>'''

    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[SUCCESS] Generated: {os.path.basename(output_svg_path)} ({os.path.getsize(output_svg_path) // 1024} KB)")


def build_live_stats_card():
    """Build or update only the dynamic live stats Card 4."""
    template_path = os.path.join(ASSETS_DIR, "card4_template.png")
    master_path = os.path.join(SCRIPT_DIR, "pdf_full_design.jpg")

    if os.path.exists(template_path):
        c4_base = Image.open(template_path)
    elif os.path.exists(master_path):
        master_img = Image.open(master_path)
        c4_base = master_img.crop((0, 4585, 2880, 5890))
    else:
        print("[ERROR] Neither card4_template.png nor pdf_full_design.jpg found!")
        return

    live_stats = fetch_live_github_stats()
    c4_rendered = render_card4_with_live_data(c4_base, live_stats)

    svg_path = os.path.join(ASSETS_DIR, "card4-stats.svg")
    create_svg_card(c4_rendered, svg_path)

    if os.path.exists(DESKTOP_BUILD):
        desktop_svg = os.path.join(DESKTOP_BUILD, "card4-stats.svg")
        try:
            create_svg_card(c4_rendered, desktop_svg)
        except Exception:
            pass


def build_all_profile_cards():
    """Build all 7 profile cards from master design and live stats."""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    os.makedirs(FONTS_DIR, exist_ok=True)

    master_path = os.path.join(SCRIPT_DIR, "pdf_full_design.jpg")
    if not os.path.exists(master_path):
        print("[INFO] Master design not found; building live stats card only.")
        build_live_stats_card()
        return

    master_img = Image.open(master_path)
    print(f"[STATUS] Loaded master design ({master_img.size[0]}x{master_img.size[1]})")

    # Fetch live GitHub stats
    live_stats = fetch_live_github_stats()

    for name, y0, y1 in CARD_SLICES:
        cropped = master_img.crop((0, y0, 2880, y1))

        # Card 4 gets dynamic live stats injection
        if name == "card4-stats":
            # Also save clean template for lightweight CI runs
            template_img = cropped.copy()
            draw_t = ImageDraw.Draw(template_img)
            draw_t.rectangle([1015, 440, 1800, 680], fill=(15, 18, 33))
            draw_t.rectangle([1880, 440, 2620, 680], fill=(15, 18, 33))
            template_img.save(os.path.join(ASSETS_DIR, "card4_template.png"), "PNG", optimize=True)

            cropped = render_card4_with_live_data(cropped, live_stats)

        svg_path = os.path.join(ASSETS_DIR, f"{name}.svg")
        create_svg_card(cropped, svg_path)

        # Mirror to Desktop build if exists
        if os.path.exists(DESKTOP_BUILD):
            desktop_svg = os.path.join(DESKTOP_BUILD, f"{name}.svg")
            try:
                create_svg_card(cropped, desktop_svg)
            except Exception:
                pass


def generate_readme():
    """Generate README.md with clean responsive SVGs and interactive links."""
    readme_content = f"""<div align="center">

<!-- ========================================== -->
<!-- 01. INTRO / HERO                           -->
<!-- ========================================== -->
<img src="assets/card1-intro.svg" width="100%" alt="Prince Kumar Gupta - Intro" />

<!-- ========================================== -->
<!-- 02. ABOUT / WHAT I BUILD                   -->
<!-- ========================================== -->
<img src="assets/card2-about.svg" width="100%" alt="What I Build - Combat Systems, Enemy AI, Mobile & PC, UI & XR" />

<!-- ========================================== -->
<!-- 03. SKILL TREE / TECH STACK                -->
<!-- ========================================== -->
<img src="assets/card3-stack.svg" width="100%" alt="Skill Tree - C#, Unity, Systems, XR, Platforms" />

<!-- ========================================== -->
<!-- 04. DEV PASS & LIVE BY THE NUMBERS         -->
<!-- ========================================== -->
<img src="assets/card4-stats.svg" width="100%" alt="Dev Pass & Live Statistics" />

<!-- ========================================== -->
<!-- 05. PROJECTS / MISSION SELECT              -->
<!-- ========================================== -->
<img src="assets/card5-levels.svg" width="100%" alt="Featured Projects: The Silent City, Monster Hunter, Sword Warrior, Legend of Tretaya" />

<!-- Interactive Quick Links for Projects -->
<p align="center">
  <b>The Silent City:</b> <a href="{PROJECT_LINKS['silent_city_repo']}">Source Code</a> &bull; <a href="{PROJECT_LINKS['silent_city_apk']}">Download APK</a> &nbsp;|&nbsp;
  <b>Monster Hunter:</b> <a href="{PROJECT_LINKS['monster_hunter_repo']}">Source Code</a><br>
  <b>Sword Warrior:</b> <a href="{PROJECT_LINKS['sword_warrior_repo']}">Source Code</a> &bull; <a href="{PROJECT_LINKS['sword_warrior_apk']}">Download APK</a> &nbsp;|&nbsp;
  <b>Legend of Tretaya:</b> <a href="{PROJECT_LINKS['legend_of_tretaya']}">Project Page</a>
</p>

<!-- ========================================== -->
<!-- 06. EXPERIENCE / SAVE POINTS               -->
<!-- ========================================== -->
<img src="assets/card6-experience.svg" width="100%" alt="Experience & Education - Akiyam Solutions, Road Safety Hackathon, KIET" />

<!-- ========================================== -->
<!-- 07. CONNECT / LET'S BUILD                  -->
<!-- ========================================== -->
<img src="assets/card7-connect.svg" width="100%" alt="Connect - LinkedIn, GitHub, Email" />

<!-- Interactive Social Badges -->
<p align="center">
  <a href="{PROJECT_LINKS['linkedin']}"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  &nbsp;
  <a href="{PROJECT_LINKS['github']}"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  &nbsp;
  <a href="{PROJECT_LINKS['email']}"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

---

<p align="center">
  <sub>🎮 Designed with Figma &bull; Powered by Unity &bull; Live GitHub Actions Sync</sub>
</p>

</div>
"""
    readme_path = os.path.join(SCRIPT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"[SUCCESS] Updated README.md ({os.path.getsize(readme_path)} bytes)")


def generate_preview():
    """Generate preview.html with GitHub Dark styling for instantaneous local viewing."""
    preview_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prince Gupta - GitHub Profile Preview</title>
  <style>
    body {
      background-color: #0d1117;
      color: #c9d1d9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 30px 15px;
      display: flex;
      justify-content: center;
    }
    .container {
      max-width: 980px;
      width: 100%;
      background: #010409;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 32px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }
    img {
      display: block;
      width: 100%;
      height: auto;
      margin: 0 auto;
    }
    .project-links {
      text-align: center;
      margin: 20px 0 35px 0;
      font-size: 14px;
      color: #8b949e;
    }
    .project-links a {
      color: #58a6ff;
      text-decoration: none;
      font-weight: 600;
    }
    .project-links a:hover {
      text-decoration: underline;
    }
    .social-links {
      text-align: center;
      margin: 25px 0;
    }
    .social-links a {
      display: inline-block;
      margin: 0 6px;
    }
    .footer {
      text-align: center;
      margin-top: 30px;
      font-size: 12px;
      color: #8b949e;
      border-top: 1px solid #21262d;
      padding-top: 15px;
    }
  </style>
</head>
<body>
  <div class="container">
    <img src="assets/card1-intro.svg" alt="Card 1 Intro" />
    <img src="assets/card2-about.svg" alt="Card 2 About" />
    <img src="assets/card3-stack.svg" alt="Card 3 Stack" />
    <img src="assets/card4-stats.svg" alt="Card 4 Stats" />
    <img src="assets/card5-levels.svg" alt="Card 5 Levels" />
    <div class="project-links">
      <b>The Silent City:</b> <a href="https://github.com/princekr77">Source Code</a> &bull; <a href="https://github.com/princekr77">Download APK</a> &nbsp;|&nbsp;
      <b>Monster Hunter:</b> <a href="https://github.com/princekr77">Source Code</a><br>
      <b>Sword Warrior:</b> <a href="https://github.com/princekr77">Source Code</a> &bull; <a href="https://github.com/princekr77">Download APK</a> &nbsp;|&nbsp;
      <b>Legend of Tretaya:</b> <a href="https://github.com/princekr77">Project Page</a>
    </div>
    <img src="assets/card6-experience.svg" alt="Card 6 Experience" />
    <img src="assets/card7-connect.svg" alt="Card 7 Connect" />
    <div class="social-links">
      <a href="https://linkedin.com/in/prince-gupta-b98189330"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" style="width:auto;display:inline-block;" alt="LinkedIn" /></a>
      <a href="https://github.com/princekr77"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" style="width:auto;display:inline-block;" alt="GitHub" /></a>
      <a href="mailto:princekr2927@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" style="width:auto;display:inline-block;" alt="Email" /></a>
    </div>
    <div class="footer">
      🎮 Designed with Figma &bull; Powered by Unity &bull; Live GitHub Actions Sync
    </div>
  </div>
</body>
</html>
"""
    preview_path = os.path.join(SCRIPT_DIR, "preview.html")
    with open(preview_path, "w", encoding="utf-8") as f:
        f.write(preview_content)
    print(f"[SUCCESS] Updated preview.html ({os.path.getsize(preview_path)} bytes)")


if __name__ == "__main__":
    print("==================================================")
    print("[START] BUILDING PRINCE GUPTA PROFILE ASSETS (SVG)")
    print("==================================================")
    build_all_profile_cards()
    generate_readme()
    generate_preview()
    print("==================================================")
    print("[ALL DONE] All 7 SVG cards built successfully!")
    print("==================================================")

import os
import sys
import json
import random
import datetime
import urllib.request
import urllib.error
from lion_vector_frames import LION_FRAMES

# Configuration & Constants
GITHUB_API_URL = "https://api.github.com/graphql"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "card_bg": "#161b22",
        "border": "#30363d",
        "text_primary": "#f0f6fc",
        "text_secondary": "#8b949e",
        "accent": "#e5a93c",
        "lion_glow": "rgba(229, 169, 60, 0.4)",
        "levels": [
            "#161b22",  # Level 0
            "#0e4429",  # Level 1
            "#006d32",  # Level 2
            "#26a641",  # Level 3
            "#39d353"   # Level 4
        ]
    },
    "light": {
        "bg": "#ffffff",
        "card_bg": "#f6f8fa",
        "border": "#d0d7de",
        "text_primary": "#24292f",
        "text_secondary": "#57606a",
        "accent": "#d49428",
        "lion_glow": "rgba(212, 148, 40, 0.3)",
        "levels": [
            "#ebedf0",
            "#9be9a8",
            "#40c463",
            "#30a14e",
            "#216e39"
        ]
    }
}

GRAPHQL_QUERY = """
query($username: String!) {
  user(login: $username) {
    name
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            color
            contributionCount
            date
            weekday
          }
        }
      }
    }
  }
}
"""

def fetch_github_contributions(username, token):
    """Fetch daily contribution calendar data from GitHub GraphQL API."""
    if not token or token == "YOUR_GITHUB_TOKEN":
        print(f"[INFO] No GitHub token provided. Generating realistic mock data for '{username}'.")
        return generate_mock_contributions(username)

    req = urllib.request.Request(
        GITHUB_API_URL,
        data=json.dumps({"query": GRAPHQL_QUERY, "variables": {"username": username}}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Lion-Contribution-Graph-Generator"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            if "errors" in result:
                print(f"[WARNING] GraphQL errors: {result['errors']}. Falling back to mock data.")
                return generate_mock_contributions(username)
            
            user_data = result.get("data", {}).get("user")
            if not user_data:
                print(f"[WARNING] User '{username}' not found. Falling back to mock data.")
                return generate_mock_contributions(username)
            
            calendar = user_data["contributionsCollection"]["contributionCalendar"]
            return calendar
    except Exception as e:
        print(f"[WARNING] HTTP Request failed: {e}. Falling back to mock data.")
        return generate_mock_contributions(username)


def generate_mock_contributions(username):
    """Generate realistic mock 52-week contribution data."""
    random.seed(hash(username) % 10000)
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=364)
    start_date -= datetime.timedelta(days=(start_date.weekday() + 1) % 7)
    
    weeks = []
    current_date = start_date
    total_contributions = 0

    for w in range(53):
        days = []
        for d in range(7):
            if current_date > today:
                break
            
            is_weekend = (d == 0 or d == 6)
            if is_weekend:
                count = random.choices([0, 1, 2, 4], weights=[60, 25, 10, 5])[0]
            else:
                count = random.choices([0, 1, 3, 6, 12, 18], weights=[15, 25, 30, 20, 7, 3])[0]

            total_contributions += count
            days.append({
                "contributionCount": count,
                "date": current_date.isoformat(),
                "weekday": d
            })
            current_date += datetime.timedelta(days=1)
        if days:
            weeks.append({"contributionDays": days})

    return {
        "totalContributions": total_contributions,
        "weeks": weeks
    }


def get_contribution_level(count):
    """Map contribution count to level 0..4."""
    if count == 0:
        return 0
    elif count <= 3:
        return 1
    elif count <= 6:
        return 2
    elif count <= 9:
        return 3
    else:
        return 4


def generate_svg(calendar, username, theme_name="dark", output_filename="github-contribution-grid-lion.svg"):
    """Generate the animated SVG file with contribution grid and running lion."""
    theme = THEMES.get(theme_name.lower(), THEMES["dark"])
    weeks = calendar.get("weeks", [])
    total_contributions = calendar.get("totalContributions", 0)

    cell_size = 10
    cell_gap = 3
    step_x = cell_size + cell_gap
    step_y = cell_size + cell_gap
    
    margin_left = 40
    margin_top = 55
    margin_bottom = 35
    
    num_weeks = len(weeks)
    grid_width = num_weeks * step_x
    svg_width = margin_left + grid_width + 40
    svg_height = margin_top + 7 * step_y + margin_bottom

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_labels = []
    last_month = -1

    for w_idx, week in enumerate(weeks):
        days = week.get("contributionDays", [])
        if days:
            first_day_date = days[0]["date"]
            dt = datetime.date.fromisoformat(first_day_date)
            if dt.month != last_month:
                month_labels.append({
                    "text": month_names[dt.month - 1],
                    "x": margin_left + w_idx * step_x
                })
                last_month = dt.month

    grid_cells_svg = []
    for w_idx, week in enumerate(weeks):
        x = margin_left + w_idx * step_x
        for day in week.get("contributionDays", []):
            d_idx = day["weekday"]
            y = margin_top + d_idx * step_y
            count = day["contributionCount"]
            level = get_contribution_level(count)
            color = theme["levels"][level]
            date_str = day["date"]
            
            grid_cells_svg.append(
                f'<rect class="contrib-cell cell-w{w_idx}-d{d_idx}" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" ry="2" fill="{color}"><title>{count} contributions on {date_str}</title></rect>'
            )

    lion_start_x = margin_left - 30
    lion_end_x = margin_left + grid_width - 40
    lion_y = margin_top + 7 * step_y - 45

    css_styles = f"""
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;display=swap');
        
        .bg {{ fill: {theme['bg']}; stroke: {theme['border']}; stroke-width: 1px; rx: 12px; ry: 12px; }}
        .header-title {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 14px; font-weight: 700; fill: {theme['text_primary']}; }}
        .header-subtitle {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 12px; font-weight: 400; fill: {theme['text_secondary']}; }}
        .label {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 9px; fill: {theme['text_secondary']}; }}
        .legend-text {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 9px; fill: {theme['text_secondary']}; }}
        
        .lion-runner {{
            animation: lionMove 12s linear infinite;
            transform-origin: center;
        }}

        @keyframes lionMove {{
            0% {{ transform: translate({lion_start_x}px, {lion_y}px); }}
            90% {{ transform: translate({lion_end_x}px, {lion_y}px); opacity: 1; }}
            95% {{ transform: translate({lion_end_x + 30}px, {lion_y}px); opacity: 0; }}
            96% {{ transform: translate({lion_start_x - 30}px, {lion_y}px); opacity: 0; }}
            100% {{ transform: translate({lion_start_x}px, {lion_y}px); opacity: 1; }}
        }}

        #lion-runner-group .frame-0 {{ animation: f0Anim 0.6s step-end infinite; }}
        #lion-runner-group .frame-1 {{ animation: f1Anim 0.6s step-end infinite; }}
        #lion-runner-group .frame-2 {{ animation: f2Anim 0.6s step-end infinite; }}
        #lion-runner-group .frame-3 {{ animation: f3Anim 0.6s step-end infinite; }}
        #lion-runner-group .frame-4 {{ animation: f4Anim 0.6s step-end infinite; }}
        #lion-runner-group .frame-5 {{ animation: f5Anim 0.6s step-end infinite; }}

        @keyframes f0Anim {{ 0%, 100% {{ opacity: 1; }} 16.6% {{ opacity: 0; }} }}
        @keyframes f1Anim {{ 0%, 16.6% {{ opacity: 0; }} 16.66% {{ opacity: 1; }} 33.3% {{ opacity: 0; }} }}
        @keyframes f2Anim {{ 0%, 33.3% {{ opacity: 0; }} 33.33% {{ opacity: 1; }} 50.0% {{ opacity: 0; }} }}
        @keyframes f3Anim {{ 0%, 50.0% {{ opacity: 0; }} 50.00% {{ opacity: 1; }} 66.6% {{ opacity: 0; }} }}
        @keyframes f4Anim {{ 0%, 66.6% {{ opacity: 0; }} 66.66% {{ opacity: 1; }} 83.3% {{ opacity: 0; }} }}
        @keyframes f5Anim {{ 0%, 83.3% {{ opacity: 0; }} 83.33% {{ opacity: 1; }} 100%  {{ opacity: 0; }} }}

        .lion-aura {{
            animation: pulseGlow 1.2s ease-in-out infinite alternate;
        }}
        @keyframes pulseGlow {{
            0% {{ transform: scale(0.95); opacity: 0.6; }}
            100% {{ transform: scale(1.1); opacity: 0.9; }}
        }}

        .contrib-cell {{
            transition: transform 0.2s ease, fill 0.3s ease;
        }}
        .contrib-cell:hover {{
            stroke: {theme['accent']};
            stroke-width: 1.5px;
            transform: scale(1.2);
        }}
    """

    svg_content = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">',
        f'<defs>',
        f'<style type="text/css">{css_styles}</style>',
        f'<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">',
        f'  <feGaussianBlur stdDeviation="3" result="blur" />',
        f'  <feComposite in="SourceGraphic" in2="blur" operator="over" />',
        f'</filter>',
        ''.join(LION_FRAMES),
        f'</defs>',
        f'<rect class="bg" width="{svg_width}" height="{svg_height}" x="0" y="0"/>',
        
        f'<g transform="translate({margin_left}, 30)">',
        f'  <path d="M -15 -10 C -18 -15 -10 -20 0 -15 C 10 -20 18 -15 15 -10 C 20 0 15 10 0 12 C -15 10 -20 0 -15 -10 Z" fill="{theme["accent"]}" transform="scale(0.7) translate(-10,-5)"/>',
        f'  <text class="header-title" x="12" y="-2">@{username}\'s Contribution Kingdom</text>',
        f'  <text class="header-subtitle" x="{svg_width - margin_left - 160}" y="-2">{total_contributions:,} contributions in the last year</text>',
        f'</g>',

        '<g>',
        ''.join([f'<text class="label" x="{m["x"]}" y="{margin_top - 10}">{m["text"]}</text>' for m in month_labels]),
        '</g>',

        '<g>',
        f'<text class="label" x="{margin_left - 28}" y="{margin_top + 1 * step_y + 8}">Mon</text>',
        f'<text class="label" x="{margin_left - 28}" y="{margin_top + 3 * step_y + 8}">Wed</text>',
        f'<text class="label" x="{margin_left - 28}" y="{margin_top + 5 * step_y + 8}">Fri</text>',
        '</g>',

        '<g>',
        ''.join(grid_cells_svg),
        '</g>',

        f'<g transform="translate({svg_width - 150}, {svg_height - 18})">',
        f'<text class="legend-text" x="-28" y="9">Less</text>',
        ''.join([f'<rect x="{i*13}" y="0" width="10" height="10" rx="2" ry="2" fill="{theme["levels"][i]}"/>' for i in range(5)]),
        f'<text class="legend-text" x="68" y="9">More</text>',
        '</g>',

        f'<g id="lion-runner-group" class="lion-runner">',
        f'  <ellipse class="lion-aura" cx="60" cy="45" rx="40" ry="12" fill="{theme["lion_glow"]}" filter="url(#glow)"/>',
        f'  <g class="frame-0"><use href="#lion-frame-0"/></g>',
        f'  <g class="frame-1"><use href="#lion-frame-1"/></g>',
        f'  <g class="frame-2"><use href="#lion-frame-2"/></g>',
        f'  <g class="frame-3"><use href="#lion-frame-3"/></g>',
        f'  <g class="frame-4"><use href="#lion-frame-4"/></g>',
        f'  <g class="frame-5"><use href="#lion-frame-5"/></g>',
        f'</g>',

        '</svg>'
    ]

    final_svg = '\n'.join(svg_content)
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(final_svg)
    
    print(f"[SUCCESS] Generated SVG saved to: {output_filename}")
    return output_filename


def main():
    username = os.environ.get("GITHUB_USERNAME", "bgukhan204-tech")
    token = os.environ.get("GITHUB_TOKEN", os.environ.get("GH_TOKEN", ""))
    theme = os.environ.get("THEME", "dark")
    output_filename = os.environ.get("OUTPUT_FILENAME", "github-contribution-grid-lion.svg")

    if len(sys.argv) > 1:
        username = sys.argv[1]
    if len(sys.argv) > 2:
        theme = sys.argv[2]

    print(f"[INFO] Generating Lion Contribution Graph for user '{username}' (Theme: {theme})...")
    calendar = fetch_github_contributions(username, token)
    generate_svg(calendar, username, theme_name=theme, output_filename=output_filename)


if __name__ == "__main__":
    main()

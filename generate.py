#!/usr/bin/env python3
"""Builds the animated SVGs used by the profile README from live GitHub data.
Run locally (needs the `gh` CLI logged in) or daily from GitHub Actions. Outputs to assets/.
Everything is self-hosted SVG, so it renders the same on phone, laptop and the GitHub app."""
import json, re, subprocess, textwrap, html, datetime, pathlib

OWNER = "Vedhrishi"
OUT = pathlib.Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

# Hand-written, truthful descriptions (what each project is), merged with live numbers from the API.
REPOS = [
    ("meta-maps", "Meta Maps",
     "Crowdsourced road-hazard navigation with a Guardian rerouting agent, live traffic and hands-free voice control.",
     "https://vedhrishi.github.io/meta-maps/"),
    ("RISHI-INDIAN-STOCKS-EXPLAINED", "RISHI | Indian Stocks Explained",
     "Financial-literacy video series for first-time Indian investors, with a live website that gathers every episode.",
     "https://rishi-indian-stocks-explained.vercel.app"),
    ("INTELLITRAP", "IntelliTrap",
     "Secure cloud storage with a RandomForest risk-scoring layer that flags suspicious sessions for an admin.",
     "https://intellitrap-batch-3.vercel.app"),
    ("AI-PLASTIC-SORTING-WEBSITE", "Plastic Decoder",
     "In-browser plastic resin identification with YOLOv8 and ResNet-18. Photos never leave the device.",
     "https://plastic-decoder-project.vercel.app"),
    ("BIO-LOCK", "BioLock SSD",
     "Face-recognition lock for external drives with multi-step liveness checks, built with OpenCV and Python.",
     None),
    ("bschool-atlas", "B-School Atlas",
     "Compare MBA destinations, Indian B-school cut-offs by exam and payback, with sidebar navigation and site-wide search.",
     "https://vedhrishi.github.io/bschool-atlas/"),
]
LANG_COLOR = {"Python": "#3776ab", "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "HTML": "#e34c26", "CSS": "#8a63d2",
              "PLpgSQL": "#336791", "PowerShell": "#5391fe", "Batchfile": "#c1f12e"}
NAVY, CARD, INK, MUTED, ACCENT = "#0b1220", "#121a2b", "#eaf0ff", "#8fa0c0", "#4cc2ff"
FONT = "font-family=\"'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif\""


def gh(*a):
    return subprocess.run(["gh", *a], capture_output=True, text=True, check=True).stdout


def commits(repo):
    out = gh("api", "-i", f"repos/{OWNER}/{repo}/commits?per_page=1")
    m = re.search(r'[?&]page=(\d+)>; rel="last"', out)
    return int(m.group(1)) if m else 1


def collect():
    rows = []
    for repo, title, blurb, live in REPOS:
        meta = json.loads(gh("api", f"repos/{OWNER}/{repo}"))
        langs = json.loads(gh("api", f"repos/{OWNER}/{repo}/languages"))
        rows.append(dict(repo=repo, title=title, blurb=blurb, live=live, langs=langs, commits=commits(repo),
                         pushed=meta["pushed_at"][:10], size=meta["size"], topics=meta.get("topics", [])))
    return rows


def esc(s):
    return html.escape(s, quote=True)


def top_langs(langs, n=3):
    tot = sum(langs.values()) or 1
    return [(k, v / tot) for k, v in sorted(langs.items(), key=lambda kv: -kv[1])[:n] if v / tot >= 0.015]


# ---------------------------------------------------------------- animated banner (static file, no data)
def banner():
    roles = ["Final-year B.Tech CSE", "Data &amp; analytics internship seeker", "Pipelines · ML scoring · computer vision", "6 projects, all documented"]
    spans = "".join(
        f'<text x="500" y="168" text-anchor="middle" fill="{INK}" font-size="26" {FONT} opacity="0">{r}'
        f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.06;0.22;0.28;1" dur="16s" begin="{i*4}s" repeatCount="indefinite"/></text>'
        for i, r in enumerate(roles))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 260" role="img" aria-label="Pasupuleti Vedh Rishi, final-year B.Tech CSE, data and analytics internship seeker">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#14305a"/></linearGradient>
<linearGradient id="w" x1="0" x2="1"><stop offset="0" stop-color="#4cc2ff" stop-opacity=".0"/><stop offset=".5" stop-color="#4cc2ff" stop-opacity=".35"/><stop offset="1" stop-color="#7c5cff" stop-opacity=".0"/></linearGradient>
<clipPath id="r"><rect width="1000" height="260" rx="22"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="1000" height="260" fill="url(#g)"/>
<path fill="url(#w)" d="M0 200 C 150 150 300 250 500 200 S 850 150 1000 200 V260 H0Z"><animateTransform attributeName="transform" type="translate" values="-60 0;60 0;-60 0" dur="9s" repeatCount="indefinite"/></path>
<path fill="url(#w)" opacity=".7" d="M0 220 C 200 180 350 260 520 215 S 860 175 1000 225 V260 H0Z"><animateTransform attributeName="transform" type="translate" values="50 0;-50 0;50 0" dur="12s" repeatCount="indefinite"/></path>
{"".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4cc2ff" opacity=".5"><animate attributeName="cy" values="{y};{y-30};{y}" dur="{d}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".15;.7;.15" dur="{d}s" repeatCount="indefinite"/></circle>' for x,y,r,d in [(90,70,3,5),(220,190,2,6),(780,60,3,7),(900,150,2,5),(640,30,2,8),(140,130,2,6)])}
<text x="500" y="112" text-anchor="middle" fill="#fff" font-size="48" font-weight="700" letter-spacing="-1" {FONT}>Pasupuleti Vedh Rishi
<animate attributeName="opacity" values="0;1" dur="1.2s" fill="freeze"/></text>
{spans}</g></svg>'''


# ---------------------------------------------------------------- stats dashboard
def stats(rows):
    total_commits = sum(r["commits"] for r in rows)
    agg = {}
    for r in rows:
        for k, v in r["langs"].items():
            agg[k] = agg.get(k, 0) + v
    tot = sum(agg.values()) or 1
    langs = sorted(agg.items(), key=lambda kv: -kv[1])[:6]
    tiles = [(len(rows), "projects"), (total_commits, "commits"), (sum(1 for r in rows if r["live"]), "live demos"), (len(agg), "languages")]
    t = ""
    for i, (n, label) in enumerate(tiles):
        x = 30 + i * 235
        t += (f'<g transform="translate({x},28)" opacity="0"><animate attributeName="opacity" values="0;1" dur=".6s" begin="{i*.15}s" fill="freeze"/>'
              f'<animateTransform attributeName="transform" type="translate" values="{x},44;{x},28" dur=".6s" begin="{i*.15}s" fill="freeze"/>'
              f'<rect width="215" height="92" rx="16" fill="{CARD}" stroke="#22304d"/>'
              f'<text x="107" y="50" text-anchor="middle" font-size="40" font-weight="700" fill="{ACCENT}" {FONT}>{n}</text>'
              f'<text x="107" y="76" text-anchor="middle" font-size="16" fill="{MUTED}" {FONT}>{label}</text></g>')
    bars = ""
    for i, (k, v) in enumerate(langs):
        y = 175 + i * 34
        w = max(6, int(600 * v / tot / (langs[0][1] / tot)))   # relative to the biggest language
        c = LANG_COLOR.get(k, "#8892b0")
        bars += (f'<text x="30" y="{y+14}" font-size="16" fill="{INK}" {FONT}>{esc(k)}</text>'
                 f'<rect x="150" y="{y}" width="640" height="18" rx="9" fill="#1a2540"/>'
                 f'<rect x="150" y="{y}" height="18" rx="9" fill="{c}" width="0"><animate attributeName="width" values="0;{w}" dur="1.1s" begin="{.5+i*.12}s" fill="freeze" calcMode="spline" keySplines=".16 1 .3 1" keyTimes="0;1"/></rect>'
                 f'<text x="{150+w+10}" y="{y+14}" font-size="14" fill="{MUTED}" {FONT}>{v/tot*100:.0f}%</text>')
    h = 175 + len(langs) * 34 + 20
    today = datetime.date.today().strftime("%d %b %Y")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {h}" role="img" aria-label="GitHub activity: {len(rows)} projects, {total_commits} commits">
<rect width="1000" height="{h}" rx="22" fill="{NAVY}"/>{t}
<text x="30" y="152" font-size="20" font-weight="600" fill="{INK}" {FONT}>Languages across all projects</text>{bars}
<text x="970" y="{h-12}" text-anchor="end" font-size="12" fill="{MUTED}" {FONT}>auto-updated {today}</text></svg>'''


# ---------------------------------------------------------------- one card per repo
def card(i, r):
    lines = textwrap.wrap(r["blurb"], 46)[:3]
    desc = "".join(f'<text x="28" y="{98+k*24}" font-size="17" fill="{MUTED}" {FONT}>{esc(l)}</text>' for k, l in enumerate(lines))
    chips, x = "", 28
    for name, share in top_langs(r["langs"]):
        c = LANG_COLOR.get(name, "#8892b0"); label = f"{name} {share*100:.0f}%"; w = 22 + len(label) * 8
        chips += (f'<g transform="translate({x},182)"><rect width="{w}" height="28" rx="14" fill="#1a2540"/><circle cx="14" cy="14" r="5" fill="{c}"/>'
                  f'<text x="26" y="19" font-size="13" fill="{INK}" {FONT}>{esc(label)}</text></g>'); x += w + 8
    live = f'<text x="452" y="40" text-anchor="end" font-size="13" font-weight="700" fill="#3ddc97" {FONT}>● LIVE</text>' if r["live"] else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 240" role="img" aria-label="{esc(r['title'])}">
<defs><linearGradient id="s{i}" x1="0" x2="1"><stop offset="0" stop-color="#4cc2ff" stop-opacity="0"/><stop offset=".5" stop-color="#4cc2ff" stop-opacity=".9"/><stop offset="1" stop-color="#7c5cff" stop-opacity="0"/></linearGradient></defs>
<rect width="480" height="240" rx="20" fill="{CARD}" stroke="#22304d"/>
<rect x="28" y="56" width="120" height="3" rx="1.5" fill="url(#s{i})"><animate attributeName="x" values="28;332;28" dur="5s" repeatCount="indefinite"/></rect>
<text x="28" y="42" font-size="22" font-weight="700" fill="{INK}" {FONT}>{esc(r['title'])}<animate attributeName="opacity" values="0;1" dur=".7s" fill="freeze"/></text>{live}
{desc}{chips}
<text x="28" y="228" font-size="13" fill="{MUTED}" {FONT}>{r['commits']} commit{'s' if r['commits'] != 1 else ''} · updated {r['pushed']}</text></svg>'''



# ---------------------------------------------------------------- featured project banner (static, animated)
def featured():
    route = "M70 292 C 190 292 210 210 330 205 S 520 215 600 150 S 790 120 930 92"
    alt = "M330 205 C 380 285 520 300 640 250 S 840 170 930 92"
    ch, cx = "", 28
    for t in ["Hazard-aware routes", "Guardian reroute", "Hey Meta voice control", "4.9M places offline in India"]:
        w = len(t) * 8.2 + 30
        ch += f'<g transform="translate({cx:.0f},318)"><rect width="{w:.0f}" height="30" rx="15" fill="#1a2540" stroke="#2a3b66"/><text x="15" y="20" font-size="13" fill="{INK}" {FONT}>{t}</text></g>'
        cx += w + 10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" role="img" aria-label="Meta Maps: a hazard on the route, the Guardian switches to a safer road">
<defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#13294f"/></linearGradient>
<clipPath id="fc"><rect width="1000" height="380" rx="22"/></clipPath>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1d2c4d" stroke-width="1"/></pattern></defs>
<g clip-path="url(#fc)"><rect width="1000" height="380" fill="url(#fg)"/><rect width="1000" height="380" fill="url(#grid)" opacity=".7"/>
<text x="28" y="52" font-size="13" font-weight="700" fill="{ACCENT}" letter-spacing="2" {FONT}>FEATURED PROJECT</text>
<text x="28" y="96" font-size="44" font-weight="700" fill="#fff" letter-spacing="-1" {FONT}>Meta Maps</text>
<text x="28" y="126" font-size="17" fill="{MUTED}" {FONT}>Navigation that warns you about the road, not just the route.</text>
<path id="main" d="{route}" fill="none" stroke="#5b6b8c" stroke-width="7" stroke-linecap="round" opacity=".55"/>
<path d="{alt}" fill="none" stroke="#3ddc97" stroke-width="5" stroke-linecap="round" stroke-dasharray="10 9" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;.42;.5;.92;1" dur="9s" repeatCount="indefinite"/></path>
<path d="{route}" fill="none" stroke="{ACCENT}" stroke-width="5" stroke-linecap="round" stroke-dasharray="1100" stroke-dashoffset="1100"><animate attributeName="stroke-dashoffset" values="1100;0;0;0" keyTimes="0;.3;.92;1" dur="9s" repeatCount="indefinite"/></path>
<g><circle cx="600" cy="150" r="18" fill="#ff5a5f" opacity=".25"><animate attributeName="r" values="10;30;10" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values=".5;0;.5" dur="2s" repeatCount="indefinite"/></circle>
<circle cx="600" cy="150" r="9" fill="#ff5a5f"/><text x="600" y="155" text-anchor="middle" font-size="13" font-weight="800" fill="#fff" {FONT}>!</text>
<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;.28;.34;1" dur="9s" repeatCount="indefinite"/></g>
<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;.4;.46;.9;1" dur="9s" repeatCount="indefinite"/>
<rect x="28" y="138" width="330" height="56" rx="14" fill="#101a30" stroke="#3ddc97"/>
<text x="44" y="162" font-size="14" font-weight="700" fill="#3ddc97" {FONT}>Guardian</text>
<text x="44" y="183" font-size="13" fill="{INK}" {FONT}>Accident ahead. Switching to a clear road, +1 min.</text></g>
<g><circle r="9" fill="#fff" stroke="{ACCENT}" stroke-width="4"/>
<animateMotion dur="9s" repeatCount="indefinite" keyPoints="0;.5;.5;1" keyTimes="0;.42;.46;1" calcMode="linear" path="{route}"/></g>
{ch}
<text x="972" y="364" text-anchor="end" font-size="12" fill="{MUTED}" {FONT}>React · TypeScript · MapLibre · FastAPI</text></g></svg>'''


# ---------------------------------------------------------------- one featured card per live project (static, animated)
LIVE = [
    ("stocks", "RISHI | Indian Stocks Explained", "Financial literacy for first-time Indian investors, as short animated episodes.",
     ["100 episodes", "200 short videos", "Twice-daily releases"], "https://rishi-indian-stocks-explained.vercel.app", "rishi-indian-stocks-explained.vercel.app"),
    ("intellitrap", "IntelliTrap", "Secure cloud storage that scores every session for risk and diverts suspicious ones to decoy data.",
     ["RandomForest scoring", "Admin threat console", "Supabase row-level security"], "https://intellitrap-batch-3.vercel.app", "intellitrap-batch-3.vercel.app"),
    ("plastic", "Plastic Decoder", "Identifies plastic types from a photo, on the device, so photos never leave the phone.",
     ["YOLOv8 + ResNet-18", "Lighthouse 100 SEO", "Works on-device"], "https://plastic-decoder-project.vercel.app", "plastic-decoder-project.vercel.app"),
    ("atlas", "B-School Atlas", "Compare MBA destinations and Indian B-school cut-offs by exam, percentile and payback.",
     ["Site-wide search", "30 automated tests", "Auto-deployed from GitHub"], "https://vedhrishi.github.io/bschool-atlas/", "vedhrishi.github.io/bschool-atlas"),
]


def live_motif(kind):
    if kind == "stocks":
        bars = ""
        for i, (h, up) in enumerate([(40, 1), (70, 1), (55, 0), (95, 1), (80, 0), (120, 1), (150, 1)]):
            x = 640 + i * 44
            c = "#3ddc97" if up else "#ff5a5f"
            bars += (f'<rect x="{x}" y="{250-h}" width="26" height="{h}" rx="4" fill="{c}" opacity=".85"><animate attributeName="height" values="0;{h}" dur="1s" begin="{i*.18}s" fill="freeze"/>'
                     f'<animate attributeName="y" values="250;{250-h}" dur="1s" begin="{i*.18}s" fill="freeze"/></rect>')
        return bars + '<polyline points="653,200 697,170 741,185 785,140 829,150 873,105 917,70" fill="none" stroke="#4cc2ff" stroke-width="3" stroke-dasharray="500" stroke-dashoffset="500"><animate attributeName="stroke-dashoffset" values="500;0" dur="2s" begin=".6s" fill="freeze"/></polyline>'
    if kind == "intellitrap":
        return (f'<path d="M780 50 L880 85 V160 C880 215 835 245 780 262 C725 245 680 215 680 160 V85 Z" fill="#121f3a" stroke="#4cc2ff" stroke-width="3"/>'
                '<circle cx="780" cy="150" r="46" fill="none" stroke="#4cc2ff" stroke-width="2"><animate attributeName="r" values="30;70;30" dur="3s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="3s" repeatCount="indefinite"/></circle>'
                '<rect x="735" y="205" width="90" height="12" rx="6" fill="#1a2540"/><rect x="735" y="205" width="20" height="12" rx="6" fill="#3ddc97"><animate attributeName="width" values="20;88;20" dur="5s" repeatCount="indefinite"/><animate attributeName="fill" values="#3ddc97;#ffb020;#ff5a5f;#3ddc97" dur="5s" repeatCount="indefinite"/></rect>'
                f'<text x="780" y="236" text-anchor="middle" font-size="13" fill="{MUTED}" {FONT}>session risk</text>')
    if kind == "plastic":
        return (f'<path d="M770 52 h40 v22 l16 26 v130 a14 14 0 0 1 -14 14 h-44 a14 14 0 0 1 -14 -14 v-130 l16 -26 z" fill="#121f3a" stroke="#4cc2ff" stroke-width="3"/>'
                '<rect x="730" y="120" width="120" height="3" fill="#3ddc97" opacity=".9"><animate attributeName="y" values="90;240;90" dur="3s" repeatCount="indefinite"/></rect>'
                + "".join(f'<g transform="translate({690+i*52},262)"><rect width="46" height="24" rx="12" fill="#1a2540" stroke="#2a3b66"/><text x="23" y="16" text-anchor="middle" font-size="12" fill="{INK}" {FONT}>{t}'
                          f'<animate attributeName="fill" values="{INK};#3ddc97;{INK}" dur="4s" begin="{i}s" repeatCount="indefinite"/></text></g>' for i, t in enumerate(["PET", "HDPE", "PP", "PS"])))
    bars = ""
    for i, h in enumerate([50, 90, 120, 80, 150]):
        x = 660 + i * 50
        bars += (f'<rect x="{x}" y="{250-h}" width="32" height="{h}" rx="6" fill="#4cc2ff" opacity="{.45+i*.1:.2f}"><animate attributeName="height" values="0;{h}" dur=".9s" begin="{i*.15}s" fill="freeze"/>'
                 f'<animate attributeName="y" values="250;{250-h}" dur=".9s" begin="{i*.15}s" fill="freeze"/></rect>')
    return bars + f'<circle cx="905" cy="52" r="30" fill="none" stroke="#7c5cff" stroke-width="3" stroke-dasharray="190" stroke-dashoffset="190"><animate attributeName="stroke-dashoffset" values="190;55" dur="1.8s" begin=".8s" fill="freeze"/></circle><text x="905" y="57" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}" {FONT}>MBA</text>'


def live_card(i, kind, title, blurb, chips, url, short):
    lines = textwrap.wrap(blurb, 52)[:3]
    desc = "".join(f'<text x="32" y="{118+k*26}" font-size="18" fill="{MUTED}" {FONT}>{esc(l)}</text>' for k, l in enumerate(lines))
    ch, cx = "", 32
    for t in chips:
        w = len(t) * 8 + 30
        ch += f'<g transform="translate({cx:.0f},206)"><rect width="{w:.0f}" height="30" rx="15" fill="#1a2540" stroke="#2a3b66"/><text x="15" y="20" font-size="13" fill="{INK}" {FONT}>{esc(t)}</text></g>'
        cx += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" role="img" aria-label="{esc(title)}, live project">
<defs><linearGradient id="lg{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#13294f"/></linearGradient><clipPath id="lc{i}"><rect width="1000" height="300" rx="22"/></clipPath>
<pattern id="gr{i}" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1d2c4d" stroke-width="1"/></pattern></defs>
<g clip-path="url(#lc{i})"><rect width="1000" height="300" fill="url(#lg{i})"/><rect width="1000" height="300" fill="url(#gr{i})" opacity=".7"/>
<circle cx="40" cy="44" r="6" fill="#3ddc97"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="54" y="49" font-size="13" font-weight="700" fill="#3ddc97" letter-spacing="2" {FONT}>LIVE</text>
<text x="32" y="92" font-size="34" font-weight="700" fill="#fff" letter-spacing="-.5" {FONT}>{esc(title)}</text>{desc}{ch}
<text x="32" y="276" font-size="14" fill="{ACCENT}" {FONT}>{esc(short)}</text>{live_motif(kind)}</g></svg>'''

# ---------------------------------------------------------------- skills chips (only tools used in the repos)
def skills():
    groups = [("Languages", ["Python", "TypeScript", "JavaScript"]),
              ("Web", ["React", "Vite", "Tailwind CSS", "FastAPI", "Supabase", "Vercel", "Render", "GitHub Pages"]),
              ("Maps and voice", ["MapLibre GL", "OSRM routing", "Overture Maps", "DuckDB", "TomTom Traffic", "Web Speech API"]),
              ("Data & ML", ["PostgreSQL", "SQLite", "scikit-learn", "YOLOv8", "ResNet-18", "OpenCV", "Gemini Vision"]),
              ("Delivery", ["Git", "GitHub Actions", "Playwright", "FFmpeg"])]
    y, out, n = 36, "", 0
    for g, items in groups:
        out += f'<text x="24" y="{y}" font-size="14" font-weight="700" fill="{MUTED}" letter-spacing="1.5" {FONT}>{esc(g.upper())}</text>'
        x = 24; y += 14
        for it in items:
            w = 28 + len(it.replace("&amp;", "&")) * 9
            if x + w > 960: x = 24; y += 44
            out += (f'<g transform="translate({x},{y})" opacity="0"><animate attributeName="opacity" values="0;1" dur=".5s" begin="{n*.07}s" fill="freeze"/>'
                    f'<rect width="{w}" height="34" rx="17" fill="#162241" stroke="#2a3b66"/><text x="{w/2}" y="22" text-anchor="middle" font-size="15" fill="{INK}" {FONT}>{it}</text></g>')
            x += w + 10; n += 1
        y += 62
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {y}" role="img" aria-label="Tools used"><rect width="1000" height="{y}" rx="22" fill="{NAVY}"/>{out}</svg>'


if __name__ == "__main__":
    rows = collect()
    (OUT / "banner.svg").write_text(banner(), encoding="utf8")
    (OUT / "stats.svg").write_text(stats(rows), encoding="utf8")
    (OUT / "featured-meta-maps.svg").write_text(featured(), encoding="utf8")
    for j, spec in enumerate(LIVE):
        (OUT / f"live-{spec[0]}.svg").write_text(live_card(j, *spec), encoding="utf8")
    (OUT / "skills.svg").write_text(skills(), encoding="utf8")
    for i, r in enumerate(rows):
        (OUT / f"card-{i+1}.svg").write_text(card(i, r), encoding="utf8")
    json.dump(rows, open(OUT / "repos.json", "w"), indent=1)
    print("generated", len(rows), "cards")

#!/usr/bin/env python3
"""Ridge Project Pulse: tarjeta SVG con DATOS REALES de ridge-lang/ridge
(release, CI, changelog, crates, stars, issues, last update). La genera el
workflow pulse.yml a diario. Lee la API con el token en env GH_TOKEN.
-> assets/pulse.svg"""
import os, json, urllib.request
from datetime import datetime, timezone

REPO = "ridge-lang/ridge"
TOKEN = os.environ.get("GH_TOKEN", "")


def api(path):
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except Exception as e:
        print("warn:", path, e)
        return None


def rel_time(iso):
    try:
        t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        s = (datetime.now(timezone.utc) - t).total_seconds()
        if s < 3600: return f"{int(s//60)}m ago"
        if s < 86400: return f"{int(s//3600)}h ago"
        return f"{int(s//86400)}d ago"
    except Exception:
        return "—"


repo = api(f"/repos/{REPO}") or {}
default = repo.get("default_branch", "main")
rel = api(f"/repos/{REPO}/releases/latest") or {}
runs = api(f"/repos/{REPO}/actions/runs?per_page=1&branch={default}") or {}
crates = api(f"/repos/{REPO}/contents/crates")

tag = rel.get("tag_name") or "unreleased"
body = (rel.get("body") or repo.get("description") or "").strip()
changelog = next((l.strip(" #*-").strip() for l in body.splitlines() if l.strip()), "—")
if len(changelog) > 58:
    changelog = changelog[:56].rstrip() + "…"
wr = (runs.get("workflow_runs") or [{}])[0]
ci = (wr.get("conclusion") or wr.get("status") or "—")
stars = repo.get("stargazers_count", 0)
issues = repo.get("open_issues_count", 0)
crates_n = len(crates) if isinstance(crates, list) else "—"
updated = rel_time(repo.get("pushed_at", ""))

ci_ok = ci == "success"
ci_txt = "passing" if ci_ok else ("failing" if ci == "failure" else str(ci))
ci_col = "#39d353" if ci_ok else ("#ff5f56" if ci == "failure" else "#8b949e")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def stat(x, y, label, value, col="#e6edf3"):
    return (f'<text x="{x}" y="{y}" font-size="13" fill="#8b949e">{esc(label)}</text>'
            f'<text x="{x+150}" y="{y}" font-size="15" font-weight="700" '
            f'fill="{col}" text-anchor="end">{esc(value)}</text>')


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 230" width="820" height="230" font-family="'JetBrains Mono','Fira Code',Consolas,monospace" role="img" aria-label="Ridge project pulse">
<defs><style>.dot{{animation:b 2s ease-in-out infinite}}@keyframes b{{0%,100%{{opacity:.45}}50%{{opacity:1}}}}</style></defs>
<rect x="1" y="1" width="818" height="228" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="24" y="36" font-size="16" font-weight="600"><tspan fill="#39d353">$ </tspan><tspan fill="#e6edf3">ridge --status</tspan><tspan fill="#8b949e">   ·   {REPO}</tspan></text>

<circle class="dot" cx="36" cy="86" r="7" fill="#39d353"/>
<text x="54" y="94" font-size="30" font-weight="800" fill="#e6edf3">{esc(tag)}</text>
<text x="56" y="116" font-size="12" fill="#8b949e">latest release</text>

<text x="24" y="156" font-size="15"><tspan fill="#8b949e">CI&#160;&#160;</tspan><tspan fill="{ci_col}" font-weight="700">{esc(ci_txt)}</tspan></text>
<text x="24" y="190" font-size="14" xml:space="preserve"><tspan fill="#39d353">&gt; </tspan><tspan fill="#8b949e" font-style="italic">{esc(changelog)}</tspan></text>

<line x1="540" y1="64" x2="540" y2="196" stroke="#21262d"/>
{stat(570, 90, "crates", crates_n, "#39d353")}
{stat(570, 120, "stars", stars)}
{stat(570, 150, "open issues", issues)}
{stat(570, 180, "updated", updated, "#bb9af7")}

<text x="24" y="216" font-size="11" fill="#484f58">live · auto-updated daily from the Ridge repo</text>
</svg>'''

open("assets/pulse.svg", "w", encoding="utf-8").write(svg)
print(f"assets/pulse.svg: {tag}, CI {ci_txt}, {crates_n} crates, {stars} stars, updated {updated}")

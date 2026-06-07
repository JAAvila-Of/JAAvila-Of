<!--
  ════════════════════════════════════════════════════════════════════
  README de PERFIL de GitHub — JAAvila-Of   ·   estilo: TERMINAL / HACKER
  Va en el repo público llamado EXACTAMENTE "JAAvila-Of".
  Aparece en https://github.com/JAAvila-Of
  Placeholders [ASÍ] => reemplázalos. Ver ../PUBLICAR.md y ../SETUP-WIDGETS.md
  Paleta: verde #39d353 (terminal) · morado #bb9af7 (Ridge) · fondo #0d1117
  ════════════════════════════════════════════════════════════════════
-->

<div align="center">

<!-- Banner ASCII art (figlet Doom) rasterizado + shimmer -->
<img src="./assets/banner.gif" alt="JAAvila" width="720" />

<br/>

<!-- Terminal ANIMADA (SVG con CSS keyframes). Si no anima por proxy, usa la raw URL:
     https://raw.githubusercontent.com/JAAvila-Of/JAAvila-Of/main/assets/terminal.svg -->
<img src="./assets/terminal.svg" alt="jose@ridge terminal" width="720" />

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=900&color=39D353&center=true&vCenter=true&width=620&lines=Creator+of+Ridge+%F0%9F%A6%80;.NET+Foundation+member+%F0%9F%92%9C;Compilers+%C2%B7+type+systems+%C2%B7+dev+tooling;Backend+engineer+desde+Per%C3%BA+%F0%9F%87%B5%F0%9F%87%AA" alt="taglines" />

<p>
  <img src="https://komarev.com/ghpvc/?username=JAAvila-Of&label=visitors&color=39d353&style=flat-square" alt="visitors" />
  <a href="https://github.com/JAAvila-Of?tab=followers"><img src="https://img.shields.io/github/followers/JAAvila-Of?label=follow&style=flat-square&color=39d353&labelColor=0d1117" alt="followers" /></a>
  <img src="https://img.shields.io/badge/Peru-%F0%9F%87%B5%F0%9F%87%AA-39d353?style=flat-square&labelColor=0d1117" alt="peru" />
</p>

</div>

---

## `~/whoami`

```console
$ whoami
> Jóse Angel Avila  —  language designer & backend engineer  🦀

$ cat ./about.txt
> 🇪🇸 Creador de Ridge, un lenguaje funcional tipado para la BEAM (en Rust).
>    Me obsesionan los compiladores, los sistemas de tipos y el dev tooling.
> 🇬🇧 Creator of Ridge, a typed functional language for the BEAM (in Rust).
>    Obsessed with compilers, type systems and developer tooling.

$ cat ./affiliations.txt
> .NET Foundation  ·  member 💜
> ridge-lang       ·  founder 🦀

$ ridge --ask-me-about
> compilers · type systems · Rust · C#/.NET · the BEAM · auth
```

---

## `~/ridge --showcase`  🦀

> **[Ridge](https://github.com/ridge-lang/ridge)** — a typed functional language for the BEAM.
> Hindley-Milner inference · row polymorphism · actor-first concurrency · effects/capabilities tracked in the type system.

```haskell
-- A pure step of Conway's Game of Life, in Ridge.
import std.list as List

type Grid = { rows: Int, cols: Int, cells: List (List Bool) }

fn nextCell (grid: Grid) (r: Int) (c: Int) -> Bool =
    match (cellAt grid r c, liveNeighbours grid r c)
        (true,  2) -> true   -- survives
        (true,  3) -> true   -- survives
        (false, 3) -> true   -- born
        _          -> false  -- dies / stays dead
```

<div align="center">

<!-- Compilador en vivo — SVG animados (reemplazan el diagrama estático) -->
<img src="./assets/pipeline.svg" alt="The Ridge compiler pipeline (animated)" width="840" />

<img src="./assets/type-infer.svg" alt="Hindley-Milner type inference (animated)" width="840" />

<img src="./assets/actors.svg" alt="BEAM actor processes passing messages (animated)" width="840" />

<sub><i>compiler pipeline · Hindley-Milner inference · actor-first concurrency — Core Erlang/BEAM 🟢, LLVM &amp; WASM exploratory</i></sub>

</div>

<div align="center">

<!-- Game of Life ASCII animado — corre uno de mis ejemplos de Ridge en vivo -->
<img src="./assets/gol.svg" alt="Conway's Game of Life running in ASCII" width="520" />

<sub><i>☝️ <code>game_of_life.ridge</code> — a Gosper glider gun, evolving live.</i></sub>

</div>

---

## `~/stack --list`

<div align="center">
  <img src="https://skillicons.dev/icons?i=rust,cs,dotnet,elixir,erlang,ts,js,svelte,tailwind,nodejs,graphql,flutter,git,github,vscode&theme=dark&perline=8" alt="stack" />
</div>

---

## `~/projects --pinned`

| Project | Description | Tech |
|---|---|---|
| 🦀 **[Ridge](https://github.com/ridge-lang/ridge)** ⭐ | Typed functional language for the BEAM. HM inference, row polymorphism, actor-first concurrency, capabilities in the type system. Compiles to Core Erlang/BEAM; native (LLVM) & WASM backends are exploratory. *(In active development.)* | Rust · BEAM |
| 🐙 **[agm-cli](https://github.com/JAAvila-Of/agm-cli)** | CLI & Rust library to parse, validate, render and orchestrate *Agent Graph Memory* (AGM) files for AI-agent workflows. Born out of the **Octopus** project. | Rust |
| 💜 **[JAAvila.FluentOperations](https://github.com/JAAvila-Of/JAAvila.FluentOperations)** | Large fluent **validation & assertive-testing** library for .NET — thread-safe, chained operations that unify inline `.Test()` assertions with model **Quality Blueprints**. 6,500+ tests; covers strings, numbers, dates, collections — even **architecture rules** (type & assembly). Integrations: DI, ASP.NET Core, Minimal API, MediatR, gRPC, OpenAPI & Roslyn analyzers. | C# / .NET |
| 🛡️ **[JAAvila.SafeTypes](https://github.com/JAAvila-Of/JAAvila.SafeTypes)** | My very **first** .NET library 💚 — lightweight type-safety utilities to dodge null-reference errors and enforce stricter, compile-time contracts (e.g. `source.SafeNull()`). Humble, but where the journey began. | C# / .NET |
| 💉 **[418Apps-COVID](https://github.com/JAAvila-Of/418Apps-COVID)** | COVID-19 vaccination tracker for Peru using official open data. | Svelte · TS |

---

## `~/stats --all`

<div align="center">

<img src="./github-metrics.svg" alt="GitHub metrics — stats, languages & activity" />

<img src="https://github-readme-streak-stats.herokuapp.com/?user=JAAvila-Of&hide_border=true&background=0d1117&stroke=39d353&ring=39d353&fire=bb9af7&currStreakLabel=39d353&sideLabels=c9d1d9&dates=8b949e&currStreakNum=c9d1d9&sideNums=c9d1d9" alt="streak" />

</div>

#### 📈 Activity

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=JAAvila-Of&hide_border=true&bg_color=0d1117&color=39d353&line=39d353&point=bb9af7&area=true&area_color=39d353" alt="activity graph" />
</div>

#### ⚡ Project pulse — live

<div align="center">
  <!-- Pulse de Ridge — datos REALES, auto-actualizado por pulse.yml -->
  <img src="./assets/pulse.svg" alt="Ridge project pulse (live)" width="840" />
</div>

---

## `~/now-playing`  🎧

<div align="center">
  <!-- SPOTIFY: reemplaza 31lwszpsc3lnbnvzdtflhmvz65ei por tu uid (login en spotify-github-profile.kittinanx.com). Ver ../SETUP-WIDGETS.md -->
  <a href="https://open.spotify.com/user/31lwszpsc3lnbnvzdtflhmvz65ei">
    <img src="https://spotify-github-profile.kittinanx.com/api/view?uid=31lwszpsc3lnbnvzdtflhmvz65ei&cover_image=true&theme=default&show_offline=true&background_color=0d1117&bar_color=39d353&bar_color_cover=true" alt="Spotify now playing" />
  </a>
</div>

---

## `~/connect`

<div align="center">

<a href="https://www.linkedin.com/in/jaavila418"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn" /></a>
<a href="mailto:jaavila.dev@outlook.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email" /></a>
<a href="https://github.com/ridge-lang/ridge"><img src="https://img.shields.io/badge/Ridge_lang-39d353?style=flat-square&logo=rust&logoColor=black&labelColor=0d1117" alt="Ridge" /></a>
<!-- Opcionales: descomenta los que uses
<a href="[TU-WEB]"><img src="https://img.shields.io/badge/Website-000000?style=flat-square&logo=aboutdotme&logoColor=white&labelColor=0d1117" alt="Website" /></a>
<a href="[TU-X]"><img src="https://img.shields.io/badge/X-000000?style=flat-square&logo=x&logoColor=white&labelColor=0d1117" alt="X" /></a>
-->

</div>

```console
$ echo "Thanks for visiting!  ·  ¡Gracias por pasar!"
> ⭐ Star Ridge if you like it: github.com/ridge-lang/ridge
> _
```

<!-- Voronoi dinámico como franja de cierre -->
<img src="./assets/voronoi.svg" alt="" width="100%" />

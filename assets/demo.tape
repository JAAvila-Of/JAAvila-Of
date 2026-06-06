# ── VHS tape: graba una sesión REAL de terminal a GIF ──────────────
# Requiere: https://github.com/charmbracelet/vhs  (y `ridge` en el PATH)
#   instalar:  winget install charmbracelet.vhs   (o scoop/brew)
#   grabar:    vhs assets/demo.tape   ->  genera assets/demo.gif
# Ajusta los comandos a lo que quieras lucir de Ridge.

Output assets/demo.gif

Require ridge

Set Shell pwsh
Set FontFamily "JetBrains Mono"
Set FontSize 20
Set Width 1200
Set Height 640
Set Padding 24
Set BorderRadius 12
Set TypingSpeed 60ms
Set Theme { "name": "ridge-terminal", "background": "#0d1117", "foreground": "#c9d1d9", "cursor": "#39d353", "selection": "#264f78", "black": "#0d1117", "red": "#ff5f56", "green": "#39d353", "yellow": "#ffbd2e", "blue": "#58a6ff", "magenta": "#bb9af7", "cyan": "#39c5cf", "white": "#c9d1d9", "brightGreen": "#39d353", "brightMagenta": "#bb9af7" }

# pausa inicial limpia
Hide
Type "clear" Enter
Show

Sleep 600ms
Type "ridge --version"
Sleep 400ms
Enter
Sleep 1.5s

Type "ridge run examples/game_of_life.ridge"
Sleep 400ms
Enter
Sleep 4s

Type "# compiled & ran on the BEAM 🟢"
Sleep 800ms
Enter
Sleep 1.5s

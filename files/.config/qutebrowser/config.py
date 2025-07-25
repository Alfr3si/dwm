# type: ignore
config.load_autoconfig(False)

# Muestra estas categorías al autocompletar con :open
c.completion.open_categories = [
    "searchengines",
    "quickmarks",
    "bookmarks",
    "history",
    "filesystem",
]
# Carga configuraciones hechas con :set o :bind
config.load_autoconfig(True)
# Guarda la sesión automáticamente al cerrar o reiniciar
c.auto_save.session = True

# --- Colores fijos en lugar de xresources ---
c.colors.statusbar.normal.bg = "#1e1e2e"
c.colors.statusbar.command.bg = "#1e1e2e"
c.colors.statusbar.command.fg = "#cdd6f4"
c.colors.statusbar.normal.fg = "#89b4fa"
c.colors.tabs.bar.bg = "#1e1e2e"
c.colors.tabs.even.bg = "#313244"
c.colors.tabs.odd.bg = "#313244"
c.colors.tabs.even.fg = "#cdd6f4"
c.colors.tabs.odd.fg = "#cdd6f4"
c.colors.tabs.selected.even.bg = "#89b4fa"
c.colors.tabs.selected.even.fg = "#1e1e2e"
c.colors.tabs.selected.odd.bg = "#89b4fa"
c.colors.tabs.selected.odd.fg = "#1e1e2e"

# --- Barra de estado estilo Tokyonight ---
c.colors.statusbar.normal.bg = "#1a1b26"
c.colors.statusbar.normal.fg = "#c0caf5"
c.colors.statusbar.command.bg = "#1a1b26"
c.colors.statusbar.command.fg = "#7aa2f7"
c.colors.statusbar.insert.bg = "#7aa2f7"
c.colors.statusbar.insert.fg = "#1a1b26"
c.colors.statusbar.caret.bg = "#bb9af7"
c.colors.statusbar.caret.fg = "#1a1b26"
c.colors.statusbar.caret.selection.bg = "#bb9af7"
c.colors.statusbar.caret.selection.fg = "#1a1b26"
c.colors.statusbar.passthrough.bg = "#414868"
c.colors.statusbar.passthrough.fg = "#c0caf5"
c.colors.statusbar.private.bg = "#343b58"
c.colors.statusbar.private.fg = "#c0caf5"
c.colors.statusbar.progress.bg = "#7aa2f7"
c.colors.statusbar.url.fg = "#c0caf5"
c.colors.statusbar.url.success.http.fg = "#1a1b26"
c.colors.statusbar.url.success.https.fg = "#1a1b26"
c.colors.statusbar.url.error.fg = "#f7768e"
c.colors.statusbar.url.hover.fg = "#7aa2f7"
c.colors.statusbar.url.warn.fg = "#bb9af7"

# --- Tabs ---
c.statusbar.show = "in-mode"
c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 20
c.tabs.show = "multiple"
c.tabs.padding = {"top": 5, "bottom": 5, "left": 9, "right": 9}
c.tabs.indicator.width = 0
c.tabs.width = "7%"

# --- Zoom ---
c.zoom.default = "120%"

# --- Fuentes ---
c.fonts.default_size = "12pt"
c.fonts.web.family.fixed = "Sans"
c.fonts.web.family.sans_serif = "Sans"
c.fonts.web.family.serif = "Sans"
c.fonts.web.family.standard = "Sans"

# --- keybindings ---
config.bind("h", "history")
config.bind("tH", "config-cycle tabs.show multiple never")
config.bind("sH", "config-cycle statusbar.show always never")
# Navegación y enlaces
config.bind("T", "hint links tab")  # Usar hints para abrir enlace en nueva pestaña
# Portapapeles (solo clipboard estándar en Wayland)
config.bind("pp", "open -- {clipboard}")  # Abrir URL del clipboard en pestaña actual
config.bind("pt", "open -t -- {clipboard}")  # Abrir URL del clipboard en nueva pestaña
# Pestañas
config.bind(
    "tT", "config-cycle tabs.position top left"
)  # Alternar posición de pestañas
config.bind("gJ", "tab-move +")  # Mover pestaña actual a la derecha
config.bind("gK", "tab-move -")  # Mover pestaña actual a la izquierda
config.bind("gm", "tab-move")  # Mover pestaña al inicio

# --- Privacidad ---
config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)
c.content.blocking.enabled = True
# c.content.blocking.method = 'adblock' # uncomment this if you install python-adblock
# c.content.blocking.adblock.lists = [
#         "https://github.com/ewpratten/youtube_ad_blocklist/blob/master/blocklist.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"]

# --- Modo oscuro ---
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.policy.images = "never"
config.set("colors.webpage.darkmode.enabled", False, "file://*")

# --- opciones de busqueda ---
c.url.start_pages = "https://www.google.com"
c.url.default_page = "https://www.google.com"

c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "!ddg": "https://duckduckgo.com/?q={}",
    "!lite": "https://lite.duckduckgo.com/lite/?q={}",
    "!aw": "https://wiki.archlinux.org/?search={}",
    "!yt": "https://www.youtube.com/results?search_query={}",
    "!gh": "https://github.com/search?o=desc&q={}&s=stars",
}

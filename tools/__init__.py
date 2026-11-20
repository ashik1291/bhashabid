# Bhashabid Tools Package

# Dev tools print Bengali/Unicode status lines; keep them from crashing on cp1252 consoles.
from bhashabid.cli import ensure_utf8_stdio as _ensure_utf8_stdio

_ensure_utf8_stdio()

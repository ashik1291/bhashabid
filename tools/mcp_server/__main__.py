# tools/mcp_server/__main__.py
import sys

# Force UTF-8 encoding on standard I/O streams across all platforms
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from .server import main

if __name__ == "__main__":
    sys.exit(main() or 0)

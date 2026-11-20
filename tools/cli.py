"""Development alias of `bhashabid.cli`."""
import importlib
import sys

if __name__ == "__main__":
    from bhashabid.cli import main
    sys.exit(main())

sys.modules[__name__] = importlib.import_module("bhashabid.cli")

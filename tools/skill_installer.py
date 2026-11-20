"""Development alias of `bhashabid.skill_installer`."""
import importlib
import sys

if __name__ == "__main__":
    from bhashabid.skill_installer import main
    sys.exit(main())

sys.modules[__name__] = importlib.import_module("bhashabid.skill_installer")

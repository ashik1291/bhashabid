"""Development alias of `bhashabid.normalize.orthography`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.orthography")

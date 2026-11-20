"""Development alias of `bhashabid.legal.deeds`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.legal.deeds")

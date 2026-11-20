"""Development alias of `bhashabid.creative.lapidary`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.creative.lapidary")

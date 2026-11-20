"""Development alias of `bhashabid.normalize.unicode`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.unicode")

"""Development alias of `bhashabid.lint.honorifics`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.lint.honorifics")

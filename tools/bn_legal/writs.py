"""Development alias of `bhashabid.legal.writs`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.legal.writs")

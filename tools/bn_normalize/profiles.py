"""Development alias of `bhashabid.normalize.profiles`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.profiles")

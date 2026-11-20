"""Development alias of `bhashabid.normalize.repair`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.repair")

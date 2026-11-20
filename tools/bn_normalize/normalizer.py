"""Development alias of `bhashabid.normalize.normalizer`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.normalizer")

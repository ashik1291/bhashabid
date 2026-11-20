"""Development alias of `bhashabid.normalize.lexicon`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.lexicon")

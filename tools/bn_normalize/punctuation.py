"""Development alias of `bhashabid.normalize.punctuation`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.normalize.punctuation")

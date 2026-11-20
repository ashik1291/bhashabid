"""Development alias of `bhashabid.numbers.currency`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.currency")

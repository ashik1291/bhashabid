"""Development alias of `bhashabid.numbers.digits`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.digits")

"""Development alias of `bhashabid.numbers.fractions`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.fractions")

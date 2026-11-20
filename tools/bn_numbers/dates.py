"""Development alias of `bhashabid.numbers.dates`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.dates")
